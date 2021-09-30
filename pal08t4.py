points = int(input("Insert your points: "))

if points >= 0 and points < 2:
        grade = 0
elif points < 4:
        grade = 1
elif points < 6:
        grade = 2
elif points < 8:
        grade = 3
elif points < 10:
        grade = 4
elif points < 13:
        grade = 5

print("Grade: " + str(grade))   

