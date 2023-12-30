#!/usr/bin/env python3

"""Wallpaper changer."""
import pathlib
import time
import os
import random
import argparse


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
    # wait for hyprland to start
    home_dir = pathlib.Path.home()
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", type=str, help="The path to the wallpapers.")
    args = parser.parse_args()
    time.sleep(1)
    wallpapers_dir = home_dir / "Pictures" / "wallpapers"
    if args.d:
        try:
            wallpapers_dir = pathlib.Path(args.d)
        except Exception as e:
            print(e)
    while True:
        change_wallpapers(wallpapers_dir)
