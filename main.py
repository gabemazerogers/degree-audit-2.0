from bs4 import BeautifulSoup
import re
file = open("UCSD Degree Audit Report.htm", "r")
html_doc = file.read()

soup = BeautifulSoup(html_doc, 'html.parser')
spans = soup.find_all('span')
span_arr = []
for span in spans:
    span_arr.append(span.getText())

class Person:
    grades = [];
    def __init__(self, name, pid, college, overall_gpa, units):
        self.name = name
        self.pid = pid
        self.college = college
        self.overall_gpa = overall_gpa
        self.units=units

    def calculate_GPA_per_dept(self, dept):
        filtered_grades = []
        for grade in self.grades:
            if grade.department == dept:
                filtered_grades.append(grade)

        total_units = 0
        total_weighted_units = 0
        points = 0
        # print grade.course
        for grade in filtered_grades:
            # print grade.grade
            if len(re.findall("[A,B,C,D,F]", grade.grade)) is 0:
                print grade.course
                filtered_grades.remove(grade)
                continue
            print grade.course
            total_units = total_units + float(grade.units)
            points = float(get_points_from_grade(grade.grade))
            total_weighted_units = total_weighted_units + (float(grade.units) * points)

        if total_units == 0:
            return 0
        return float(total_weighted_units) / float(total_units)

    def calculate_GPA_all_depts(self):
        dept_list = {}
        for course in self.grades:
            if not (course.department) in dept_list:
                dept_list[course.department] = 0
        for dept in dept_list:
            dept_list[dept] = self.calculate_GPA_per_dept(dept)
        print dept_list
        return dept_list

    #TODO Get points from letter grade
def get_points_from_grade(grade):
    letters = {'A' : 4.0, 'B' : 3.0, 'C' : 2.0, 'D' : 1.0, 'F' : 0.0}
    signs = {'+' : .3, '-' : -.3}
    letter = grade[0]
    if letter in letters:
        if letter == 'F':
            return 0.0
        if grade == "A+":
            return 4.0
        if len(grade) == 1:
            return letters[grade]
        else:
            return letters[grade[0]] + signs[grade[1]]
    else:
        return None




class Course:
    def __init__(self, quarter, year, department, course, units, grade):
        self.quarter = quarter
        self.year = year
        self.department = department
        self.course = course
        self.units = units
        self.grade = grade



student = Person(span_arr[3],span_arr[5],span_arr[7], span_arr[9], span_arr[11])

grades = re.findall("[A-Z]+[0-9]{1,3}[ ]+[A-Z]*[ ]*[A-Z]+[ ]*[0-9]*[A-Z]*[ ]+[0-9].[0-9][ ]+[A-Z]+[+,-]?", html_doc)
grade_arr = []
for grade in grades:
    grade = grade.split() #splits string by white spaces
    grade[:] = [x for x in grade if x != " "] #remove all white space elements
    if not grade[1].isalpha(): #checks for cases where department + course number are concantenated
        new_grade = re.findall(r"[^\W\d_]+|\d+", grade[1]) #splits the string between alpha and numeric
        grade[1] = new_grade[0]
        grade.insert(2, new_grade[1])
    if len(grade[1]) > 4:
        continue
    temp_year = grade[0]
    grade[0] = temp_year[:2]
    grade.insert(1, temp_year[2:])
    # print grade
    grade = Course(grade[0], grade[1], grade[2], grade[3], grade[4], grade[5])
    grade_arr.append(grade)
student.grades = grade_arr

student.calculate_GPA_all_depts()
dept_list = student.calculate_GPA_all_depts()
print type(dept_list)
import pygal
line_chart = pygal.Bar()

for key in dept_list:
    if dept_list[key] > 0:
        line_chart.add(key, [dept_list[key]])
line_chart.render_to_file('test.svg')
