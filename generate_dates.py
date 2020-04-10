# SPDX-License-Identifier: LGPL-2.0-or-later
#
# SPDX-FileCopyrightText: © 2020 Liferay, Inc. <https://liferay.com>

import json
from multiprocessing import Pool
from typing import NamedTuple
import datetime

from liferay_header_converter import replace_header, all_files, get_latest_date


class DateResult(NamedTuple):
    file_: str
    date: datetime.datetime


def get_latest_date_wrapper(file_):
    result = DateResult(file_, get_latest_date(file_))
    print(file_)
    return result


def main():
    dates = dict()
    pool = Pool(processes=16)

    results = pool.map(get_latest_date_wrapper, all_files())

    pool.close()
    pool.join()

    for result in results:
        dates[result.file_] = result.date.isoformat()

    with open("dates.json", "w") as fp:
        json.dump(dates, fp)


if __name__ == "__main__":
    main()
