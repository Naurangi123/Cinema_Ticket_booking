# '''CREATE TABLE "seat" (
# 	"seat_id"	TEXT,
# 	"taken"	INTEGER,
# 	"Field4"	INTEGER
# );'''
#
import sqlite3


def create_table():
    connection = sqlite3.connect("cinema.db")
    connection.execute("""
    CREATE TABLE "seat" (
	"seat_id"	TEXT,
	"taken"	INTEGER,
	"price"	REAL
    );
    """)
    connection.commit()
    connection.close()

def insert_record():
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
    INSERT INTO "seat"("seat_id","taken","price") VALUES("A1","0","100"),("A2","1","130"),("A3","0","160")
    """)

    connection.commit()
    connection.close()
def select_all():
    connection=sqlite3.connect("cinema.db")
    cursur=connection.cursor()
    cursur.execute("""
    SELECT * FROM "seat"
    """)
    result=cursur.fetchall()
    connection.close()
    return result

def select_specific_columns():
    connection=sqlite3.connect("cinema.db")
    cursur=connection.cursor()
    cursur.execute("""
    SELECT "seat_id","price" FROM "seat"
    """)
    result=cursur.fetchall()
    connection.close()
    return result

def select_with_condition():
    connection=sqlite3.connect("cinema.db")
    cursur=connection.cursor()
    cursur.execute("""
    SELECT "seat_id","price" FROM "seat" WHERE "price">130
    """)
    result=cursur.fetchall()
    connection.close()
    return result

def update_value():
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
    UPDATE "seat" SET "taken"=0 WHERE "seat_id"="A1"
    """)
    connection.commit()
    connection.close()

def delete_records():
    connection=sqlite3.connect("cinema.db")
    connection.execute("""
    DELETE FROM "seat"WHERE "seat_id"="A1"
    """)
    connection.commit()
    connection.close()

create_table()
# insert_record()
# print(select_all())
# # print(select_specific_columns())
# # print(select_with_condition())
# #update_value()
# delete_records()
