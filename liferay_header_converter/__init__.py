# SPDX-License-Identifier: LGPL-2.1-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

from difflib import SequenceMatcher
import os
import glob
import subprocess
import datetime

ORIGINAL = """/**
 * Copyright (c) 2000-present Liferay, Inc. All rights reserved.
 *
 * This library is free software; you can redistribute it and/or modify it under
 * the terms of the GNU Lesser General Public License as published by the Free
 * Software Foundation; either version 2.1 of the License, or (at your option)
 * any later version.
 *
 * This library is distributed in the hope that it will be useful, but WITHOUT
 * ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
 * FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more
 * details.
 */"""
LEN_ORIGINAL = len(ORIGINAL)

# original, replacement
HEADERS = {
    ORIGINAL: """/*
 * SPDX-FileCopyrightText: © {year} Liferay, Inc. <https://liferay.com>
 * SPDX-License-Identifier: LGPL-2.1-or-later
 */""",
    """/**
 * Copyright (c) 2000-present Liferay, Inc. All rights reserved.
 *
 * This file is part of Liferay Social Office. Liferay Social Office is free
 * software: you can redistribute it and/or modify it under the terms of the GNU
 * Affero General Public License as published by the Free Software Foundation,
 * either version 3 of the License, or (at your option) any later version.
 *
 * Liferay Social Office is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
 * FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License
 * for more details.
 *
 * You should have received a copy of the GNU General Public License along with
 * Liferay Social Office. If not, see http://www.gnu.org/licenses/agpl-3.0.html.
 */""": """/*
 * SPDX-FileCopyrightText: © {year} Liferay, Inc. <https://liferay.com>
 * SPDX-License-Identifier: AGPL-3.0-or-later
 */""",
}

DIR_PATH = os.path.dirname(os.path.realpath(__file__))
ROOT_PATH = os.path.dirname(DIR_PATH)


def all_files():
    files = glob.glob("**/*", recursive=True)
    for file_ in files:
        if (
            os.path.isfile(file_)
            and not file_.startswith("modules/third-party")
            and not file_.endswith("copyright.txt")
            and not file_.endswith("copyright.js")
        ):
            yield file_


def get_latest_date(file_):
    mtime = os.path.getmtime(file_)
    return datetime.datetime.fromtimestamp(mtime)


def replace_header(file_):
    with open(file_) as fp:
        contents = fp.read()

    for original, replacement in HEADERS.items():
        if original in contents:
            contents = contents.replace(
                original, replacement.format(year=get_latest_date(file_).year)
            )
            break
    else:
        raise Exception("No header replaced")

    with open(file_, "w") as fp:
        fp.write(contents)
