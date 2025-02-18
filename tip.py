def main():
    dollars = dollars_to_float(input("How much was the meal ?"))
    percent = percent_to_float(input("What percentage would you like to tip?"))
    tip = percent*dollars
    print(f"leave ${tip:.2f}")

# change dollars to decimal removing the sign
def dollars_to_float(d):
    d_without_dollar_sign = d.replace("$", "")
    return float(d_without_dollar_sign)


# chnge the percentages to dollars
def percent_to_float(p):
    p_without_percent = p.replace("%", "")
    p_converted = float(p_without_percent) /100
    return p_converted


main()