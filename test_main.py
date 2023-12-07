from fastapi.testclient import TestClient
from main import app
from test_course import courseA
from test_student import studentA, courseB
from course import courses
from student import stds

client = TestClient(app)

def test_get_stdCourses(studentA):
    studentA.addCourse(courseB)
    stds [studentA._IED] = studentA
    response = client.get("/stdCourses/1")
    assert response.status_code == 200
    assert response.json() == [
            ["COSC", "176", 30, "John Moe", 
        "Programming II", "PH 503", "TH 12:00"]
    ]
def test_get_courses(courseA):
    courses.append(courseA)
    print(courses)
    response = client.get("/courses/COSC")
    assert response.status_code == 200
    assert response.json() == [
        {
            "_prefix":"COSC",
            "_course_number":"111",
            "_cap":30,
            "_instructor":"John Doe",
            "_name":"Programming I",
            "_place":"PH 503",
            "_meeting_times":"TH 9:00"
        }]

    courses.pop()

