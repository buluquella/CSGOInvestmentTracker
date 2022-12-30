import gspread
from gspread_formatting import *
import steammarket as sm
import time
import json

scriptLoopCount = 0

myInventory = []

sa = gspread.service_account(filename="steam-price-373111-f3db7e886437.json")
sh = sa.open("CSGO Investment Trackor")

wks = sh.worksheet("ItemData")

mHandler = ""

columnList = ['B','C','D']

def GetPrice(x, price):
    x = (data[price])
    x = x[:-1]
    x = float((x).replace(",", "."))
    return x

def UpdateSheet(lowestPriceLoc, medianPriceLoc):
    wks.update(lowestPriceLoc, GetPrice(mHandler, "lowest_price"))
    wks.update(medianPriceLoc, GetPrice(mHandler, "median_price"))

def AddItem(_ItemName, _Amount, _BuyPrice):
    MyList = []
    _ItemName = input("Write down the item name [ENG]: ")
    MyList.append(_ItemName)
    _Amount = input("How many did you buy [INT eg 100]: ")
    MyList.append(_Amount)
    _BuyPrice = input("What price did you invest at [eg; 18.51]: ")
    MyList.append(_BuyPrice)

    
    wks.update("B"+str(lastItemRow),_ItemName)
    wks.update("C"+str(lastItemRow),_Amount)
    wks.update("D"+str(lastItemRow),_BuyPrice)
    myInventory.append((_ItemName + " " + _Amount + " " + _BuyPrice))

def CountItems(values_list):
    values_list = wks.col_values(2)
    values_list = values_list[values_list.index("//Start Under This Row") + 1:]
    return len(values_list)

itemCount = int(input("How many items do you invest? "))

valueslist=0


aiIN = ""
aiAM = ""
aiBP = ""


while True:
    itemColumnLetter = 'B'
    lowestPriceColumLetter = 'J'
    medianPriceColumLetter = 'K'
    firstItemRowNo = 7
    lastItemRow = firstItemRowNo + CountItems(valueslist)
    itemLocation = ""
    itemName = ""

    for i in range(CountItems(valueslist)):
        itemLocation = itemColumnLetter + str(firstItemRowNo)
        LowestPriceLocation = lowestPriceColumLetter + str(firstItemRowNo)
        MedianPriceLocation = medianPriceColumLetter + str(firstItemRowNo)
        print("Processing: ",itemLocation)

        # myInventory.append(wks.acell(itemLocation).value)
        
        itemName = ((wks.acell(itemLocation).value))
        print(str(itemName))

        data = sm.get_item(730, itemName , currency='EUR')
        print(data)

        print("Looking for performance bugs...")
        time.sleep(1)

        UpdateSheet(lowestPriceLoc=LowestPriceLocation,
                    medianPriceLoc=MedianPriceLocation)

        firstItemRowNo += 1

    scriptLoopCount += 1

    
    AddItem(aiIN, aiAM, aiBP)

    print("Starting: ", scriptLoopCount,"th loop in 5 seconds...")
    time.sleep(5)
