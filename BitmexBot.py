

# Program supports BNB, BTC, and ETH markets only. No USDT.

from binance.enums import *
import pandas as pd
import time
import subprocess
import sys
import numpy as np
import os
import bitmex
from bitmex_historical import Bitmex
from datetime import datetime
import warnings
warnings.filterwarnings('ignore')

client = bitmex.bitmex(test=False, api_key="YOUR_KEY_HERE",
                       api_secret="YOUR_SECRET_HERE")

short_window = 2
long_window = 60
longer_window=10

#quantity to send via limit order
quantity = 5


list = client.Position.Position_get().result()




holder = 0




def limitOrder(holder,quantity):
    # binance.order("BNBBTC", binance.BUY, 1000, 0.000001, test=True)
    if holder == 0:
        ret_usd = client.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=1).result()

        print(ret_usd[0][1]['price']-1.0)
        position1 = client.Order.Order_new(symbol='XBTUSD', side='Buy', orderQty=quantity, ordType='Limit', price=ret_usd[0][1]['price']-1.5,text='Limit Order').result()
        time.sleep(20)
        list = client.Position.Position_get().result()
        if list[0][0].get('openOrderBuyQty')>0 & list[0][0].get('currentQty')==0:
            print('NOT FILLED CANCELLING ORDER')
            result1 = client.Order.Order_cancel(orderID=position1[0].get('orderID'), text='Submitted via API.').result()
            return
            #positionQuantity = client.Position.Position_get().result()
        elif list[0][0].get('currentQty')!=quantity:
            print("Partfial fill! Current Position Size:",list[0][0].get('currentQty') )
            result1 = client.Order.Order_cancel(orderID=position1[0].get('orderID'), text='Submitted via API.').result()
            quantity = list[0][0].get('currentQty')
            #if positionQuantity[0][0]['currentQty']!=quantity:
             #   print("TEST")



    checkTimer2 = int(datetime.now().strftime("%S"))
    while checkTimer2 < 21 or checkTimer2 > 29:
        #print("Boi2: Waiting till 20 secs...")
        #print(checkTimer2)
        time.sleep(2)
        checkTimer2 = int(datetime.now().strftime("%S"))
    #data = Bitmex().get_historical_data(tick='1m')
    data2 = Bitmex().get_historical_data(tick='1m')
    signals2 = pd.DataFrame(data2)
    signals2['signal'] = 0.0
    signals2['fee'] = 0.0
    signals2['MavgCross'] = 0.0
    signals2['number2'] = 0.0
    signals2['ShiftOne'] = 0.0
    signals2['ShiftTwo'] = 0.0
    signals2['number5'] = 0.0
    signals2['number6'] = 0.0
    signals2['number7'] = 0.0
    signals2['number8'] = 0.0
    signals2['number9'] = 0.0
    signals2['number10'] = 0.0
    signals2['number11'] = 0.0
    signals2['number12'] = 0.0
    signals2['number13'] = 0.0
    signals2['number14'] = 0.0
    signals2['number15'] = 0.0
    signals2['number16'] = 0.0
    signals2['number17'] = 0.0
    signals2['number18'] = 0.0
    signals2['number19'] = 0.0
    signals2['number20'] = 0.0
    signals2['number21'] = 0.0
    signals2['number22'] = 0.0
    signals2['number23'] = 0.0
    signals2['number24'] = 0.0
    signals2['number25'] = 0.0
    signals2['number26'] = 0.0
    signals2['number27'] = 0.0
    signals2['number28'] = 0.0
    signals2['number29'] = 0.0
    signals2['number30'] = 0.0
    signals2['number31'] = 0.0
    signals2['number32'] = 0.0
    signals2['number33'] = 0.0
    signals2['number34'] = 0.0
    signals2['number35'] = 0.0
    signals2['number36'] = 0.0
    signals2['number37'] = 0.0
    signals2['number38'] = 0.0
    signals2['number39'] = 0.0
    signals2['number40'] = 0.0
    signals2['number41'] = 0.0
    signals2['number42'] = 0.0
    signals2['number43'] = 0.0
    signals2['number44'] = 0.0
    signals2['number45'] = 0.0
    signals2['number46'] = 0.0
    signals2['number47'] = 0.0

    signals2['score'] = 0.0



    # Create short simple moving average over the short window
    signals2['short_mavg'] = signals2['volume'].rolling(window=short_window, min_periods=1, center=False).std()
    signals2['long_mavg'] = signals2['volume'].rolling(window=long_window, min_periods=1, center=False).std()
    signals2['longer_mavg'] = signals2['volume'].rolling(window=longer_window, min_periods=1, center=False).std()


    signals2['MavgCross'][0:] = np.where(signals2['close'] > signals2['open'].shift(1),-0.1,0)#& (signals2['close'] > signals2['high'].shift(1))  signals2['short_mavg'] > signals2['short_mavg'].shift(1) * .999
    signals2['number2'][0:] = np.where(signals2['open'] < signals2['high'].shift(1),0.2, 0)
    signals2['ShiftOne'][0:] = np.where((signals2['close'] > signals2['close'].shift(2)) & (signals2['close'] > signals2['close'].shift(1)), -0.1, 0)
    signals2['ShiftTwo'][0:] = np.where((signals2['close'] > signals2['close'].shift(1)) & (signals2['high'].shift(1) > signals2['close'].shift(3)), -0.1, 0)
    signals2['number5'][0:] = np.where(signals2['high'] * .999 > signals2['close'], 0.3, 0)
    signals2['number6'][0:] = np.where((signals2['low'] < signals2['close'].shift(1)) & (signals2['high'] > signals2['close'].shift(1)) & (signals2['low'].shift(1) > signals2['close'].shift(3)), -0.1, 0)
    signals2['number7'][0:] = np.where((signals2['low'] < signals2['close'].shift(1)) & (signals2['high'] > signals2['close'].shift(1)) & (signals2['low'] < signals2['close'].shift(3)), 0.2, 0)
    signals2['number8'][0:] = np.where(signals2['short_mavg'] > signals2['longer_mavg'], 0.2, 0)
    signals2['number9'][0:] = np.where((signals2['low'] < signals2['close'].shift(2)) & (signals2['high'] > signals2['close'].shift(1)) & (signals2['low'] < signals2['close'].shift(1)), 0.2, 0)
    signals2['number10'][0:] = np.where(signals2['open'] < signals2['open'].shift(1), 0.3, 0)
    signals2['number11'][0:] = np.where(signals2['high'] > signals2['close'].shift(1), -0.1, 0)
    signals2['number12'][0:] = np.where(signals2['open'] > signals2['low'].shift(1), 0.1, 0)
    signals2['number13'][0:] = np.where(signals2['close'] > signals2['high'].shift(1), -0.1, 0)
    signals2['number14'][0:] = np.where(signals2['low'] > signals2['high'].shift(2), -0.1, 0)
    signals2['number15'][0:] = np.where(signals2['low'] > signals2['open'].shift(1), -0.1, 0)
    signals2['number16'][0:] = np.where(signals2['short_mavg'] > signals2['short_mavg'].shift(1)*1.5, 0.2, 0)
    signals2['number17'][0:] = np.where(signals2['volume'] > signals2['volume'].shift(1), -0.1, 0)
    signals2['number18'][0:] = np.where((signals2['close'] > signals2['open'].shift(1)) & (signals2['close'] > signals2['high'].shift(3)), -.1, 0)
    signals2['number19'][0:] = np.where((signals2['close'] > signals2['low'].shift(2)) & (signals2['open'] < signals2['close'].shift(2)), .2, 0)
    signals2['number20'][0:] = np.where((signals2['low'] > signals2['close'].shift(2)) & (signals2['open'] > signals2['high'].shift(3)), -.1, 0)
    signals2['number21'][0:] = np.where((signals2['open'] > signals2['close'].shift(2)) & (signals2['open'] > signals2['high'].shift(3)), -.1, 0)
    signals2['number22'][0:] = np.where((signals2['close'] > signals2['close'].shift(2)) & (signals2['open'] > signals2['open'].shift(3)), -.1, 0)
    signals2['number23'][0:] = np.where((signals2['open'] > signals2['close'].shift(2)) & (signals2['open'] > signals2['open'].shift(4)), -.1, 0)
    signals2['number24'][0:] = np.where((signals2['open'] > signals2['high'].shift(3)) & (signals2['open'] > signals2['open'].shift(2)), -.1, 0)
    signals2['number25'][0:] = np.where((signals2['close'] > signals2['high'].shift(2)) & (signals2['close'] > signals2['open'].shift(3)), -.1, 0)
    signals2['number26'][0:] = np.where((signals2['open'] > signals2['high'].shift(3)) & (signals2['close'] > signals2['open'].shift(5)), -.1, 0)
    signals2['number27'][0:] = np.where((signals2['open'] > signals2['low'].shift(2)) & (signals2['low'] > signals2['open'].shift(2)), -.1, 0)
    signals2['number28'][0:] = np.where((signals2['high'] < signals2['high'].shift(2)) & (signals2['low'] < signals2['close'].shift(3)), .2, 0)
    signals2['number29'][0:] = np.where((signals2['open'] > signals2['low'].shift(1)) & (signals2['low'] < signals2['open'].shift(2)), .2, 0)
    signals2['number30'][0:] = np.where(signals2['close'] < signals2['close'].shift(1), .1, 0)
    signals2['number31'][0:] = np.where(signals2['high'] < signals2['high'].shift(1), .2, 0)
    signals2['number32'][0:] = np.where(signals2['high'] < signals2['open'].shift(1), .2, 0)
    signals2['number33'][0:] = np.where(signals2['close'] < signals2['open'].shift(1), .2, 0)
    signals2['number34'][0:] = np.where(signals2['close'] < signals2['high'].shift(1), .1, 0)
    signals2['number35'][0:] = np.where(signals2['open'] < signals2['high'].shift(2), .2, 0)
    signals2['number36'][0:] = np.where(signals2['high'] < signals2['open'].shift(2), .2, 0)
    signals2['number37'][0:] = np.where(signals2['close'] < signals2['open'].shift(2), .2, 0)
    signals2['number38'][0:] = np.where(signals2['close'] < signals2['open'].shift(3), .2, 0)
    signals2['number39'][0:] = np.where(signals2['high'] < signals2['open'].shift(3), .2, 0)
    signals2['number40'][0:] = np.where(signals2['open'] < signals2['high'].shift(3), .2, 0)
    signals2['number41'][0:] = np.where(signals2['open'] < signals2['high'].shift(4), .2, 0)
    signals2['number42'][0:] = np.where(signals2['high'] < signals2['open'].shift(4), .2, 0)
    signals2['number43'][0:] = np.where(signals2['close'] < signals2['open'].shift(4), .2, 0)
    signals2['number44'][0:] = np.where(signals2['open'] > signals2['high'].shift(2), -.1, 0)
    signals2['number45'][0:] = np.where(signals2['volume'] > signals2['volume'].shift(1), .2, 0)
    signals2['number46'][0:] = np.where(signals2['volume'] > signals2['volume'].shift(2), .2, 0)
    signals2['number47'][0:] = np.where(signals2['volume'] > signals2['volume'].shift(3), .1, 0)


    signals2['score'][0:] = signals2['MavgCross'] + signals2['number2'] + signals2['ShiftOne'] + signals2['ShiftTwo'] + signals2['number5'] + signals2['number6']   \
                           + signals2['number7'] + signals2['number8'] +  signals2['number9'] + signals2['number10'] + signals2['number11'] + signals2['number12'] \
                           + signals2['number13'] + signals2['number14'] + signals2['number15'] + signals2['number16'] + signals2['number17'] + signals2['number18'] \
                            + signals2['number19'] + signals2['number20'] + signals2['number21'] + signals2['number22'] + signals2['number23'] + signals2['number24'] \
                           + signals2['number25'] + signals2['number26'] + signals2['number27'] + signals2['number28'] + signals2['number29'] + signals2['number30'] \
                            + signals2['number31'] + signals2['number32'] + signals2['number33'] + signals2['number34'] + signals2['number35'] + signals2['number36'] \
                           + signals2['number37'] + signals2['number38'] + signals2['number39'] + signals2['number40'] + signals2['number41'] + signals2['number42']  \
                            + signals2['number43'] + signals2['number44'] + signals2['number45'] + signals2['number46'] + signals2['number47']

    signals2['signal'][0:] = np.where((signals2['score'] > .79) & (signals2['score'].shift(1) * .10 < signals2['score']) & (
                signals2['score'].shift(2) * .10 < signals2['score'].shift(1)), 1.0, 0)

    # signals2['signal'][0:] = np.where(signals['score'] > .39, 1.0, 0)
    print("Current Score:",signals2['score'].iloc[20])
    #print(round(signals2['score'],3))
    list2 = client.Position.Position_get().result()
    if ((signals2['score'].iloc[20] > .79) & (signals['score'].iloc[19]*.10 <signals['score'].iloc[20]) & (signals['score'].iloc[18]*.10 <signals['score'].iloc[19])):
        time.sleep(10)
        del signals2
        limitOrder(1,quantity)
    elif holder == 1 and list2[0][0].get('currentQty')>0:
        print("SELLING...")
        ret_usd = client.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=1).result()
        # print(ret_usd[0][0]['price'])  # Offer
        print(ret_usd[0][0]['price'] +1.0)
        #print(.5*round(ret_usd[0][0]['price'] * 1.0002/.5))
        position3 = client.Order.Order_new(symbol='XBTUSD', side='Sell', orderQty=quantity, ordType='Limit',price=ret_usd[0][0]['price'] +1.0, text='Limit Order').result()
        #position1 = client.Order.Order_new(symbol='XBTUSD', side='SELL', orderQty=1, ordType='Limit', price='5600',text='Limit Order').result()
        print("TESTSELL", position3)
        time.sleep(15)


        list = client.Position.Position_get().result()
        while list[0][0]['currentQty'] > 0:
            result2 = client.Order.Order_cancel(orderID=position3[0].get('orderID'), text='Submitted via API.').result()
            position3 = client.Order.Order_new(symbol='XBTUSD', side='Sell', orderQty=quantity, ordType='Limit',price=ret_usd[0][0]['price']+1.0,text='Limit Order').result()
            time.sleep(15)
            print(list[0][0].get('openOrderSellQty'))
            print("TRY TO SELL")
            list = client.Position.Position_get().result()
            ret_usd = client.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=1).result()
            print (list[0][0].get('openOrderSellQty'))

    elif ((signals2['score'].iloc[20] < .79) & (signals['score'].iloc[19]*.10 <signals['score'].iloc[20]) & (signals['score'].iloc[18]*.10 <signals['score'].iloc[19]) & (list2[0][0].get('currentQty')>0)):
        print("SELLING...")
        ret_usd = client.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=1).result()
        print(ret_usd[0][0]['price']+1.0)
        # print(ret_usd[0][0]['price'])  # Offer
        position4 = client.Order.Order_new(symbol='XBTUSD', side='Sell', orderQty=quantity, ordType='Limit',price=ret_usd[0][0]['price'] +1.0, text='Limit Order').result()
        print("TESTSELL", position4)
        time.sleep(15)


        list = client.Position.Position_get().result()
        while list[0][0]['currentQty'] > 0:
            result3 = client.Order.Order_cancel(orderID=position4[0].get('orderID'), text='Submitted via API.').result()
            position4 = client.Order.Order_new(symbol='XBTUSD', side='Sell', orderQty=quantity, ordType='Limit',
                                               price=ret_usd[0][0]['price']+1.0,
                                               text='Limit Order').result()
            time.sleep(15)
            list = client.Position.Position_get().result()
            ret_usd = client.OrderBook.OrderBook_getL2(symbol='XBTUSD', depth=1).result()






