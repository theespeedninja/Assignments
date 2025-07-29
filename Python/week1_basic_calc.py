print("🧮BASIC CALCULATOR🧮")
#asking for user input for the two numbres
num_1 = int( input("Enter first number: "))
num_2 = int(input("Enter second number: "))
operrand = input("Enter operator (➕ , ➖ , ✖️ (*) , ➗(/) ): ")
#Checking the operator and performing the calculation
if operrand == "+":
    result = num_1 + num_2
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}") #Addition ➕
elif operrand == "-":
    result = num_1 - num_2
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}") #Subtraction ➖
elif operrand == "*":
    result = num_1 * num_2
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}") #Multiplication ✖️
elif operrand == "/":
    result =float( num_1 / num_2)
    print(f"🚀🚀🟰\n{num_1} {operrand} {num_2} = {result}") #Divison ➗
else:
    print("\n‼️‼️‼️Invalid operator. Please run the code again and make sure to use (➕ , ➖ , ✖️ (*) , ➗(/) ).")