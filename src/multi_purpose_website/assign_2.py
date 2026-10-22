
try:
    num_of_students = int(input("Enter number of students: "))
except:
    raise TypeError

sum = 0
count = 0

for i in range(num_of_students):
    steps = int(input(f"Enter steps for student {i + 1}: "))

    if steps >= 10000:
        count += 1

    sum = sum + steps

percent = float((count/num_of_students) * 100)

print("Total steps:", sum)
print("Average steps:", (sum/num_of_students))
print("Students who achieved the targets:", count)
print("Students did not achieved targets:", (num_of_students - count))
print("Percentage achieved:", percent, "%")
