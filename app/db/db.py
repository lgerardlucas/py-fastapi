'''
Mòdulo para conexão ao banco de dados

'''
import psycopg2
from decouple import config
from psycopg2.extras import RealDictCursor

class DBConnect(object):
    '''
    Class - Data base acess
    '''
    db=None
    def __init__(self):
        print('Preparando conexão, aguarde...')
        host = config('HOST')
        database = config('DB')
        usr = config('ROLE')
        pwd = config('PASSWORD')
        self._db = psycopg2.connect(host=host, database=database, user=usr,  password=pwd)
        print('Conexão estabelicida com sucesso"')

    def manipulate(self, sql):
        '''
        Funciont - Data manipulate
        '''
        try:
            cur=self._db.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except psycopg2.Error:
            return False
        return True

    def query(self, sql):
        '''
        Funciont - Query result
        '''
        result_set=None
        try:
            cur=self._db.cursor(cursor_factory=RealDictCursor)
            cur.execute(sql)
            result_set=cur.fetchall()
        except psycopg2.Error:
            return {"detail": "Erro ao executar a consulta!", "SQL": sql}

        return [dict(row) for row in result_set]

    def nextpk(self, tabela, chave):
        '''
        Funciont - Return primary key
        '''
        sql='select max('+chave+') from '+tabela
        result_set = self.query(sql)
        primarykey = result_set[0][0]
        return primarykey+1

    def close(self):
        '''
        Funciont - Closed connection
        '''
        self._db.close()