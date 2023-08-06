Mapper file
'''''''''''

Create a mapper file in 'mapper' folder, you can named
'user_mapper.xml', like follow:

.. code:: xml

   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE mapper PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN" "https://gitee.com/summry/mysqlx/blob/master/dtd/mapper.dtd">
   <mapper namespace="user">
       <select id="select_all">
       <![CDATA[
            select id, name, age from user
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

   from mysqlx.orm import Model
   from typing import List, Tuple, Mapping
   from mysqlx import mapper, sql, db, dbx, init_db

   @mapper(namespace='user')
   def select_all(): List

   @mapper(namespace='user')
   def select_by_name(name: str): List

   @sql('select id, name, age from user')
   def query_all(): List(Mapping)

   @sql('select id, name, age from user where name=?')
   def query_by_name(name: str): List(Mapping)


   if __name__ == '__main__':
       init_db(host='127.0.0.1', port='3306', user='xxx', password='xxx', database='test', pool_size=5, show_sql=True, mapper_path='./mapper')
       
       users = select_all()
       # result:
       # (3, 'zhangsan', 15)
       # (4, 'lisi', 26)
       # (5, 'wangwu', 38)
       
       users = select_by_name(name='zhangsan')
       # result:
       # (3, 'zhangsan', 15)
       
       users = query_all()
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}
       # {'id': 4, 'name': 'lisi', 'age': 26}
       # {'id': 5, 'name': 'wangwu', 'age': 38}
       
       users = query_by_name('zhangsan')
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}
       
       # you can use dbx execte mapper sql with full sql id: namespace join sql id
       users = dbx.select('user.select_all')  # 'user' is namespace, 'select_all' is sql id
       # result:
       # (3, 'zhangsan', 15)
       # (4, 'lisi', 26)
       # (5, 'wangwu', 38)
       
       users = dbx.select('user.select_by_name', name='zhangsan')
       # result:
       # (3, 'zhangsan', 15)
       
       # you can direct execte sql with db
       users = db.select('select id, name, age from user')
       # result:
       # (3, 'zhangsan', 15)
       # (4, 'lisi', 26)
       # (5, 'wangwu', 38)
       
       users = db.select('select id, name, age from user where name=?', 'zhangsan')
       # result:
       # (3, 'zhangsan', 15)
       
       # you can use orm to operate a single table
       class User(Model):
           __key__ = 'id'
           __table__ = 'user'

           def __init__(self, id: int = None, name: str = None, age: int = None):
               self.id = id
               self.name = name
               self.age = age
                     
       users = User.query()
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}
       # {'id': 4, 'name': 'lisi', 'age': 26}
       # {'id': 5, 'name': 'wangwu', 'age': 38}
       
       users = User.query(name__eq='zhangsan')
       # result:
       # {'id': 3, 'name': 'zhangsan', 'age': 15}

Transaction
'''''''''''

.. code:: python

   from mysqlx import with_transaction, transaction

   @with_transaction
   def test_transaction():
       insert_func(....)
       update_func(....)


   def test_transaction2():
       with transaction():
           insert_func(....)
           update_func(....)

You can generate model class with mysqlx-generator: https://pypi.org/project/mysqlx-generator

If you want to operate PostgreSQL database, may be you need PgSqlx: https://pypi.org/project/pgsqlx

If you just wanted a simple sql executor, may be you need sqlx-exec: https://pypi.org/project/sqlx-exec

If you wanted simultaneously support MySQL and PostgreSQL, may be you need sqlx-batis: https://pypi.org/project/sqlx-batis
