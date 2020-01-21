# Properties
# First name
# Last name
# Slack handle
# The student's cohort
# exercises[]


class Student:
    def __init__(self, first_name, last_name, slack_handle, cohort):
        self.first_name = first_name
        self.last_name = last_name
        self.slack_handle = slack
        self.cohort = cohort
        self.exercises = []
    def add_exercises(self, exercises_list):
        self.exercises.extend(exercises_list)