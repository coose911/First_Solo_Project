from db.run_sql import run_sql

from models.member import Member
from models.lesson import Lesson

def save(member):
    sql = "INSERT INTO members (first_name, last_name, dob) VALUES (%s, %s, %s) RETURNING id"
    values = [member.first_name, member.last_name, member.dob]
    results = run_sql(sql, values)
    member.id = results[0]["id"]
    return member

def select_all():
    members = []

    sql = "SELECT * FROM members"
    results = run_sql(sql)

    for row in results:
        member = Member(row["first_name"], row["last_name"], row["dob"], row["id"])
        members.append(member)
    return members