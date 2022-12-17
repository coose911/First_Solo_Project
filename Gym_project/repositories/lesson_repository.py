from db.run_sql import run_sql
from models.lesson import Lesson
from models.member import Member

def save(lesson):
    sql = "INSERT INTO lessons (name) VALUES (%s) RETURNING id"
    values = [lesson.name]
    results = run_sql(sql, values)
    lesson.id = results[0]['id']
    return lesson
