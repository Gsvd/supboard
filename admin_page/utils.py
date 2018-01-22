import datetime
from planning.models import Planning


def grade_has_course(grade):
    date = datetime.datetime.now()
    count = Planning.objects.filter(date=date, grade=grade).count()
    return True if count > 0 else False


def at_least_one_grade_on_campus_today():
    date = datetime.datetime.now()
    at_least = False
    for i in range(1, 6):
        count = Planning.objects.filter(date=date, grade=i).count()
        at_least = True if count > 0 else False
        if at_least:
            break
    return at_least

def get_grades_on_campus():
    result = []
    date = datetime.datetime.now()
    for i in range(1, 6):
        count = Planning.objects.filter(date=date, grade=i).count()
        result.append(True if count > 0 else False)
    return result


def get_grade_by_id(id):
    return {
        1: "grade_1",
        2: "grade_2",
        3: "grade_3",
        4: "grade_4",
        5: "grade_5"
    }[id]


def get_classrooms_by_date(date):
    grade_1 = Planning.objects.filter(date=date, grade=1)
    grade_2 = Planning.objects.filter(date=date, grade=2)
    grade_3 = Planning.objects.filter(date=date, grade=3)
    grade_4 = Planning.objects.filter(date=date, grade=4)
    grade_5 = Planning.objects.filter(date=date, grade=5)
    return {
        "grade_1": grade_1[0].classroom if len(grade_1) > 0 else None,
        "grade_2": grade_2[0].classroom if len(grade_2) > 0 else None,
        "grade_3": grade_3[0].classroom if len(grade_3) > 0 else None,
        "grade_4": grade_4[0].classroom if len(grade_4) > 0 else None,
        "grade_5": grade_5[0].classroom if len(grade_5) > 0 else None,
    }