# print(client.get_historical_klines("ETHBTC", Client.KLINE_INTERVAL_1MINUTE, "1 min ago"))

checkTimer = int(datetime.now().strftime("%S"))
while checkTimer<21 or checkTimer>30:
    #print("Boi1: Waiting till 20 secs...")
    #print(boi)
    time.sleep(2)
    checkTimer = int(datetime.now().strftime("%S"))






data = Bitmex().get_historical_data(tick='1m')
#print(data)
signals = pd.DataFrame(data)
#signals.to_csv('dater14.csv', encoding='utf-8', index=False)
#print (signals.iloc[20])


# print(signals[2].iloc[0])
# signals[2].to_csv('dater000.csv', encoding='utf-8', index=False)
# print(df)


signals['signal'] = 0.0
signals['fee'] = 0.0
signals['MavgCross'] = 0.0
signals['number2'] = 0.0
signals['ShiftOne'] = 0.0
signals['ShiftTwo'] = 0.0
signals['number5'] = 0.0
signals['number6'] = 0.0
signals['number7'] = 0.0
signals['number8'] = 0.0
signals['number9'] = 0.0
signals['number10'] = 0.0
signals['number11'] = 0.0
signals['number12'] = 0.0
signals['number13'] = 0.0
signals['number14'] = 0.0
signals['number15'] = 0.0
signals['number16'] = 0.0
signals['number17'] = 0.0
signals['number18'] = 0.0
signals['number19'] = 0.0
signals['number20'] = 0.0
signals['number21'] = 0.0
signals['number22'] = 0.0
signals['number23'] = 0.0
signals['number24'] = 0.0
signals['number25'] = 0.0
signals['number26'] = 0.0
signals['number27'] = 0.0
signals['number28'] = 0.0
signals['number29'] = 0.0
signals['number30'] = 0.0
signals['number31'] = 0.0
signals['number32'] = 0.0
signals['number33'] = 0.0
signals['number34'] = 0.0
signals['number35'] = 0.0
signals['number36'] = 0.0
signals['number37'] = 0.0
signals['number38'] = 0.0
signals['number39'] = 0.0
signals['number40'] = 0.0
signals['number41'] = 0.0
signals['number42'] = 0.0
signals['number43'] = 0.0
signals['number44'] = 0.0
signals['number45'] = 0.0
signals['number46'] = 0.0
signals['number47'] = 0.0
signals['score'] = 0.0

