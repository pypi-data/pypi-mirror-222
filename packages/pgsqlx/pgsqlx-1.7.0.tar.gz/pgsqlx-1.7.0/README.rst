Mapper file
'''''''''''

Create a mapper file in 'mapper' folder, you can named
'person_mapper.xml', like follow:

.. code:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "https://gitee.com/summry/pgsqlx/blob/master/dtd/mapper.dtd">
   <mapper namespace="person">
       <select id="select_all">
       <![CDATA[
            select id, name, age from person
       ]]>
       </select>
       
       <select id="select_by_name" include="select_all">
       <![CDATA[
            {{select_all}}
            {% if name -%}
             where name=:name
            {%- endif -%}
       ]]>
       </select>
   </mapper>

Usage Sample
''''''''''''

.. code:: python

   from pgsqlx.orm import Model
   from typing import List, Tuple, Mapping
   from pgsqlx import mapper, sql, db, dbx, init_db

   @mapper(namespace='person')
   def select_all(): List

   @mapper(namespace='person')
   def select_by_name(name: str): List

   @sql('select id, name, age from person')
   def query_all(): List(Mapping)

   @sql('select id, name, age from person where name=?')
   def query_by_name(name: str): List(Mapping)


   if __name__ == '__main__':
       init_db(host='127.0.0.1', port='3306', person='xxx', password='xxx', database='test', pool_size=5, show_sql=True, mapper_path='./mapper')
       
       persons = select_all()
       # result:
       # (3, 'zhangsan', 15)
       # (4, 'lisi', 26)
       # (5, 'wangwu', 38)
       
       persons = select_by_name(name='zhangsan')
       # result:
       # (3, 'zhangsan', 15)
       
       persons = query_all()
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}
       # {'id': 4, 'name': 'lisi', 'age': 26}
       # {'id': 5, 'name': 'wangwu', 'age': 38}
       
       persons = query_by_name('zhangsan')
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}
       
       # you can use dbx execte mapper sql with full sql id: namespace join sql id
       persons = dbx.select('person.select_all')  # 'person' is namespace, 'select_all' is sql id
       # result:
       # (3, 'zhangsan', 15)
       # (4, 'lisi', 26)
       # (5, 'wangwu', 38)
       
       persons = dbx.select('person.select_by_name', name='zhangsan')
       # result:
       # (3, 'zhangsan', 15)
       
       # you can direct execte sql with db
       persons = db.select('select id, name, age from person')
       # result:
       # (3, 'zhangsan', 15)
       # (4, 'lisi', 26)
       # (5, 'wangwu', 38)
       
       persons = db.select('select id, name, age from person where name=?', 'zhangsan')
       # result:
       # (3, 'zhangsan', 15)
       
       # you can use orm to operate a single table
       class person(Model):
           __pk__ = 'id'
           __table__ = 'person'
           __pk_seq__ = 'person_id_seq'

           def __init__(self, id: int = None, name: str = None, age: int = None):
               self.id = id
               self.name = name
               self.age = age
                     
       persons = person.query()
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}
       # {'id': 4, 'name': 'lisi', 'age': 26}
       # {'id': 5, 'name': 'wangwu', 'age': 38}
       
       persons = person.query(name__eq='zhangsan')
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}

Transaction
'''''''''''

.. code:: python

   from pgsqlx import with_transaction, transaction

   @with_transaction
   def test_transaction():
       insert_func(....)
       update_func(....)


   def test_transaction2():
       with transaction():
           insert_func(....)
           update_func(....)


You can generate model class with pgsqlx-generator: https://pypi.org/project/pgsqlx-generator

If you want to operate MySQL database, may be you need pgsqlx: https://pypi.org/project/mysqlx

If you just wanted a simple sql executor, may be you need sqlx-exec: https://pypi.org/project/sqlx-exec

If you wanted simultaneously support MySQL and PostgreSQL, may be you need sqlx-batis: https://pypi.org/project/sqlx-batis
