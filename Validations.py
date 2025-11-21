# Validations for Honest Harry Program.

# License plate validation.


def valid_plate(PlateNum):
    all_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    if PlateNum == "":
        print(f" ** Data Entry Error - Plate number cannot be blank.")
        return False
    elif PlateNum != 6:
        print(f" ** Data Entry Error - Plate number must be 6 characters.")
        return False
    elif not set(PlateNum).issubset(all_char):
        print(f" ** Data Entry Error - Plate number contains invalid characters.")
        return False
    elif not PlateNum[3:].isdigit():
        print(" ** Data Entry Error - Plate number must be in format XXX999.")
        return False
    else:
        return True

    
def valid_phone_num(PhoneNum):
    all_char = set("1234567890")
    if PhoneNum == "":
        print(f" ** Data Entry Error - Phone number cannot be blank.")
        return False
    elif set(PhoneNum).issubset(all_char):
        print(f" ** Data Entry Error - Phone number contains invalid characters.")
        return False
    else:
        return True

    
def Valid_Names(CustFName):
    all_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if CustFName == "":
        print(f" ** Data Entry Error - Customer name cannot be blank.")
        return False
    elif set(CustFName).issubset(all_char):
        print(f" ** Data Entry Error - Customer name contains invalid characters.")
        return False
    else:
        return True





