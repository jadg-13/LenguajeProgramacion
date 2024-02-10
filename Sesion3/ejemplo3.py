#funciones

def get_full_name(name, last_name):
    full_name = name + ' ' + last_name
    return full_name

def getGrade(homeWork= 0, test= 0, final= 0):
    grade = (homeWork * 0.3) + (test * 0.3) + (final * 0.4)
    return grade

def getAmountToPay(price, quantity, discount):
    amount = price * quantity
    amountToPay = amount - (amount * discount)
    return amountToPay

def getDiscount(amount, discount=0.1):
    return amount * discount
    