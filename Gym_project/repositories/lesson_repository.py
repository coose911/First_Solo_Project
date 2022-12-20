from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member


# repository is where you write a function to speak to the database via sql and return your instructions. controller then uses your function.

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

def select(id):
    lesson = None
    sql = "SELECT * FROM lessons WHERE id = %s"
    values = [id]
    results = run_sql(sql,values)

    if len(results) > 0:
        result = results[0]
        lesson = Lesson(result["name"], result["time"], result["date"], result["id"])
    return lesson

def update(lesson):
    sql = "UPDATE lessons SET (name, time, date) = (%s,%s,%s) WHERE id = %s"
    values = [lesson.name, lesson.time, lesson.date, lesson.id]
    run_sql(sql, values)

def delete(id):
    sql = "DELETE FROM lessons WHERE id = %s"
    values = [id]
    run_sql(sql, values)

