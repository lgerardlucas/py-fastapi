'''
destionation file to query data base
'''


class SQLQuery():
    '''
    Class to manipulate database register - CRUD
    '''
    def __init__(self, id_num: int = 0, table_name: str = None) -> None:
        self.id_num = id_num
        self.table_name = table_name

    def query_search(self) -> str:
        '''
        Function - Record list from database
        '''
        where: str = f'Where id = {self.id_num}' if self.id_num > 0 else ''

        sql: str = f'''Select * From {self.table_name} {where} Order by id'''

        return sql

    def insert(self, **kwargs: str) -> str:
        '''
        Function - Save register new in database
        '''
        keys_fields = ','.join(kwargs.keys())
        keys_values =  "','".join(kwargs.values())

        sql: str = f'''Insert Into {self.table_name}({keys_fields}) 
            Values( '{keys_values}')
            '''

        return sql

    def update(self, **kwargs: str) -> str:
        '''
        Function - Update one register in dababase
        '''
        update_fields: str = ''
        for i in range(len(kwargs.keys())):
            update_fields += f"{list(kwargs.keys())[i]}='{list(kwargs.values())[i]}'"
            update_fields += ',' if i+1 < len(kwargs.keys()) else ''

        sql = f'''Update {self.table_name} Set {update_fields}
            Where id = {self.id_num}
            '''

        return sql    

    def delete(self) -> str:
        '''
        Function - Delete one register in database
        '''
        sql = f'''Delete From {self.table_name}
            where id = {self.id_num}
            '''

        return sql
