#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Copyright (C) 2019 tribe29 GmbH - License: GNU General Public License v2
# This file is part of Checkmk (https://checkmk.com). It is subject to the terms and
# conditions defined in the file COPYING, which is part of this source code package.
from cmk.base.plugins.agent_based.v0 import (  # type: ignore[import]
    all_of, contains, exists,
)

DETECT_RICOH = all_of(
    contains(".1.3.6.1.2.1.1.2.0", ".1.3.6.1.4.1.367.1.1"),
    exists(".1.3.6.1.4.1.367.3.2.1.2.19.5.1.5.1"),
)
