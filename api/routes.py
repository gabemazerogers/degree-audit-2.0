import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.join(os.getcwd(), os.pardir), 'scrap')))
import main

import falcon
import msgpack
import uuid
import mimetypes
import redis
import json

r = redis.Redis(host='localhost', port=6379, db=0)

class Auth(object):
    def __init__(self):
        pass

    def on_get(self, req, resp, username, password):
        userID = main.main(param=True, username=username, password=password)
        resp.body = '{"authToken": "%s"}' % userID
        resp.status = falcon.HTTP_200

class Courses(object):
    def __init__(self):
        pass

    def on_get(self, req, resp, token, group=None):
        courses = (r.get(token)).encode("utf-8")

        if group.lower() == "department":
            courses = group_courses_by_department(courses)

        elif group.lower() == "quarter":
            courses = group_courses_by_quarter(courses)

        courses = str(courses).replace('\'','\"')

        resp.body = courses
        resp.status = falcon.HTTP_200


def group_courses_by_quarter(courses):
    """
        Input: JSON object
        Returns: JSON object
        Sorts input courses by quarter
    """
    grouped = {}
    courses = byteify(json.loads(courses))
    for course in courses["courses"]:
        quarter = course["quarter"]
        if quarter in grouped:
            grouped[quarter].append(course)
        else:
            grouped[quarter] = [course]
    return grouped

def group_courses_by_department(courses):
    grouped = {}
    courses = byteify(json.loads(courses))
    for course in courses["courses"]:
        coursename = get_dept_from_name(course["course"])
        if coursename in grouped:
            grouped[coursename].append(course)
        else:
            grouped[coursename] = [course]
    return grouped

def get_dept_from_name(coursename):
    import re
    try:
        coursename = (re.match(r"([A-Z])\w+", coursename)).group(0)
        return coursename
    except:
        pass
    else:
        return ""


# Taken from stackoverflow: http://stackoverflow.com/questions/956867/how-to-get-string-objects-instead-of-unicode-ones-from-json-in-python

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input