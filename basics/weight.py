weight = float(input("Enter weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    conv_weight = weight / 0.45
    print("Wight in Lbs: " + str(conv_weight))
elif unit.upper() == "L":
    conv_weight = weight * 0.45
    print("Wight in Kg: " + str(conv_weight))
