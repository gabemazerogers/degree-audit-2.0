import re, json, course

class Person:


    def __init__(self, name, pid, college, overall_gpa, units):
        self.name = name
        self.pid = pid
        self.college = college
        self.overall_gpa = overall_gpa
        self.units=units
        self.grades = []


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
                filtered_grades.remove(grade)
                continue
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
        return dept_list


    def to_json_by_courses(self):
        outer_json = {}
        grades = []
        for grade in self.grades:
            tmp = grade.grade_to_min_json()
            quarter_name = tmp[1]
            course_json = tmp[2]
            grades.append(course_json)
        outer_json["name"] = self.name
        outer_json["GPA"] = self.overall_gpa
        outer_json["courses"] = grades
        return sanitize_json(json.dumps(outer_json, ensure_ascii=True))

    def to_json_by_quarter(self):
        outer_json = {}
        grade_json = {}
        for grade in self.grades:
            tmp = grade.grade_to_min_json()
            quarter_name = tmp[1]
            course_json = tmp[2]
            if quarter_name in grade_json:
                grade_json[quarter_name].append(course_json)
            else:
                grade_json[quarter_name] = [course_json]
        outer_json["name"] = self.name
        outer_json["GPA"] = self.overall_gpa
        outer_json["courses"] = grade_json
        return sanitize_json(json.dumps(outer_json, ensure_ascii=True))


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

def sanitize_json(to_clean):
    to_clean = to_clean.replace("\\", "")
    to_clean = to_clean.replace("\"{", "{")
    to_clean = to_clean.replace("}\"", "}")
    return to_clean

