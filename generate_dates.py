# SPDX-License-Identifier: LGPL-2.0-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

import json
import subprocess
import os

from liferay_header_converter import all_files, get_latest_date, ROOT_PATH


def main():
    dates = dict()

    # Remove all untracked files
    subprocess.run(["git", "clean", "-dxf"])
    # Change the mtime of all files to the last time they were modified. Through
    # some voodoo in `restore-mtime`, this is much quicker than requesting the
    # last modified time via `git log`.
    subprocess.run(["git", "restore-mtime"])

    for file_ in all_files():
        dates[file_] = get_latest_date(file_).isoformat()

    with open(os.path.join(ROOT_PATH, "dates.json"), "w") as fp:
        json.dump(dates, fp, indent=1)


if __name__ == "__main__":
    main()
