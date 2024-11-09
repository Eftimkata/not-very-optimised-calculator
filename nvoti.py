def cancel():
    pass

def again():
    ask = input("Another equasion? ")
    if ask == "no" or ask == "-":
        cancel()
    else:
        calculator_module()

def calculator_module():
    v1 = float(input("Enter value 1: "))
    v2 = float(input("Enter value 2: "))
    
    print("\n Possible options:\n\n  +   -   *   /   \n\n or \n\n   plus   minus   times   devide  \n")
    what_to_do = input("What equasion: ")
    what_to_do = what_to_do.lower()

    
    if what_to_do == "plus" or what_to_do == "+":
        result = v1 + v2
        print(result)

        again()
    elif what_to_do == "minus" or what_to_do  == "-":
        # fixed a thing by...... nah i dont do comments
        result = v1 - v2
        print(result)

        again()
    elif what_to_do == "times" or what_to_do == "*":
        result = v1 * v2
        print(result)

        again()
    elif what_to_do == "devide" or what_to_do == "/":
        result = v1 / v2
        print(result)

        again()
    else:
        print("That is not valid choice try: \n  +  -  /  *  \n  plus  minus  times  devide  ")


