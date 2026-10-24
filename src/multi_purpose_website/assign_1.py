
print("Enter amount of flour (kg) to donate to Old Folk House:")
print("(Flour sack with the heaviest weight will be given to Old House Folk A)")

totalKg , average , heavyFlour = 0.00, 0.00, 0.00
flourList = []

i = 1
while i <= 10:
    calc = input()
    if float(calc) >= 100 or float(calc) < 0:
        continue
    else:
        totalKg += float(calc)
        flourList.append(float(calc))
    i += 1

heavyFlour = max(flourList)
average = float(totalKg / 10)

print("Total kg of flour: " , totalKg , "kg")
print("Average kg of flour: " , average , "kg")
print("Flour for Old Folk House A: " , heavyFlour , "kg")