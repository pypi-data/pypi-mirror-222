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

    def __init__(self,data,strategy,out='',style='candle'):
        data.reset_index(drop=False, inplace=True)
        self.data = bt.feeds.PandasData(dataname=data, datetime='datetime')
        self.strategy = strategy
        self.style = style
        self.out = out

    def byrun(self):
        cerebro = bt.Cerebro()
        cerebro.addstrategy(self.strategy)
        
        cerebro.addanalyzer(bt.analyzers.PyFolio, _name='_Pyfolio')
        cerebro.addanalyzer(bt.analyzers.SharpeRatio, _name='_SharpeRatio')  # 夏普比率
        cerebro.addanalyzer(bt.analyzers.Returns, _name='_Returns')  # 用对数法计算总、平均、复合、年化收益率
        cerebro.addanalyzer(bt.analyzers.DrawDown, _name='_DrawDown')  # 回撤
            
            
        
        cerebro.broker.setcash(1000000.0)
        cerebro.adddata(self.data)
        results = cerebro.run()

        if 'plot' == self.out or 'a' == self.out:
            cerebro.plot(style = self.style)
            
        elif 'plotly' == self.out or 'c' == self.out:
            # 获取策略的收益率
            import pandas as pd
            import plotly.graph_objects as go
            returns = results[0].analyzers._Returns.get_analysis()
            # 创建收益曲线图
            returns_df = pd.DataFrame.from_dict(returns, orient='index', columns=['Returns'])
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=returns_df.index, y=returns_df['Returns'], mode='lines', name='Returns'))

            # 设置图表布局
            fig.update_layout(title='Strategy Returns',
                              xaxis_title='Time',
                              yaxis_title='Returns')

            # 显示图表
            fig.show()
            
        elif 'pyfolio' == self.out or 'p' == self.out:
            import pyfolio as pf
            pyfoliozer = results[0].analyzers.getbyname('_Pyfolio')
            returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()
            pf.create_full_tear_sheet(returns, positions, transactions)

        elif 'quantstats' == self.out or 'q' == self.out: 
            import quantstats as qs
            pyfoliozer = results[0].analyzers.getbyname('_Pyfolio')
            returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()
            returns.index = returns.index.tz_convert(None)
            qs.reports.full(returns, benchmark=returns, mode='full')
            
        
            
        elif 'bokeh' == self.out or 'b' == self.out:
            from backtrader_plotting import Bokeh
            from backtrader_plotting.schemes import Tradimo,Blackly
            b = Bokeh(
                title='symbol',
                tabs='single',  # single 和 multi
                plot=True,  # 关闭K线
                style='line',  # style='line'
                plot_mode='single',
                scheme=Tradimo(),
                # scheme=Blackly(),
                output_mode='show',  # output_mode “show”,“save”,"memory"
                filename='filepath',
                show_headline=False
            )
            cerebro.plot(b)
            
        elif 'seaborn' == self.out or 's' == self.out:
            import seaborn as sns
            pyfoliozer = results[0].analyzers.getbyname('_Pyfolio')
            returns, positions, transactions, gross_lev = pyfoliozer.get_pf_items()
            sns.lineplot(returns)
            #sns.histplot(positions)
            #sns.histplot(transactions)

        else:
            returns = results[0].analyzers._Returns.get_analysis()
            sharpe_ratio = results[0].analyzers._SharpeRatio.get_analysis()
            draw_down = results[0].analyzers._DrawDown.get_analysis()
            #print('Value: %.2f' % cerebro.broker.getvalue())
            print('Returns:%s' % returns)
            print('Sharpe Ratio: %s' % sharpe_ratio)
            print('Draw Down: %s' % draw_down)
 