# signals[2] = 0.0
# signals[3] = 0.0
# signals[4] = 0.0
# signals[5] = 0.0
# signals[8] = 0.0

# Create short simple moving average over the short window
signals['short_mavg'] = signals['volume'].rolling(window=short_window, min_periods=1, center=False).std()
signals['long_mavg'] = signals['volume'].rolling(window=long_window, min_periods=1, center=False).std()
signals['longer_mavg'] = signals['volume'].rolling(window=longer_window, min_periods=1, center=False).std()
signals['long_mavg'] = signals['close'].shift(3)
signals['long_close'] = signals['close'].pct_change(fill_method='ffill').mean()
# signals['long_mavg'] = signals[4].shift(3)
# signals['long_close'] = df['close'].pct_change(fill_method='ffill').mean()

#signals[1] = signals[1].astype(float)
#signals[2] = signals[2].astype(float)
#signals[3] = signals[3].astype(float)
#signals[4] = signals[4].astype(float)
signals['MavgCross'][0:] = np.where(signals['close'] > signals['open'].shift(1), -0.1,
                                    0)  # & (signals['close'] > signals['high'].shift(1))  signals['short_mavg'] > signals['short_mavg'].shift(1) * .999
signals['number2'][0:] = np.where(signals['open'] < signals['high'].shift(1), 0.2, 0)
signals['ShiftOne'][0:] = np.where(
    (signals['close'] > signals['close'].shift(2)) & (signals['close'] > signals['close'].shift(1)), -0.1, 0)
