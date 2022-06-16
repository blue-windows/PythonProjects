v1 = input("Enter in your first number: ")
v2 = input("Enter in your second number: ")
is_running = True

while is_running:
    op = input("Do you want to: \n[a]dd\n[s]ubtract\n[m]ultiply\n[d]ivide\n[e]nd\n").lower()
    if op == "a":
        sum = int(v1) + int(v2)
        print("\n"+v1 + " + " + v2 + " = " + str(sum) + "\n")
    if op == "s":
        dif = int(v1) - int(v2)
        print("\n"+ v1 + " - " + v2 + " = " + str(dif) + "\n")
    if op == "m":
        prod = int(v1) * int(v2)
        print("\n"+v1 + " * " + v2 + " = " + str(prod) + "\n")
    if op == "d":
        quot = int(v1) / int(v2)
        print("\n"+v1 + " / " + v2 + " = " + str(quot) +  "\n")
    if op == "e":
        break
