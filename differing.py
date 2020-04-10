# SPDX-License-Identifier: LGPL-2.0-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

import glob
import os
from difflib import SequenceMatcher

from liferay_header_converter import ORIGINAL, LEN_ORIGINAL


def main():
    files = glob.glob("**/*.js", recursive=True)
    result = dict()

    for file_ in files:
        if not os.path.isfile(file_):
            continue

        with open(file_) as fp:
            contents = fp.read(LEN_ORIGINAL)

        ratio = SequenceMatcher(a=ORIGINAL, b=contents).ratio()
        result[file_] = ratio

    for file_, ratio in result.items():
        if 1 > ratio > 0.6:
            print(file_)


if __name__ == "__main__":
    main()
