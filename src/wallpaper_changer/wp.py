#!/usr/bin/env python3

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
    parser.add_argument("-d", type=str, help="The path to the wallpapers.")
    args = parser.parse_args()
    home_dir = pathlib.Path.home()
    # set a default path
    wallpapers_dir = home_dir / "Pictures" / "wallpapers"
    if args.d:
        try:
            wallpapers_dir = pathlib.Path(args.d)
        except Exception as e:
            print(e)
    if not wallpapers_dir.exists():
        print(f"Error: The path \"{wallpapers_dir}\" does not exist!")
        exit(1)

    # wait for hyprland to start
    time.sleep(1)
    while True:
        change_wallpapers(wallpapers_dir)
