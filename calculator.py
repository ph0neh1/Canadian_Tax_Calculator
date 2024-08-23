# API is restricted to 60 request per hour.
# Only calculates GST, PST, and HST for Canada.

import os
import requests
import json

os.system('cls||clear')
os.system('title Canadian Tax Calculator')

class TextColor:
    RESET = "\033[0m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    PURPLE = "\033[95m"
    CYAN = "\033[96m"

GST = 0
PST = 0
HST = 0
PROVINCE = "The KrustyKrab"
TOTALBT = 0
TOTALAT = 0

def FetchRates(province):
     global GST, PST, HST, PROVINCE

     response = requests.get("https://api.salestaxapi.ca/v2/province/all")
     if response.status_code == 200:
          provinces = response.json()
          if province in provinces:
               rates = provinces[province]
               PROVINCE=province
               GST = rates.get("gst", 0)
               PST = rates.get("pst", 0)
               HST = rates.get("hst", 0)
          else:
               print(f"Tax rate for {province} was not found.")
               return None
     else:
          print("Error fetching tax rates from API.")
          return None
     
def CalculateTax():
     global GST, PST, HST, PROVINCE, TOTALBT, TOTALAT

     if GST == 0:
          print(TextColor.RED + "There is no GST in " + PROVINCE + TextColor.RESET)
     else:
          GST = GST+1
          TOTALAT = float(TOTALAT) * GST

     if PST == 0:
          print(TextColor.RED + "There is no PST in " + PROVINCE + TextColor.RESET)
     else:
          PST = PST+1
          TOTALAT = float(TOTALAT) * PST

     if HST == 0:
          print(TextColor.RED + "There is no HST in " + PROVINCE + TextColor.RESET)
     else:
          HST = HST+1
          TOTALAT = float(TOTALAT) * HST

totally = input(TextColor.YELLOW + "Enter total amount before Tax" + " " + ":" + " " + TextColor.RESET)
TOTALBT= float(totally)
TOTALAT= float(totally)
provincey = input(TextColor.YELLOW + "Enter your Province (2 Letter abbrviation)" + " "+ ":"+ " " + TextColor.RESET)
FetchRates(provincey)
CalculateTax()
print(TextColor.GREEN + "Total (Before Tax)" + " " + ":" + " " + str(TOTALBT) + TextColor.RESET)
print(TextColor.GREEN + "Total (After Tax)" + " " + ":" + " " + str(TOTALAT) + TextColor.RESET)
