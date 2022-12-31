import gspread
from gspread_formatting import *
import steammarket as sm
import time
import json

import tkinter as tk
from tkinter import *

sa = gspread.service_account(filename="steam-price-373111-f3db7e886437.json")
sh = sa.open("CSGO Investment Trackor")

wks = sh.worksheet("ItemData")

def CountItems(values_list):
    values_list = wks.col_values(2)
    values_list = values_list[values_list.index("//Start Under This Row") + 1:]
    return len(values_list)

itemColumnLetter = 'B'
lowestPriceColumLetter = 'J'
medianPriceColumLetter = 'K'

firstItemRowNo = 7
valueslist=0

lastItemRow = firstItemRowNo + CountItems(valueslist)

itemLocation = ""
itemName = ""

window = Tk()
window.geometry("1000x500")


def AddItemToTable():
    lastItemRow = firstItemRowNo + CountItems(valueslist)
    e1=entryItemName.get()
    e2=entryQuantity.get()
    e3=entryBuyPrice.get()
    MyList = []
    MyList.append(e1)
    MyList.append(e2)
    MyList.append(e3)

    print(MyList)

    wks.update("B"+str(lastItemRow), e1)
    wks.update("C"+str(lastItemRow),e2)
    wks.update("D"+str(lastItemRow),e3)

s=StringVar

def ViewInventory():
    values_list = wks.col_values(2)
    values_list = values_list[values_list.index("//Start Under This Row") + 1:]
    MyList = []
    for i in values_list:
        MyList.append(i)
    s = str(MyList)
    s = s.replace(",", "\n")
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.replace("'", "")
    lblItemNameInv["text"] = "Item Name: \n"+s
    MyList.clear()
    print(MyList)
        
        
ItemAddMenu = Frame(window, bg='red',height=500,width=300)
ItemAddMenu.pack(side=LEFT)
ItemAddMenu.grid_propagate(0)
lblItemName = Label(ItemAddMenu, text='Item Name:',font=('Tahoma', 14), bg='red')
lblItemName.grid(column=0,row=0)
lblQuantity = Label(ItemAddMenu, text='Quantity:',font=('Tahoma', 14), bg='red')
lblQuantity.grid(column=0,row=2)
lblBuyPrice = Label(ItemAddMenu, text='Buy Price:',font=('Tahoma', 14), bg='red')
lblBuyPrice.grid(column=0,row=4)

entryItemName = Entry(ItemAddMenu, text='Item Name:',font=('Tahoma', 14), bg='red',width=250)
entryItemName.grid(column=2,row=0)
entryQuantity = Entry(ItemAddMenu, text='Quantity:',font=('Tahoma', 14), bg='red',width=250)
entryQuantity.grid(column=2,row=2)
entryBuyPrice = Entry(ItemAddMenu, text='Buy Price:',font=('Tahoma', 14), bg='red',width=250)
entryBuyPrice.grid(column=2,row=4)

addItemBtn = Button(ItemAddMenu, text="Add Item!", command=AddItemToTable, font=("Tahoma", 14), bg='red')
addItemBtn.grid(column=0,row=6)
viewInvBtn = Button(ItemAddMenu, text="View Inventory!", command=ViewInventory, font=("Tahoma", 14), bg='red')
viewInvBtn.grid(column=0,row=8)

InventoryMenu = Frame(window, bg='red',height=500,width=500)
InventoryMenu.pack()
InventoryMenu.grid_propagate(0)

Item1 = Frame(InventoryMenu ,bg='black',height=500, width=500)
Item1.grid(column=0,row=0)
Item1.grid_propagate(0)
lblItemNameInv = Label(Item1, anchor='w',text='Item Name: Sticker | Natus Vincere | Stockholm 2021',font=('Tahoma', 12), bg='black')
lblItemNameInv.grid(column=0,row=0)
lblQuantityInv = Label(Item1, text='Quantity: ',font=('Tahoma', 12), bg='red')
lblQuantityInv.grid(column=1,row=0)
lblBuyPriceInv = Label(Item1, text='Buy Price: ',font=('Tahoma', 12), bg='red')
lblBuyPriceInv.grid(column=2,row=0)



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
