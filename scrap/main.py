from bs4 import BeautifulSoup
import scrap
import re
import getpass
import person
import course
import redis
import hashlib
import time
import socket
import subprocess

REDIS_PORT = 6379
HOST = 'localhost'
DB_FLAG = 0

r = redis.Redis(host=HOST, port=REDIS_PORT, db=DB_FLAG)

DEV = True

def init():
    if DEV:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((HOST, REDIS_PORT))
        sock.close()
        if result is not 0:
            subprocess.call(["redis-server"])
            check_redis = subprocess.Popen(['redis-cli', 'ping'],
                                           stdout=subprocess.PIPE,
                                           stderr=subprocess.PIPE)
            success, fail = check_redis.communicate()
            if success:
                print("Redis started successfully.")
            elif fail:
                raise Exception("Error starting Redis.")


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
    span_array, html_doc, user_id = setup(param, username, password)
    student = build_student(span_array, html_doc)
    r.set(user_id, str(student.to_json_by_courses()))
    return user_id
