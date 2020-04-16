# SPDX-License-Identifier: LGPL-2.1-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

from liferay_header_converter import replace_header, all_files


def main():
    files = list(all_files())
    total = len(files)
    replaced = 0
    skipped = 0

    for file_ in files:
        try:
            replace_header(file_)
            replaced += 1
        except Exception:
            print(file_)
            skipped += 1

    print(replaced, skipped)


if __name__ == "__main__":
    main()
