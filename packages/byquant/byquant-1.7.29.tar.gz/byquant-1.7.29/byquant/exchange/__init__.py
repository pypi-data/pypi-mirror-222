#!/usr/bin/env python
# -*- coding: utf-8; py-indent-offset:4 -*-
###############################################################################
#
# Author : Trabi
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

from .okx import okx                                              
from .ace import ace                                              
from .alpaca import alpaca                                        
from .ascendex import ascendex                                    
from .bequant import bequant                                      
from .bigone import bigone                                        
from .binance import binance                                      
from .binancecoinm import binancecoinm                            
from .binanceus import binanceus                                  
from .binanceusdm import binanceusdm                              
from .bit2c import bit2c                                          
from .bitbank import bitbank                                      
from .bitbay import bitbay                                        
from .bitbns import bitbns                                        
from .bitcoincom import bitcoincom                                
from .bitfinex import bitfinex                                    
from .bitfinex2 import bitfinex2                                  
from .bitflyer import bitflyer                                    
from .bitforex import bitforex                                    
from .bitget import bitget                                        
from .bithumb import bithumb                                      
from .bitmart import bitmart                                      
from .bitmex import bitmex                                        
from .bitopro import bitopro                                      
from .bitpanda import bitpanda                                    
from .bitrue import bitrue                                        
from .bitso import bitso                                          
from .bitstamp import bitstamp                                    
from .bitstamp1 import bitstamp1                                  
from .bittrex import bittrex                                      
from .bitvavo import bitvavo                                      
from .bkex import bkex                                            
from .bl3p import bl3p                                            
from .blockchaincom import blockchaincom                          
from .btcalpha import btcalpha                                    
from .btcbox import btcbox                                        
#from .btcex import btcex                                          
from .btcmarkets import btcmarkets                                
from .btctradeua import btctradeua                                
from .btcturk import btcturk                                      
from .bybit import bybit                                          
from .cex import cex                                              
from .coinbase import coinbase                                    
from .coinbaseprime import coinbaseprime                          
from .coinbasepro import coinbasepro                              
from .coincheck import coincheck                                  
from .coinex import coinex                                        
from .coinfalcon import coinfalcon                                
from .coinmate import coinmate                                    
from .coinone import coinone                                      
from .coinsph import coinsph                                      
from .coinspot import coinspot                                    
from .cryptocom import cryptocom                                  
from .currencycom import currencycom                              
from .delta import delta                                          
from .deribit import deribit                                      
from .digifinex import digifinex                                  
from .exmo import exmo                                            
from .fmfwio import fmfwio                                        
from .gate import gate                                            
from .gateio import gateio                                        
from .gemini import gemini                                        
from .hitbtc import hitbtc                                        
from .hitbtc3 import hitbtc3                                      
from .hollaex import hollaex                                      
from .huobi import huobi                                          
from .huobijp import huobijp                                      
from .huobipro import huobipro                                    
from .idex import idex                                            
from .independentreserve import independentreserve                
from .indodax import indodax                                      
from .kraken import kraken                                        
from .krakenfutures import krakenfutures                          
from .kucoin import kucoin                                        
from .kucoinfutures import kucoinfutures                          
from .kuna import kuna                                            
from .latoken import latoken                                      
from .lbank import lbank                                          
from .lbank2 import lbank2                                        
from .luno import luno                                            
from .lykke import lykke                                          
from .mercado import mercado                                      
from .mexc import mexc                                            
from .mexc3 import mexc3                                          
from .ndax import ndax                                            
from .novadax import novadax                                      
from .oceanex import oceanex                                      
from .okcoin import okcoin                                        
from .okex import okex                                            
from .okex5 import okex5                                          
#from .okx import okx                                                Uakeey
from .paymium import paymium                                      
from .phemex import phemex                                        
from .poloniex import poloniex                                    
from .poloniexfutures import poloniexfutures                      
from .probit import probit                                        
#from .stex import stex                                            
from .tidex import tidex                                          
from .timex import timex                                          
from .tokocrypto import tokocrypto                                
from .upbit import upbit                                          
from .wavesexchange import wavesexchange                          
from .wazirx import wazirx                                        
from .whitebit import whitebit                                    
from .woo import woo                                              
#from .xt import xt                                                
from .yobit import yobit                                          
from .zaif import zaif                                            
from .zonda import zonda                                          

from .buda import buda                                            
from .flowbtc import flowbtc                                      
from .itbit import itbit                                          
from .ripio import ripio                                          
from .zb import zb                                                


