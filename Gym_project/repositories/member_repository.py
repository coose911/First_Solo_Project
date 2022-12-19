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

def select(id):
    member = None
    sql = "SELECT * FROM members WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if len(results) > 0:
        result = results[0]
        member = Member(result['first_name'], result['last_name'], result['dob'], result['id'] )
    return member

def update(member):
    sql = "UPDATE members SET (first_name, last_name, dob) = (%s,%s,%s) WHERE id = %s"
    values = [member.first_name, member.last_name, member.dob, member.id]
    run_sql(sql, values)