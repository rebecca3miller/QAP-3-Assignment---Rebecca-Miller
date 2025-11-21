# Description: Program to keep track of honest harry's sales.
# Author: Rebecca Miller
# Date(s): November, 12, 2025


# Define required libraries.
import Validations as VD


# Define program constants.
LOW_STANDARD_RATE = 75.00
HIGH_STANDARD_RATE = 165.00
HST_RATE = .15
TRANSFER_FEE = 1.0
LUXURY_TAX = 1.6
FINANCE_FEE = 39.99

# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    while True:
        CustFName = input("Enter the customer first name: ").title()
        if VD.Valid_Names(CustFName):
            break
    CustLName = input("Enter the customer last name: ").title()
    PhoneNum = input("Enter the customer phone number (999-999-9999): ")
    while True:
        PlateNum = input("Enter the customer plate number (XXX999): ").upper()
        if VD.valid_plate(PlateNum):
            break
        


    CarMake = input("Enter the car make (Toyota): ")
    CarModel = input("Enter the car model (Corola): ")
    CarYear = input("Enter the car year (2018): ")
    
    SellPrice = input("Enter the selling price (does not exceed $50,000.00): ")
    TradeAmt = input("Enter the trade in amount (does not exceed selling price): ")
    SalesPersonName = input("Enter the salesperson name: ")



    # Perform required calculations.
    PriceAfterTrade = SellPrice - TradeAmt

    if SellPrice <= 15000.00:
        LicenseFee = LOW_STANDARD_RATE
    else:
        LicenseFee = HIGH_STANDARD_RATE
    
    TransFee = SellPrice * TRANSFER_FEE

    LuxuryTax = 0
    if SellPrice > 20000.00:
        TransFee += LUXURY_TAX

    SubTot = PriceAfterTrade + LicenseFee + TransFee
    
    HSTCost = SubTot * HST_RATE
    
    TotSales = SubTot + HSTCost




    # Display results



    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.