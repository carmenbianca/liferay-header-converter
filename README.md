# Liferay Header Converter

This is a quickly written tool intended for the replacement of Liferay's
headers. It is written as part of my educational internship at Liferay. The
sending institution is NHL Stenden, Leeuwarden.

In short, these headers:

```
/**
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
 */
```

need to turn into:

```
/**
 * SPDX-FileCopyrightText: © {year} Liferay, Inc. <https://liferay.com>
 * SPDX-License-Identifier: LGPL-2.1-or-later
 */
```

## Usage

```
cd path/to/liferay-portal
python path/to/liferay-header-converter/generate_dates.py
python path/to/liferay-header-converter/replace.py
```

That's the basic usage. All the other stuff is code to assist me in the process.
