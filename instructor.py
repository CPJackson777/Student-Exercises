# Instructor needs a method to assign an exercise to a student


class Instructor:
    def __init__(self, first_name, last_name, slack, cohort, specialty):
        self.first_name = first_name
        self.last_name = last_name
        self.slack = slack
        self.cohort = cohort
        self.specialty = specialty

    def assign_exercise(self, student, exercise):
        student.exercises.append(exercise)

#use dot notation to append the exercise to the student's list.