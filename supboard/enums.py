from enum import Enum


class Grade(Enum):
    ASC1 = "A.Sc.1"
    ASC2 = "A.Sc.2"
    BSC = "B.Sc"
    MSC1 = "M.Sc.1"
    MSC2 = "M.Sc.2"


class Url(Enum):
    INDEX = "/"
    ADMIN = "/admin"
    ADMIN_PLANNING_UPLOAD = "/admin/planning/upload"


class RowTarget(Enum):
    COURSE_CODE = 0
    DATE = 1
    GRADE = 2
    COURSE_NAME = 4
    TEACHER = 5
    HOUR = 7
    DURATION = 13
    CLASSROOM = 4


class Twitter(Enum):
    # CONFIGURE TWITTER ACCOUNT HERE
    TWEETS_LIMIT = 20
    COULD_NOT_AUTHENTICATE = "[Twitter] Could not authenticate you!"
    WAIT_ON_RATE_LIMIT = False
    CONSUMER_TOKEN = ""
    CONSUMER_SECRET = ""
    APP_TOKEN = ""
    APP_SECRET = ""
