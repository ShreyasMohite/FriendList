import sqlite3

def Friendlist():
    conn=sqlite3.connect("Friend")
    cur=conn.cursor()
    cur.execute("create table if not exists friendlist(id integer primary key,name text,facebook text,instagram text,whatsapp text)")
    conn.commit()
    conn.close()
    
def add_friendlist(name,facebook,instagram,whatsapp):
    conn=sqlite3.connect("Friend")
    cur=conn.cursor()
    cur.execute("insert into friendlist values(null,?,?,?,?)",(name,facebook,instagram,whatsapp))
    conn.commit()
    conn.close()
    
def view_friendlist():
    conn=sqlite3.connect("Friend")
    cur=conn.cursor()
    cur.execute("select * from friendlist")
    row=cur.fetchall()
    conn.close()
    return row


def delete_friendlist(id):
    conn=sqlite3.connect("Friend")
    cur=conn.cursor()
    cur.execute("delete from friendlist where id=?",(id,))
    conn.commit()
    conn.close()

def update_friendlist(id,name=" ",facebook=" ",whatsapp=" ",instagram=" "):
    conn=sqlite3.connect("Contact")
    cur=conn.cursor()
    cur.execute("select * from friendlist where name=?  or facebook=? or whatsapp=? or instagram=?",(name,facebook,whatsapp,instagram,id))
    conn.commit()
    conn.close()




Friendlist()

