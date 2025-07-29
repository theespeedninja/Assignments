print("🧮BASIC CALCULATOR🧮")
num_1 = int( input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operrand = input("Enter operator (➕ , ➖ , ✖️ (*) , ➗(/) ): ")
if operrand == "+":
    result = num_1 + num_2
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}")
elif operrand == "-":
    result = num_1 - num_2
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}")
elif operrand == "*":
    result = num_1 * num_2
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}")
elif operrand == "/":
    result =float( num_1 / num_2)
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}")
else:
    print("\n‼️‼️‼️Invalid operator. Please use (➕ , ➖ , ✖️ (*) , ➗(/) ).")