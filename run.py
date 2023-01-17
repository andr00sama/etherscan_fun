#stopwatch start
from datetime import datetime
start = datetime.timestamp(datetime.now())

#imports
from contracts import USDC_WETH
from functions import getCurrentBlock, getTokentxns, getPrice

#run
print("Current ETH price: $" + str(getPrice(USDC_WETH)))

#stopwatch finish
finish = datetime.timestamp(datetime.now())
duration = round(finish - start,3)
print("Time to run: " + str(duration) + " seconds")