signals['ShiftTwo'][0:] = np.where(
    (signals['close'] > signals['close'].shift(1)) & (signals['high'].shift(1) > signals['close'].shift(3)), -0.1, 0)
signals['number5'][0:] = np.where(signals['high'] * .999 > signals['close'], 0.3, 0)
signals['number6'][0:] = np.where(
    (signals['low'] < signals['close'].shift(1)) & (signals['high'] > signals['close'].shift(1)) & (
                signals['low'].shift(1) > signals['close'].shift(3)), -0.1, 0)
signals['number7'][0:] = np.where(
    (signals['low'] < signals['close'].shift(1)) & (signals['high'] > signals['close'].shift(1)) & (
                signals['low'] < signals['close'].shift(3)), 0.2, 0)
signals['number8'][0:] = np.where(signals['short_mavg'] > signals['longer_mavg'], 0.2, 0)
signals['number9'][0:] = np.where(
    (signals['low'] < signals['close'].shift(2)) & (signals['high'] > signals['close'].shift(1)) & (
                signals['low'] < signals['close'].shift(1)), 0.2, 0)
signals['number10'][0:] = np.where(signals['open'] < signals['open'].shift(1), 0.3, 0)
signals['number11'][0:] = np.where(signals['high'] > signals['close'].shift(1), -0.1, 0)
signals['number12'][0:] = np.where(signals['open'] > signals['low'].shift(1), 0.1, 0)
signals['number13'][0:] = np.where(signals['close'] > signals['high'].shift(1), -0.1, 0)
signals['number14'][0:] = np.where(signals['low'] > signals['high'].shift(2), -0.1, 0)
signals['number15'][0:] = np.where(signals['low'] > signals['open'].shift(1), -0.1, 0)
signals['number16'][0:] = np.where(signals['short_mavg'] > signals['short_mavg'].shift(1) * 1.5, 0.2, 0)
signals['number17'][0:] = np.where(signals['volume'] > signals['volume'].shift(1), -0.1, 0)
signals['number18'][0:] = np.where(
    (signals['close'] > signals['open'].shift(1)) & (signals['close'] > signals['high'].shift(3)), -.1, 0)
