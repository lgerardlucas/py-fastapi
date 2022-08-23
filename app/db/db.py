'''
Mòdulo para conexão ao banco de dados

'''
import psycopg2
from decouple import config
from psycopg2.extras import RealDictCursor

class DBConnect(object):
   db=None
   def __init__(self):
        print('Preparando conexão, aguarde...')
        host = config('HOST')
        db = config('DB')
        usr = config('ROLE')
        pwd = config('PASSWORD')
        self._db = psycopg2.connect(host=host, database=db, user=usr,  password=pwd)
        print('Conexão estabelicida com sucesso"')

   def manipulate(self, sql):
        try:
            cur=self._db.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql)
            cur.close();
            self._db.commit()
        except:
            return False;
        return True;
   
   def query(self, sql):
       rs=None
       try:
           cur=self._db.cursor(cursor_factory=RealDictCursor)
           cur.execute(sql)
           rs=cur.fetchall();
       except:
           return None
       return [dict(row) for row in rs]

   def nextPK(self, tabela, chave):
       sql='select max('+chave+') from '+tabela
       rs = self.consultar(sql)
       pk = rs[0][0]
       return pk+1
   
   def close(self):
       self._db.close()

#cur = DBConnect()
#cliente = cur.query('select * from cliente')
#print(cliente[0])
