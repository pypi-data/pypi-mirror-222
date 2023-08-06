import os
from rich.progress import Progress, BarColumn, TextColumn, TimeRemainingColumn, FileSizeColumn


def format_file_size(file_size):
    if file_size >= 1024 ** 5:  # Petabyte
        return f"{file_size / (1024 ** 5):.2f} PB"
    elif file_size >= 1024 ** 4:  # Terabyte
        return f"{file_size / (1024 ** 4):.2f} TB"
    elif file_size >= 1024 ** 3:  # Gigabyte
        return f"{file_size / (1024 ** 3):.2f} GB"
    elif file_size >= 1024 ** 2:  # Megabyte
        return f"{file_size / (1024 ** 2):.2f} MB"
    elif file_size >= 1024:  # Kilobyte
        return f"{file_size / 1024:.2f} kB"
    elif file_size >= 8:  # Byte
        return f"{file_size} bytes"
    else:  # Bit
        return f"{file_size * 8} bits"


def getTotalSize(srcPaths):
    total_size = 0
    for path in srcPaths:
        if os.path.isfile(path):
            total_size += os.path.getsize(path)
        else:
            for r, d, files in os.walk(path):
                for f in files:
                    fp = os.path.join(r, f)
                    total_size += os.path.getsize(fp)
    return total_size


def regular_copy(src, dst, console, task, progress):
    with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
        while True:
            buf = fsrc.read(1024*1024)
            if not buf:
                break
            fdst.write(buf)
            progress.update(task, advance=len(buf))
            progress.refresh()


def verbose_copy(src, dst, console, current, total_files):

    file_size = os.path.getsize(src)

    with Progress(
        BarColumn(bar_width=50),
        "[progress.percentage]{task.percentage:>3.0f}%",
        TimeRemainingColumn(),
        "[#ea2a6f][[/#ea2a6f]",
        FileSizeColumn(),
        "[#ea2a6f]/[/#ea2a6f]",
        TextColumn(f"[bold cyan]{format_file_size(file_size)}[/bold cyan]"),
        "[#ea2a6f]][/#ea2a6f]",
        f"({current} of {total_files})",
        console=console,
        auto_refresh=False
    ) as progress:
        task = progress.add_task("", total=file_size, file_size=format_file_size(file_size))

        with open(src, 'rb') as fsrc, open(dst, 'wb') as fdst:
            while not progress.finished:
                buf = fsrc.read(1024*1024)
                if not buf:
                    break
                fdst.write(buf)
                progress.update(task, advance=len(buf))
                progress.refresh()


def hlp():
    print("""
usage: ptrack [-h] [-v] [-c] [-m]

A simple CLI utility for asthetically tracking progress when copying or moving files.

options:
  -h, --help     show this help message and exit
  -v, --verbose  verbose output
  -c, --copy     copy files (You can use `ptc` instead of `ptrack -c`)
  -m, --move     move files (You can use `ptm` instead of `ptrack -m`)
""")