signals['number19'][0:] = np.where(
    (signals['close'] > signals['low'].shift(2)) & (signals['open'] < signals['close'].shift(2)), .2, 0)
signals['number20'][0:] = np.where(
    (signals['low'] > signals['close'].shift(2)) & (signals['open'] > signals['high'].shift(3)), -.1, 0)
signals['number21'][0:] = np.where(
    (signals['open'] > signals['close'].shift(2)) & (signals['open'] > signals['high'].shift(3)), -.1, 0)
signals['number22'][0:] = np.where(
    (signals['close'] > signals['close'].shift(2)) & (signals['open'] > signals['open'].shift(3)), -.1, 0)
signals['number23'][0:] = np.where(
    (signals['open'] > signals['close'].shift(2)) & (signals['open'] > signals['open'].shift(4)), -.1, 0)
signals['number24'][0:] = np.where(
    (signals['open'] > signals['high'].shift(3)) & (signals['open'] > signals['open'].shift(2)), -.1, 0)
signals['number25'][0:] = np.where(
    (signals['close'] > signals['high'].shift(2)) & (signals['close'] > signals['open'].shift(3)), -.1, 0)
signals['number26'][0:] = np.where(
    (signals['open'] > signals['high'].shift(3)) & (signals['close'] > signals['open'].shift(5)), -.1, 0)
