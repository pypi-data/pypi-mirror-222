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

import backtrader as bt

def MACD(data, period_me1,period_me2,period_signal):
    return bt.indicators.MACD(
            data,
            period_me1=period_me1,
            period_me2=period_me2,
            period_signal=period_signal,
        )
    
class MACD_Stop(bt.Indicator):
    lines = ('byindicator',)
    params = (
        ('period_me1', 12),
        ('period_me2', 26),
        ('period_signal', 9)
    )
    def __init__(self):
        self._indicator_data = bt.indicators.MACD(
            self.data[0],
            period_me1=self.p.period_me1,
            period_me2=self.p.period_me2,
            period_signal=self.p.period_signal,
        )

    def next(self):
        self.lines.byindicator['macd'][0] = self._indicator_data['macd'][0]
        self.lines.byindicator['signal'][0] = self._indicator_data['signal'][0]