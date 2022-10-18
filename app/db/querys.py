'''
destionation file to query data base
'''


from email.policy import default
from typing import Any


class SQLQuery():
    '''
    Class to manipulate database register - CRUD
    '''
    def __init__(self, 
            value: Any,
            table_name: str = None,
            field_name: str = None
        ) -> None:
        self.value = value
        self.table_name = table_name
        self.field_name = field_name if field_name else 'id'

    def query_search(self) -> str:
        '''
        Function - Record list from database
        '''
        where: str = f"Where {self.field_name} = '{self.value}'" if self.value else ''

        sql: str = f'''Select * From {self.table_name} {where} Order by {self.field_name}'''

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
            Where id = {self.value}
            '''

        return sql

    def delete(self) -> str:
        '''
        Function - Delete one register in database
        '''
        sql = f'''Delete From {self.table_name}
            where id = {self.value}
            '''

        return sql
