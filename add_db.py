import sqlite3

conn = sqlite3.connect("skill.db")
c = conn.cursor()



def add_skill(id,skill_name,skill_description,creator_id,target_date):
    conn = sqlite3.connect("skill.db")
    c = conn.cursor()
    c.execute("INSERT INTO skill (id,skill_name,skill_description,creator_id,target_date) VALUES (?,?,?,?,?)",(id,skill_name,skill_description,creator_id,target_date,))
    conn.commit()

add_skill(1,"JavaScript","I want to learn JavaScript so I can make a reactive frontend for this",0,"2016-03-01")

