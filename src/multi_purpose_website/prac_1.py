
sum = 0
num = 0
count = 0

print("Welcome to the Sum & Average Calculator!")
print("Enter any number to start and -1 to end:")

while num != -1:
    num = int(input())
    sum += num
    if num == -1:
        sum += 1
        break
    count += 1
    
average = sum / count if count > 0 else 0
print ("Sum: ", sum)
print("Average: " , format(average, '.2f'))
