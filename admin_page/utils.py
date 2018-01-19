import datetime
from planning.models import Planning
from supboard.enums import Grade


def grade_has_course(grade):
    date = datetime.datetime.now()
    count = Planning.objects.filter(date=date, grade=grade).count()
    return True if count > 0 else False


def get_grade_by_id(id):
    return {
        1: "grade_1",
        2: "grade_2",
        3: "grade_3",
        4: "grade_4",
        5: "grade_5"
    }[id]
