from decimal import Decimal

def to_double(object):
    string = object.replace("R$", "")
    string = string.replace(",", "")
    double = Decimal(string)
    return double


to_double("R$1,129.1234")