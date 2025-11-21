# Description: Program to keep track of honest harry's car sales.
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
TRANSFER_FEE = .01
LUXURY_TAX = .016
FINANCE_FEE = 39.99

YEARS_TO_PAY = 4
INVOICE_DATE = datetime.datetime.now().strftime("%Y-%m-%d")

# Define program functions.



# Main program starts here.
while True:
    
    # Gather user inputs.
    print()
    print()
    print("Honest Harry Car Sales")
    print("Please enter the following:")
    print()
    while True:
        CustFName =       input("Enter the customer first name:                             ").title()
        if VD.valid_names(CustFName):
            break
    while True:
        CustLName =       input("Enter the customer last name:                              ").title()
        if VD.valid_names(CustLName):
            break
    while True:
        PhoneNum =        input("Enter the customer phone number (999-999-9999):            ")
        if VD.valid_phone_num(PhoneNum):
            break
    while True:
        PlateNum =        input("Enter the customer plate number (XXX999):                  ").upper()
        if VD.valid_plate(PlateNum):
            break
        
    print()

    CarMake =             input("Enter the car make (Toyota):                               ").title()
    CarModel =            input("Enter the car model (Corola):                              ").title()
    CarYear = int(        input("Enter the car year (2018):                                 "))
    
    print()

    while True:
        SellPrice = float(input("Enter the selling price (does not exceed $50,000.00):      "))
        if VD.valid_price(SellPrice):
            break
    while True:
        TradeAmt = float( input("Enter the trade in amount (does not exceed selling price): "))
        if TradeAmt > SellPrice:
            print(f" ** Data Entry Error - Trade in price cannot exceed the selling price.   ")
        else:
            break
    while True:
        SalesPersonName =  input("Enter the salesperson name:                                ")
        if VD.valid_names(SalesPersonName):
            break

    ReceiptId = CustFName[0] + CustLName[0] + "-" + PlateNum[3:7] + "-" + PhoneNum[5:11]

    FormattedPhoneNum = f"({PhoneNum[:3]})-{PhoneNum[3:6]}-{PhoneNum[6:]}"

    # Perform required calculations.

    PriceAfterTrade = SellPrice - TradeAmt

    if SellPrice <= 15000.00:
        LicenseFee = LOW_STANDARD_RATE
    else:
        LicenseFee = HIGH_STANDARD_RATE
    
    TransFee = SellPrice * TRANSFER_FEE

    if SellPrice > 20000.00:
        TransFee += SellPrice * LUXURY_TAX

    SubTot = PriceAfterTrade + LicenseFee + TransFee
    
    HSTCost = SubTot * HST_RATE
    
    TotSales = SubTot + HSTCost


    # Display results
    print()
    print()
    print(f"Honest Harry Car Sales                             Invoice Date:  {INVOICE_DATE:>23s}")
    print(f"Used Car Sale and Receipt                          Receipt No:    {ReceiptId:>23s}")
    print()
    print(f"                                                Sale price:             {FV.FDollar2(SellPrice):>17s}")
    print(f"Sold to:                                        Trade Allowance:         {FV.FDollar2(TradeAmt):>16s}")
    print(f"                                                -----------------------------------------")
    print(f"     {CustFName} {CustLName}                                 Price after Trade:      {FV.FDollar2(PriceAfterTrade):>17s}")
    print(f"     {FormattedPhoneNum}                                 License Fee:      {FV.FDollar2(LicenseFee):>19s}")
    print(f"                                                Transfer Fee:             {FV.FDollar2(TransFee):>15s}")
    print(f"                                                -----------------------------------------")
    print(f"Car Details:                                    Subtotal:         {FV.FDollar2(SubTot):>23s}")
    print(f"                                                HST:      {FV.FDollar2(HSTCost):>31s}")
    print(f"     {CarYear} {CarMake} {CarModel}                        -----------------------------------------")
    print(f"                                                Total sales price:             {FV.FDollar2(TotSales):>10s}")
    print()
    print(f"-----------------------------------------------------------------------------------------")
    print()
    print(f"      {'# Year':>4}  {'# Payments':>15}  {'Financing Fee':>15}  {'Total Price':>16}  {'Monthly Payment':>21}")

    print(f"      ---------------------------------------------------------------------------------")

    CurrDate = datetime.datetime.now()
    year = CurrDate.year
    month = CurrDate.month

    
    if CurrDate.day >= 25:
        month += 2  
    else:
        month += 1


    if month > 12:
        month -= 12
        year += 1

    FirstPaymentDate = datetime.datetime(year, month, 1)

    # Create a loop for payment schedule.
    
    for Year in range(1, YEARS_TO_PAY + 1):
        NumPayments = Year * 12
        FinancingFeeYear = FINANCE_FEE * Year
        TotalPriceYear = TotSales + FinancingFeeYear
        MonthlyPaymentYear = TotalPriceYear / NumPayments

   
        FinancingFeeDsp = "${:,.2f}".format(FinancingFeeYear)
        TotalPriceDsp = "${:,.2f}".format(TotalPriceYear)
        MonthlyPaymentDsp = "${:,.2f}".format(MonthlyPaymentYear)

    
       
        print(f"{Year:>10} {NumPayments:>14} {FinancingFeeDsp:>16}  {TotalPriceDsp:>18}  {MonthlyPaymentDsp:>19}")


    print(f"      ---------------------------------------------------------------------------------")
    print(f"      First payment date:", FirstPaymentDate.strftime("%d-%b-%y"))
    print(f"-----------------------------------------------------------------------------------------")
    print(f"                                Best used cars at the best prices!")

    print()
    print()

    # Write the values to a data file for storage.



    # Any housekeeping duties at the end of the program.