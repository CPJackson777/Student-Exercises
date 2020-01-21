from student import Student
from cohort import Cohort
from exercise import Exercise
from instructor import Instructor


first_exercise = Exercise("1", "python",)
second_exercise = Exercise("2", "python")
third_exercise = Exercise("3", "python")
forth_exercise = Exercise("4", "python")

three_six = Cohort("Cohort 36")
three_seven = Cohort("Cohort 37")
three_eight = Cohort("Cohort 38")

guy = Student("Guy", "Cherkesky", "guy", "Cohort 36")
erin = Student("Erin", "Polley", "erin", "Cohort 36")
ryan = Student("Ryan", "Crowley", "ryan", "Cohort 36")
sam = Student("Sam", "Pita", "sam", "Cohort 36")

Joe = Instructor("Joe", "Shepherd", "joe", "Cohort 36", "Awesome at teaching Python")
Jisie = Instructor("Jisie", "David", "jisie", "Cohort 36", "Javascript and React Guru")
Jenna = Instructor("Jenna", "Solis", "jenna", "Cohort 36", "Fashion consultant and developer")

Joe.assign_exercise(guy, second_exercise)
Jisie.assign_exercise(ryan, third_exercise)
Jenna.assign_exercise(erin, forth_exercise) 

def exercise_list(list):
    for list_item in list:
        print(f"{list_item.name} is what I have to do today")

exercise_list(sam.exercises)