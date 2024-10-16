from flask import Flask, render_template, request
import json
import mysql.connector

app = Flask(__name__)
cnx = mysql.connector.connect(user='root', password='Formation20!',
host='127.0.0.1', port=3306,
database='st_perf')
mycursor = cnx.cursor()

class Student():
    """
    Class to handle Student objects and help with data formatting
    """
    def __init__(self, id, age, gender, gpa, gradeclass, studytime):
        self.id = id
        self.age = age
        self.gender = gender
        self.gpa = gpa
        self.gradeclass = gradeclass
        self.studytime = studytime

    def __repr__(self):
        return f'''{{"id": {self.id},"age": {self.age},"gender": {self.gender},"gpa": {self.gpa},"gradeclass": {self.gradeclass},"studytime": {self.studytime} }}'''
        
@app.route('/students', methods=['GET'])
def get_students():    
    """
    Get list of all students
    TODO: Paginate
    """
    mycursor.execute("select * from Students")
    results = mycursor.fetchall()
    students = [Student(r[0], r[1], r[2], r[3], r[4], r[5]) for r in results]
    return json.loads(repr(students))

@app.route('/student', methods=['GET'])
def get_student_by_id():
    """
    Get Student by ID.
    params:
    id: int
    """
    id = request.args['id']
    mycursor.execute(f'select ID, Age, Gender, GPA, GradeClass, StudyTimeWeekly from Students where ID={id}')
    results = mycursor.fetchall()
    if len(results) > 0:
        result = results[0]
        student = Student(result[0], result[1], result[2], result[3], result[4], result[5])
        return json.loads(repr(student))
    else:
        error = {'error': 'Invalid Student ID'}
        return error, 204

@app.route('/ethnicities', methods=['GET'])
def get_ethnicities():
    """
    Get ethnicities 
    """
    mycursor.execute('select * from ethnicity')
    results = mycursor.fetchall()
    results = [{'id': r[0], 'name': r[1]} for r in results]
    return results

@app.route('/activities', methods=['GET'])
def get_activities_by_id():
    """
    Get Activities by id
    params:
    id: int
    """
    id = request.args['id']
    sql_request = f"""select ExtracurricularactivitiesID, Activitytype from Extracurricularactivities as ea,
    student_to_activities as sa 
    where sa.StudentID = {id}
    and sa.ActivityID = ea.ExtracurricularactivitiesID"""
    mycursor.execute(sql_request)
    results = mycursor.fetchall()
    if len(results) > 0:
        results = [{'id': r[0], 'name': r[1]} for r in results]
        return results
    else:
        error = {'error': 'Invalid Activity ID'}
        return error, 204

@app.route('/parentalinfo', methods=['GET'])
def get_parental_info():
    """
    Get all Parental Information by Student ID
    params:
    id: int
    """
    id = request.args['id']
    sql_request = f"""select ParentalEducationLevel, ParentalSupport from Parentalinfo as pi 
    where pi.StudentID = {id}"""
    mycursor.execute(sql_request)
    results = mycursor.fetchall()
    if len(results) > 0:
        results = [{'Education Level': r[0], 'Support Level': r[1]} for r in results]
        return results
    else:
        error = {'error': 'Invalid Student ID'}
        return error, 204

if __name__ == '__app__':
    app.run(debug=True)
    
    cnx.close()
    
