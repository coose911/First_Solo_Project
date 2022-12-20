from db.run_sql import run_sql

from models.booking import Booking
from models.member import Member
from models.lesson import Lesson

import repositories.member_repository as member_repository
import repositories.lesson_repository as lesson_repository

def save(booking):
    sql = "INSERT INTO bookings (member_id, lesson_id) VALUES (%s, %s) RETURNING id"
    values = [booking.member.id, booking.lesson.id]
    results = run_sql(sql, values)
    booking.id = results[0]['id']
    return booking

def select_all():
    lessons = []

    sql = "SELECT * FROM lessons"
    results = run_sql(sql)

    for row in results:
        lesson = Lesson(row["name"], row["time"], row["date"], row["id"])
        lessons.append(lesson)
    return lessons