# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#newlist = sorted(student_scores)
#high_score_index = len(newlist)-1
#high_score = newlist[high_score_index]
#print(f"The highest score in the class is: {high_score}")

#above code is not how this exercise was meant to be solved. Sorted function was not taught. Meant to use for loop.
save_score = 0
for student_score in student_scores:
  if student_score >= save_score:
    save_score = student_score
  
print(f"The highest score in the class is: {save_score}")

#This is intended code. Both work.