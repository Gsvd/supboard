from django.db import models
import datetime

from supboard.enums import Grade


class Planning(models.Model):
    course_code = models.CharField(max_length=255)
    course_name = models.CharField(max_length=255)
    date = models.DateField(null=True)
    grade = models.IntegerField()
    teacher = models.CharField(max_length=255)
    hour = models.TimeField()
    duration = models.TimeField()
    classroom = models.CharField(max_length=255)
    exam_type = models.CharField(default="", max_length=255)

    def __str__(self):
        return str(self.id) + "\t\t" + self.course_code + "\t\t" + self.date.strftime("%Y-%m-%d") + "\t\t" + self.exam_type

    @property
    def get_grade(self):
        return {
            1: Grade.ASC1.value,
            2: Grade.ASC2.value,
            3: Grade.BSC.value,
            4: Grade.MSC1.value,
            5: Grade.MSC2.value
        }[self.grade]

    @property
    def get_course_start(self):
        return self.hour.strftime("%H:%M")

    @property
    def get_course_end(self):
        date = datetime.datetime(100, 1, 1, self.hour.hour, self.hour.minute, 00)
        end = date + datetime.timedelta(hours=self.duration.hour, minutes=self.duration.minute)
        return end.strftime("%H:%M")
