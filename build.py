#!/usr/bin/env python3
import json
import pathlib
import shutil

MOD_NAME = "silent-buildings"
MOD_PATH = pathlib.Path("silent-buildings")


def main():
    with open(MOD_PATH / "info.json") as f:
        version = json.load(f)["version"]

    output_name = f"{MOD_NAME}_{version}"
    if pathlib.Path(f"{output_name}.zip").exists():
        if input("Already exists, overwrite? (y/N): ").strip().lower() not in ("y", "yes"):
            print("Done nothing.")
            return

    shutil.make_archive(output_name, "zip", base_dir=MOD_PATH)

    print("Building done.")

if __name__ == "__main__":
    main()