signals['number27'][0:] = np.where(
    (signals['open'] > signals['low'].shift(2)) & (signals['low'] > signals['open'].shift(2)), -.1, 0)
signals['number28'][0:] = np.where(
    (signals['high'] < signals['high'].shift(2)) & (signals['low'] < signals['close'].shift(3)), .2, 0)
signals['number29'][0:] = np.where(
    (signals['open'] > signals['low'].shift(1)) & (signals['low'] < signals['open'].shift(2)), .2, 0)
signals['number30'][0:] = np.where(signals['close'] < signals['close'].shift(1), .1, 0)
signals['number31'][0:] = np.where(signals['high'] < signals['high'].shift(1), .2, 0)
signals['number32'][0:] = np.where(signals['high'] < signals['open'].shift(1), .2, 0)
signals['number33'][0:] = np.where(signals['close'] < signals['open'].shift(1), .2, 0)
signals['number34'][0:] = np.where(signals['close'] < signals['high'].shift(1), .1, 0)
signals['number35'][0:] = np.where(signals['open'] < signals['high'].shift(2), .2, 0)
signals['number36'][0:] = np.where(signals['high'] < signals['open'].shift(2), .2, 0)
signals['number37'][0:] = np.where(signals['close'] < signals['open'].shift(2), .2, 0)
signals['number38'][0:] = np.where(signals['close'] < signals['open'].shift(3), .2, 0)
signals['number39'][0:] = np.where(signals['high'] < signals['open'].shift(3), .2, 0)
signals['number40'][0:] = np.where(signals['open'] < signals['high'].shift(3), .2, 0)
signals['number41'][0:] = np.where(signals['open'] < signals['high'].shift(4), .2, 0)
signals['number42'][0:] = np.where(signals['high'] < signals['open'].shift(4), .2, 0)
signals['number43'][0:] = np.where(signals['close'] < signals['open'].shift(4), .2, 0)
signals['number44'][0:] = np.where(signals['open'] > signals['high'].shift(2), -.1, 0)
signals['number45'][0:] = np.where(signals['volume'] > signals['volume'].shift(1), .2, 0)
signals['number46'][0:] = np.where(signals['volume'] > signals['volume'].shift(2), .2, 0)
signals['number47'][0:] = np.where(signals['volume'] > signals['volume'].shift(3), .1, 0)

