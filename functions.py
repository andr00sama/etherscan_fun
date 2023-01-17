from datetime import datetime
import requests, json

def getCurrentBlock():
    timestamp = str(round(datetime.timestamp(datetime.now())))
    link = "https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=" + timestamp + "&closest=before&apikey=3JGAJUKSIMFXWNJWDB4X9QY5CWYP8P262A"
    dictionary = json.loads(requests.get(link).text)
    return dictionary.get("result")

def getTokentxns(contract):
    currentBlock = getCurrentBlock()
    link = "https://api.etherscan.io/api?module=account&action=tokentx&address=" + str(contract) + "&startblock=" + str(int(currentBlock)-5) +"&endblock=" + str(currentBlock)+ "&apikey=3JGAJUKSIMFXWNJWDB4X9QY5CWYP8P262A"
    return json.loads(requests.get(link).text)

def getPrice(contract):
    tokentxns = getTokentxns(contract).get("result")
    swap1 = tokentxns[0]
    divisor = 1000000000000000000
    if swap1.get("tokenSymbol") == "USDC":
        divisor = 1000000
    amount1 = int(swap1.get("value"))/divisor
    swap2 = tokentxns[1]
    divisor = 1000000000000000000
    if swap2.get("tokenSymbol") == "USDC":
        divisor = 1000000
    amount2 = int(swap2.get("value"))/divisor
    ethAmount = 0
    usdcAmount = 0
    if amount1 > amount2:
        usdcAmount = amount1
        ethAmount = amount2
    else:
        ethAmount = amount1
        usdcAmount = amount2
    return round(usdcAmount/ethAmount,2)
