from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member

def save(lesson):
    sql = "INSERT INTO lessons (name, time, date) VALUES (%s,%s,%s) RETURNING id"
    values = [lesson.name, lesson.time, lesson.date]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson

def select_all():
    lessons = []

    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    for row in results:
        lesson = Lesson(row["name"], row["time"], row["date"], row["id"])
        lessons.append(lesson)
    return lessons


