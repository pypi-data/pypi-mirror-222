#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Copyright (C) 2022-2023 ByQuant.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from __future__ import (absolute_import, division, print_function,unicode_literals)
import talib

# 参数说明：talib.BBANDS(close, timeperiod, matype)
# close:收盘价；timeperiod:周期；matype:平均方法(bolling线的middle线 = MA，用于设定哪种类型的MA)
# MA_Type: 0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA, 8=T3 (Default=SMA)

def BBANDS(data,period,matype = talib.MA_Type.EMA):
    upper, middle, lower = talib.BBANDS(data.close, timeperiod=period,matype = matype)
    return upper, middle, lower