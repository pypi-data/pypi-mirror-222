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

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
import talib

class MACD():
    def __init__(self, data, fastperiod, slowperiod, signalperiod):
        self.data = data
        self.fastperiod = fastperiod
        self.slowperiod = slowperiod
        self.signalperiod = signalperiod
        self.result = self._macd()

    def _macd(self):
        macd, signal, hist = talib.MACD(self.data.close, fastperiod=self.fastperiod, slowperiod=self.slowperiod, signalperiod=self.signalperiod)
        return hist
    
    def __str__(self):
        return str(self.result)