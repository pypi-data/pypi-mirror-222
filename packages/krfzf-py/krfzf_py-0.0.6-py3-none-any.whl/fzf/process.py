import importlib
import shutil
import subprocess
import typing

T = typing.TypeVar("T")


get_opts = importlib.import_module(".options", __package__).get_opts

EXECUTABLE = "fzf"


def ensure_stdin_available(f):
    def __inner__(self, *args, **kwargs):
        if self.process.stdin.closed:
            return

        return f(self, *args, **kwargs)

    return __inner__


class Fzf:
    fetch_options = staticmethod(get_opts)

    def __init__(
        self,
        executable=EXECUTABLE,
        opts=None,
        disable_env: bool = False,
        *,
        encoding="utf-8",
        encoding_errors="strict"
    ):
        opts = opts or []

        if shutil.which(executable) is None:
            raise RuntimeError(
                "fzf was not found in PATH. Please ensure that the process can access fzf."
            )

        self.process = subprocess.Popen(
            [EXECUTABLE, *opts],
            stdout=subprocess.PIPE,
            stdin=subprocess.PIPE,
            env={} if disable_env else None,
        )
        self.encoding_options = {
            "encoding": encoding,
            "errors": encoding_errors,
        }

    @classmethod
    def load_with_options(
        cls,
        *,
        executable=EXECUTABLE,
        encoding="utf-8",
        encoding_errors="strict",
        **opts
    ):
        return cls(
            executable=executable,
            opts=Fzf.fetch_options(**opts),
            encoding=encoding,
            encoding_errors=encoding_errors,
        )

    @ensure_stdin_available
    def add_lines(self, lines: typing.Iterable[str], flush_last: bool = True):
        for line in lines:
            if not self.to_stdin(
                data=line.encode(**self.encoding_options) + b"\n", flush=not flush_last
            ):
                return

        if flush_last:
            self.to_stdin(flush=True)

    @property
    def is_alive(self):
        return self.process.poll() is None

    def close(self):
        try:
            if not self.process.stdin.closed:
                self.process.stdin.close()
        except OSError:
            pass

    def to_stdin(self, data: typing.Optional[typing.AnyStr] = None, flush: bool = True):
        try:
            if data is not None:
                self.process.stdin.write(data)
            if flush:
                self.process.stdin.flush()

        except (BrokenPipeError, OSError):
            return False

        return True

    @ensure_stdin_available
    def pipe_from_stream(
        self, stream: typing.IO[typing.AnyStr], flush_last: bool = True
    ):
        for line in stream:
            if not self.to_stdin(line, flush=not flush_last):
                return

        if flush_last:
            self.to_stdin(flush=True)

    def get_output(self):
        self.process.wait()

        stdout = self.process.stdout.read().decode(**self.encoding_options)

        if not stdout:
            return None

        if any(multi_opt in self.process.args for multi_opt in ("-m", "--multi")):
            return stdout[:-1].split("\n")

        return stdout[:-1]

    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


def fzf_prompt(
    components: typing.Iterable[T],
    processor: typing.Optional[typing.Callable[[T], str]] = None,
    escape_output: bool = True,
    encoding: str = "utf-8",
    encoding_errors: str = "strict",
    duplication_treatment: typing.Callable[[str], str] = lambda value: value + "*",
    flush_last: bool = False,
    *,
    executable=EXECUTABLE,
    **opts
) -> typing.Union[T, typing.List[T]]:
    with Fzf.load_with_options(
        executable=executable,
        encoding=encoding,
        encoding_errors=encoding_errors,
        **opts
    ) as fzf:
        if escape_output:
            output_escape = lambda value: repr(value)[
                1:-1
            ]  # type: typing.Callable[[str], str]
        else:
            output_escape = lambda value: value  # type: typing.Callable[[str], str]

        if processor:
            shallow_copy = {}

            def raw_process_save(value: str, processed_value: str):
                if processed_value in shallow_copy:
                    return raw_process_save(
                        value, duplication_treatment(processed_value)
                    )

                shallow_copy.update(
                    {
                        processed_value: value,
                    }
                )
                return processed_value

            generator = (
                raw_process_save(value, output_escape(processor(value)))
                for value in components
            )
        else:
            generator = (output_escape(value) for value in components)

        fzf.add_lines(lines=generator, flush_last=flush_last)

    output = fzf.get_output()

    if processor and output is not None:
        if isinstance(output, list):
            return [shallow_copy[value] for value in output]

        return shallow_copy[output]

    return output


def get_fzf_version(executable=EXECUTABLE):
    with Fzf(executable, ["--version"]) as fzf:
        return fzf.get_output()