signals['score'][0:] = signals['MavgCross'] + signals['number2'] + signals['ShiftOne'] + signals['ShiftTwo'] + signals[
    'number5'] + signals['number6'] \
                       + signals['number7'] + signals['number8'] + signals['number9'] + signals['number10'] + signals[
                           'number11'] + signals['number12'] \
                       + signals['number13'] + signals['number14'] + signals['number15'] + signals['number16'] + \
                       signals['number17'] + signals['number18'] \
                       + signals['number19'] + signals['number20'] + signals['number21'] + signals['number22'] + \
                       signals['number23'] + signals['number24'] \
                       + signals['number25'] + signals['number26'] + signals['number27'] + signals['number28'] + \
                       signals['number29'] + signals['number30'] \
                       + signals['number31'] + signals['number32'] + signals['number33'] + signals['number34'] + \
                       signals['number35'] + signals['number36'] \
                       + signals['number37'] + signals['number38'] + signals['number39'] + signals['number40'] + \
                       signals['number41'] + signals['number42'] \
                       + signals['number43'] + signals['number44'] + signals['number45'] + signals['number46'] + \
                       signals['number47']

signals['signal'][0:] = np.where((signals['score'] > .79) & (signals['score'].shift(1)*.10 <signals['score']) & (signals['score'].shift(2)*.10 <signals['score'].shift(1)), 1.0, 0)


print (signals['score'].iloc[20])


signals['positions'] = signals['signal'].diff()





# print(signals['score'])

if ((signals['score'].iloc[20] > .79) & (signals['score'].iloc[19]*.10 <signals['score'].iloc[20]) & (signals['score'].iloc[18]*.10 <signals['score'].iloc[19])):

    limitOrder(0,quantity)
    print("BUY/SELL HAS RUN, RESTARTING...")

    now = datetime.now()

    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')

else:
    print("SKIPPED, PAUSE 1Min")
    time.sleep(30)
    subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')





