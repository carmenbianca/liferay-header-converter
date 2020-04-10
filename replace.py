# SPDX-License-Identifier: LGPL-2.0-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

from liferay_header_converter import replace_header, all_files


def main():
    for file_ in all_files():
        try:
            replace_header(file_)
        except Exception:
            print(file_)


if __name__ == "__main__":
    main()
