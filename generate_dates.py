# SPDX-License-Identifier: LGPL-2.1-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

import subprocess

def main():
    # Remove all untracked files
    subprocess.run(["git", "clean", "-dxf"])
    # Change the mtime of all files to the last time they were modified. Through
    # some voodoo in `restore-mtime`, this is much quicker than requesting the
    # last modified time via `git log`.
    subprocess.run(["git", "restore-mtime"])


if __name__ == "__main__":
    main()
