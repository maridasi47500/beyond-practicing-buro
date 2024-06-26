# coding=utf-8
import sqlite3
import sys
import re
from model import Model
class Userfamily(Model):
    def __init__(self):
        self.con=sqlite3.connect(self.mydb)
        self.con.row_factory = sqlite3.Row
        self.cur=self.con.cursor()
        self.cur.execute("""create table if not exists userfamily(
        id integer primary key autoincrement,
        user_id text,
            relationship_id text,
            member_id text
                    );""")
        self.con.commit()
        #self.con.close()
    def getallbyuserid(self,userid):
        self.cur.execute("select a.*,r.name as relation,m.name,m.sex from userfamily a left join user on user.id = a.user_id left join member m on m.id = a.member_id left join relationship r on r.id = a.relationship_id where a.user_id = ?",(userid,))

        row=self.cur.fetchall()
        return row
    def getall(self):
        self.cur.execute("select * from userfamily")

        row=self.cur.fetchall()
        return row
    def deletebyid(self,myid):

        self.cur.execute("delete from userfamily where id = ?",(myid,))
        job=self.cur.fetchall()
        self.con.commit()
        return None
    def getbyid(self,id):
        self.cur.execute("select a.*,m.sex,m.name, r.name as relation from userfamily a left join user on user.id = a.user_id left join member m on m.id = a.member_id left join relationship r on r.id = a.relationship_id where user_id = ?",(id,))

        row=self.cur.fetchone()
        return row
    def create(self,params):
        print("ok")
        myhash={}
        for x in params:
            if 'confirmation' in x:
                continue
            if 'envoyer' in x:
                continue
            if '[' not in x and x not in ['routeparams']:
                #print("my params",x,params[x])
                try:
                  myhash[x]=str(params[x].decode())
                except:
                  myhash[x]=str(params[x])
        print("M Y H A S H")
        print(myhash,myhash.keys())
        myid=None
        try:
          self.cur.execute("insert into userfamily (user_id,relationship_id,member_id) values (:user_id,:relationship_id,:member_id)",myhash)
          self.con.commit()
          myid=str(self.cur.lastrowid)
        except Exception as e:
          print("my error"+str(e))
        azerty={}
        azerty["userfamily_id"]=myid
        azerty["notice"]="votre userfamily a été ajouté"
        return azerty




