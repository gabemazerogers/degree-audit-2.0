from bs4 import BeautifulSoup
import scrap
import re
import getpass
import person
import course


def setup():
    username = raw_input("PID: ").strip()
    password = getpass.getpass().strip()
    html_doc = scrap.get_html(username, password)

    soup = BeautifulSoup(html_doc, 'html.parser')
    spans = soup.find_all('span')
    span_arr = []
    for span in spans:
        span_arr.append(span.getText())
    return span_arr,html_doc

def build_student(span_arrray,html_doc):
    student = person.Person(span_array[3],span_array[5],span_array[7], span_array[9], span_array[11])
    student.grades = course.get_grade_arr(html_doc)
    for grade in student.grades:
        print grade.grade_to_json()
    student.calculate_GPA_all_depts()
    return student 

def generate_grade_chart(student):
    dept_list = student.calculate_GPA_all_depts()
    import pygal
    line_chart = pygal.Bar()

    for key in dept_list:
        if dept_list[key] > 0:
            line_chart.add(key, [dept_list[key]])
    line_chart.render_to_file('grade_chart.svg')
    print("%s has been created!" % "grade_chart.svg")

span_array, html_doc = setup()
student = build_student(span_array, html_doc)
generate_grade_chart(student)
