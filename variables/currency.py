a = int(input("How much you have is pesos? "))
b = int(input("How much you have in soles? "))
c = int(input("How much you have in reais? "))
total = a * 0.00026 + b * 0.30 + c * 0.19
print(total)
print("The total amount in dollars is:", total)
