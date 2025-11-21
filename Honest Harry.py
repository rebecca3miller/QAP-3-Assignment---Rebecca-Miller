# Description: Program to keep track of honest harry's sales.
# Author: Rebecca Miller
# Date(s): November, 12, 2025


# Define required libraries.
import Validations as VD
import datetime
import FormatValues as FV

# Define program constants.
LOW_STANDARD_RATE = 75.00
HIGH_STANDARD_RATE = 165.00
HST_RATE = .15
TRANSFER_FEE = 1.0
LUXURY_TAX = 1.6
FINANCE_FEE = 39.99

YEARS_TO_PAY = 4
INVOICE_DATE = datetime.datetime.now().strftime("%Y-%m-%d")

# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    while True:
        CustFName = input("Enter the customer first name: ").title()
        if VD.valid_names(CustFName):
            break
    while True:
        CustLName = input("Enter the customer last name: ").title()
        if VD.valid_names(CustLName):
            break
    while True:
        PhoneNum = input("Enter the customer phone number (999-999-9999): ")
        if VD.valid_phone_num(PhoneNum):
            break
    while True:
        PlateNum = input("Enter the customer plate number (XXX999): ").upper()
        if VD.valid_plate(PlateNum):
            break
        


    CarMake = input("Enter the car make (Toyota): ").title()
    CarModel = input("Enter the car model (Corola): ").title()
    CarYear = int(input("Enter the car year (2018): "))
    while True:
        SellPrice = float(input("Enter the selling price (does not exceed $50,000.00): "))
        if VD.valid_price(SellPrice):
            break
    TradeAmt = float(input("Enter the trade in amount (does not exceed selling price): "))
    if TradeAmt > SellPrice:
        print(f" ** Data Entry Error - Trade in price cannot exceed the selling price.")
    else:
        break
    while True:
        SalesPersonName = input("Enter the salesperson name: ")
        if VD.valid_names(SalesPersonName):
            break

    ReceiptId = CustFName[0] + CustLName[0] + "-" + PlateNum[3:7] + "-" + PhoneNum[5:11]

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



# Calculate financing fee and total price
FinancingFee = FINANCE_FEE * YEARS_TO_PAY
TotalPrice = TotSales + FINANCE_FEE * YEARS_TO_PAY
TotalMonths = YEARS_TO_PAY * 12
MonthlyPayment = TotalPrice / TotalMonths


CurDate = datetime.datetime.now()
if CurDate.day >= 25:
    FirstPaymentDate = (CurDate.timedelta(days=32)).replace(day=1)
else:
    FirstPaymentDate = (CurDate.timedelta(days=32)).replace(day=1)



# Loop for years 1 to 4 
for Year in range(1, YEARS_TO_PAY + 1):
    FinancingFeeYear = FINANCE_FEE * Year
    TotalPriceYear = TotSales + FinancingFeeYear
    MonthlyPaymentYear = TotalPriceYear / (Year * 12)

   


    # Display results
    print()
    print()
    print(f"Honest Harry Car Sales                             Invoice Date:  {INVOICE_DATE:>20s}")
    print(f"Used Car Sale and Receipt                          Receipt No:    {ReceiptId:>20s}")
    print()
    print(f"                                                Sale price:             {FV.FDollar2(SellPrice):>15s}")
    print(f"Sold to:                                        Trade Allowance:         {FV.FDollar2(TradeAmt):>15s}")
    print(f"                                                -----------------------------------------")
    print(f"     {CustFName + CustLName}                    Price after Trade:      {FV.FDollar2(PriceAfterTrade):>20s}")
    print(f"     {PhoneNum}                                 License Fee:      {FV.FDollar2(LicenseFee):>20s}")
    print(f"                                                Transfer Fee:             {FV.FDollar2(TransFee):>15s}")
    print(f"                                                -----------------------------------------")
    print(f"Car Details:                                    Subtotal:         {FV.FDollar2(SubTot):>15s}")
    print(f"   {CarYear + CarModel + CarMake}               HST:      {FV.FDollar2(HSTCost):>20s}")
    print(f"                                                -----------------------------------------")
    print(f"                                                Total sales price:             {FV.FDollar2(TotSales):>15s}")
    print()
    print(f"-----------------------------------------------------------------------------------------")
    print()
    print(f"{'# Year':>4}  {'Financing Fee':>15}  {'Total Price':>15}  {'Monthly Payment':>17}")
    print(f"---------------------------------------------------------------------------------")
    print(f"---------------------------------------------------------------------------------")
    print(f"First payment date: {FirstPaymentDate:<15s}")
    print(f"-----------------------------------------------------------------------------------------")
    print(f"                     Best used cars at the best prices!")










    # Write the values to a data file for storage.



# Any housekeeping duties at the end of the program.