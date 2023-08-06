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

class Backtest():

    def __init__(self,data,strategy,out='plotly',style='candle'):
        self.data = bt.feeds.PandasData(dataname=data, datetime='datetime')
        self.strategy = strategy
        self.style = style
        self.out = out

    def byrun(self):
        cerebro = bt.Cerebro()
        cerebro.addstrategy(self.strategy)
        cerebro.addanalyzer(bt.analyzers.PyFolio, _name='_Pyfolio')
        cerebro.adddata(self.data)
        results = cerebro.run()

        if 'pyfolio' in self.out:
            import pyfolio as pf
            pyfoliozer = results[0].analyzers.getbyname('_Pyfolio')
            returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()
            pf.create_full_tear_sheet(returns, positions, transactions)

        elif 'quantstats' in self.out: 
            import quantstats as qs
            pyfoliozer = results[0].analyzers.getbyname('_Pyfolio')
            returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()
            returns.index = returns.index.tz_convert(None)
            qs.reports.full(returns, benchmark=returns, mode='full')
            
        elif 'plotly' in self.out:
            cerebro.plot(style = self.style)
            
        
        