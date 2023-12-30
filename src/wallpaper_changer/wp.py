#!/usr/bin/env python3

###############################################################################
# Requires swww-daemon to be running                                          #
###############################################################################

"""Wallpaper changer."""
import argparse
import os
import pathlib
import random
import time


def change_wallpapers(wallpapers_dir: pathlib.Path) -> None:
    """Change the wallpapers."""
    nps = [str(p).replace(" ", r"\ ") for p in wallpapers_dir.iterdir()]
    if not nps:
        time.sleep(300)
        return
    random.shuffle(nps)
    for np in nps:
        os.popen(f"swww img {np}")
        time.sleep(300)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-d",
        type=pathlib.Path,
        dest="wallpapers_dir",
        help="The path to the wallpapers.",
        default=pathlib.Path("~/Pictures/wallpapers").expanduser()
    )
    args = parser.parse_args()
    home_dir = pathlib.Path.home()
    # set a default path
    if not args.wallpapers_dir.exists() \
            or not args.wallpapers_dir.is_dir():
        print(
            f"Error: The path \"{args.wallpapers_dir}\" does not exist or \
is not a directory!"
        )
        exit(1)

    # wait for hyprland to start
    time.sleep(1)
    while True:
        change_wallpapers(args.wallpapers_dir)
