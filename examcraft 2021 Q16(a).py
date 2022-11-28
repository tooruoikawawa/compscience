# Question 16(a)
# Student name:
def username():
    user_name = input("Please enter your username: ")
    return user_name

print("Welcome ", username(), ", to the student result calculator")

student_name = input("Please enter the students name: ")
student_score = float(input("Please enter the students mark: "))
exam_total = int(input("Please enter the total amount of marks going for the exam: "))

score_as_a_percentage = (student_score/exam_total)*100

if score_as_a_percentage >= 80:
    grade = "A"
elif score_as_a_percentage <= 59:
    grade = "C"
else:
    grade = "B"

print(student_name,"scored",round(score_as_a_percentage , 1),"%. They got a", grade)