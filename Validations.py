# Validations for Honest Harry Program.

# License plate validation.


def valid_plate(PlateNum):
    all_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
    if PlateNum == "":
        print(f" ** Data Entry Error - Plate number cannot be blank.")
        return False
    elif len(PlateNum) != 6:
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
    elif len(PhoneNum) != 10:
        print(f" ** Data Entry Error - Phone number must be 10 characters.")
        return False
    elif not set(PhoneNum).issubset(all_char):
        print(f" ** Data Entry Error - Phone number contains invalid characters.")
        return False
    else:
        return True

    
def valid_names(Name):
    all_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    if Name == "":
        print(f" ** Data Entry Error - Customer name cannot be blank.")
        return False
    elif not set(Name).issubset(all_char):
        print(f" ** Data Entry Error - Customer name contains invalid characters.")
        return False
    else:
        return True


def valid_price(Price):
    if Price == "":
        print(f" ** Data Entry Error - Selling price cannot be blank.")
        return False
    elif Price > 50000:
        print(f" ** Data Entry Error - Selling price cannot exceed 50,000.00.")
        return False
    else:
        return True







