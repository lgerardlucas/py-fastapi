from db.db import DBConnect

def list_people(DBConnect):
    cur = DBConnect()
    cliente = cur.query('select * from cliente')
    print(cliente[0])

list_people()