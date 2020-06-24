# SPDX-License-Identifier: LGPL-2.1-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

from multiprocessing.pool import ThreadPool
import argparse
import sys

from liferay_header_converter import (
    replace_header,
    all_files,
    get_latest_date,
    get_earliest_date,
)


def inner(file_, use_creation_date=False):
    try:
        replace_header(file_, use_creation_date)
        print(file_)
        return True
    except Exception:
        return False


def main(args=None):
    if args is None:
        args = sys.argv[1:]

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--creation-date",
        action="store_true",
        help="use creation date instead of last modification date. This is **expensive**.",
    )

    parsed = parser.parse_args(args)

    files = list(all_files())

    pool = ThreadPool()
    pool.starmap(inner, ((file_, parsed.creation_date) for file_ in files))


if __name__ == "__main__":
    main()
