student_marks={
    "X":89,
    "Y":90,
    "Z":91,
    "A":92
}
name=input("Enter student's name:")
if name in student_marks:
    print("{}'s marks: {}".format(name,student_marks[name]))
else:
   print(" Student not found")
