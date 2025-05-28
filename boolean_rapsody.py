import re

def calculator(statement):
    statement = re.sub(r"([()])", r" \1 ", statement)

    statement_as_list = [
        transform(unit)
        for unit in statement.split(" ")
    ]

    return eval(" ".join(statement_as_list))


def transform(unit):
    if unit in ["TRUE", "FALSE"]:
        return unit.capitalize()

    return unit.lower()