def get(exName):
    #print(exName)
    exName=exName.lower()
    if exName == 'ace': result = ace()
    elif exName == 'alpaca': result = alpaca()
    elif exName == 'ascendex': result = ascendex()
    elif exName == 'bequant': result = bequant()
    elif exName == 'bigone': result = bigone()
    elif exName == 'binance': result = binance()
    elif exName == 'binancecoinm': result = binancecoinm()
    elif exName == 'binanceus': result = binanceus()
    elif exName == 'binanceusdm': result = binanceusdm()
    elif exName == 'bit2c': result = bit2c()
    elif exName == 'bitbank': result = bitbank()
    elif exName == 'bitbay': result = bitbay()
    elif exName == 'bitbns': result = bitbns()
    elif exName == 'bitcoincom': result = bitcoincom()
    elif exName == 'bitfinex': result = bitfinex()
    elif exName == 'bitfinex2': result = bitfinex2()
    elif exName == 'bitflyer': result = bitflyer()
    elif exName == 'bitforex': result = bitforex()
    elif exName == 'bitget': result = bitget()
    elif exName == 'bithumb': result = bithumb()
    elif exName == 'bitmart': result = bitmart()
    elif exName == 'bitmex': result = bitmex()
    elif exName == 'bitopro': result = bitopro()
    elif exName == 'bitpanda': result = bitpanda()
    elif exName == 'bitrue': result = bitrue()
    elif exName == 'bitso': result = bitso()
    elif exName == 'bitstamp': result = bitstamp()
    elif exName == 'bitstamp1': result = bitstamp1()
    elif exName == 'bittrex': result = bittrex()
    elif exName == 'bitvavo': result = bitvavo()
    elif exName == 'bkex': result = bkex()
    elif exName == 'bl3p': result = bl3p()
    elif exName == 'blockchaincom': result = blockchaincom()
    elif exName == 'btcalpha': result = btcalpha()
    elif exName == 'btcbox': result = btcbox()
    #elif exName == 'btcex': result = btcex()
    elif exName == 'btcmarkets': result = btcmarkets()
    elif exName == 'btctradeua': result = btctradeua()
    elif exName == 'btcturk': result = btcturk()
    elif exName == 'buda': result = buda()
    elif exName == 'bybit': result = bybit()
    elif exName == 'cex': result = cex()
    elif exName == 'coinbase': result = coinbase()
    elif exName == 'coinbaseprime': result = coinbaseprime()
    elif exName == 'coinbasepro': result = coinbasepro()
    elif exName == 'coincheck': result = coincheck()
    elif exName == 'coinex': result = coinex()
    elif exName == 'coinfalcon': result = coinfalcon()
    elif exName == 'coinmate': result = coinmate()
    elif exName == 'coinone': result = coinone()
    elif exName == 'coinspot': result = coinspot()
    elif exName == 'cryptocom': result = cryptocom()
    elif exName == 'currencycom': result = currencycom()
    elif exName == 'delta': result = delta()
    elif exName == 'deribit': result = deribit()
    elif exName == 'digifinex': result = digifinex()
    elif exName == 'exmo': result = exmo()
    elif exName == 'flowbtc': result = flowbtc()
    elif exName == 'fmfwio': result = fmfwio()
    elif exName == 'gate': result = gate()
    elif exName == 'gateio': result = gate() #gateio
    elif exName == 'gemini': result = gemini()
    elif exName == 'hitbtc': result = hitbtc()
    elif exName == 'hitbtc3': result = hitbtc3()
    elif exName == 'hollaex': result = hollaex()
    elif exName == 'huobi': result = huobi()
    elif exName == 'huobijp': result = huobijp()
    elif exName == 'huobipro': result = huobipro()
    elif exName == 'idex': result = idex()
    elif exName == 'independentreserve': result = independentreserve()
    elif exName == 'indodax': result = indodax()
    elif exName == 'itbit': result = itbit()
    elif exName == 'kraken': result = kraken()
    elif exName == 'krakenfutures': result = krakenfutures()
    elif exName == 'kucoin': result = kucoin()
    elif exName == 'kucoinfutures': result = kucoinfutures()
    elif exName == 'kuna': result = kuna()
    elif exName == 'latoken': result = latoken()
    elif exName == 'lbank': result = lbank()
    elif exName == 'lbank2': result = lbank2()
    elif exName == 'luno': result = luno()
    elif exName == 'lykke': result = lykke()
    elif exName == 'mercado': result = mercado()
    elif exName == 'mexc': result = mexc()
    elif exName == 'mexc3': result = mexc3()
    elif exName == 'ndax': result = ndax()
    elif exName == 'novadax': result = novadax()
    elif exName == 'oceanex': result = oceanex()
    elif exName == 'okcoin': result = okcoin()
    elif exName == 'okex': result = okex()
    elif exName == 'okex5': result = okex5()
    elif exName == 'okx': result = okx()
    elif exName == 'paymium': result = paymium()
    elif exName == 'phemex': result = phemex()
    elif exName == 'poloniex': result = poloniex()
    elif exName == 'poloniexfutures': result = poloniexfutures()
    elif exName == 'probit': result = probit()
    elif exName == 'ripio': result = ripio()
#    elif exName == 'stex': result = stex()
    elif exName == 'tidex': result = tidex()
    elif exName == 'timex': result = timex()
    elif exName == 'tokocrypto': result = tokocrypto()
    elif exName == 'upbit': result = upbit()
    elif exName == 'wavesexchange': result = wavesexchange()
    elif exName == 'wazirx': result = wazirx()
    elif exName == 'whitebit': result = whitebit()
    elif exName == 'woo': result = woo()
    elif exName == 'yobit': result = yobit()
    elif exName == 'zaif': result = zaif()
    elif exName == 'zb': result = zb()
    elif exName == 'zonda': result = zonda()
    else:
        print('No %s' % (exName))
    return result
