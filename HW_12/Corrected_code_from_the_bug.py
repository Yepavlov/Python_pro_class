"""
There is a bug in def age, the function does not take into account the case when the student
has not yet had a birthday this year, but the result of the function will be the same
as if the student already had a birthday.
The corrected code is given below.
"""
from datetime import date


class Student(Person):
    uuid = models.UUIDField(default=uuid4, primary_key=True, unique=True, editable=False, db_index=True)
    group = models.ForeignKey("students.Group", on_delete=models.CASCADE)

    # def age(self):
    #     return datetime.datetime.now().year - self.birth_date.year

    def age(self):
        today = date.today()
        return (
                today.year
                - self.birth_date.year
                - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        )
