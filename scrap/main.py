from bs4 import BeautifulSoup
import scrap
import re
import getpass
import person
import course
import redis
import hashlib
import time

r = redis.Redis(host='localhost', port=6379, db=0)

def setup(param=False, username="", password=""):
    if not param:
        username = raw_input("PID: ").strip()
        password = getpass.getpass().strip()
    userID = hashlib.md5((username+password).encode('utf-8')).hexdigest()
    userID = hashlib.md5((userID+ str(time.time())).encode('utf-8')).hexdigest()
    html_doc = scrap.get_html(username, password)
    soup = BeautifulSoup(html_doc, 'html.parser')
    spans = soup.find_all('span')
    span_arr = []
    for span in spans:
        span_arr.append(span.getText())
    return span_arr,html_doc, userID

def build_student(span_array,html_doc):
    student = person.Person(span_array[3],span_array[5],span_array[7], span_array[9], span_array[11])
    student.grades = course.get_grade_arr(html_doc)
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


def main(param=False, username="", password=""):
    span_array, html_doc,userID = setup(param, username, password)
    student = build_student(span_array, html_doc)
    r.set(userID, str(student.to_json_by_courses()))
    return userID