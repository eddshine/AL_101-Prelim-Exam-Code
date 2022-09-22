# Set-Builder Notation Symbols

element_of = "∈" # an element of set
not_element_of = "∉" # an element of set
whole_number = "W" # Whole numbers
integers = "Z" # Integers
natural_numbers = "N" # all natural numbers or all positive integers.
real_numbers = "R" # real numbers or any numbers that are not imaginary.
rational_numbers = "Q" # real numbers or any numbers that are not imaginary.


isNum = False
isString = False




def checkSet(set):
    symbol = ""
    conditions = ""
    set_builder = f"x | x = {conditions} {symbol}"

    global isNum
    global isString
    for x in range(len(set)):
        if set[x].isnumeric():
            isNum = True
        else:
            isString = True

    if 0 or "0" in set:
        conditions




