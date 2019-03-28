import psycopg2
import pymysql
import pymssql
import cx_Oracle
from django.conf import settings


class SqlConn:
    """
    连接数据库，以及进行一些操作的封装
    """

    # 创建连接、游标
    def __init__(self):
        print(settings.DATABASEs['default']['ENGINE'])
        if settings.DATABASEs['default']['ENGINE'] == 'django.db.backends.mysql':
            self.sql_name = 'mysql'
        elif settings.DATABASEs['default']['ENGINE'] == 'sql_server.pyodbc':
            self.sql_name = 'sqlserver'
            print(self.sql_name)
        else:
            self.sql_name = ''
            raise Warning("conn_error!")
        self.host = settings.DATABASEs['default']['HOST']
        self.port = settings.DATABASEs['default']['PORT']
        self.user = settings.DATABASEs['default']['USER']
        self.password = settings.DATABASEs['default']['PASSWORD']
        self.database = settings.DATABASEs['default']['NAME']

        sql_conn = {'mysql': pymysql,
                    'postgresql': psycopg2,
                    'sqlserver': pymssql,
                    'orcle': cx_Oracle
                    }

        self.conn = sql_conn[self.sql_name].connect(host=self.host,
                                                    port=self.port,
                                                    user=self.user,
                                                    password=self.password,
                                                    database=self.database,
                                                    # charset='utf8',
                                                    )
        self.cursor = self.conn.cursor()
        if not self.cursor:
            raise Warning("conn_error!")

    # 测试连接
    def test_conn(self):
        if self.cursor:
            print("conn success!")
        else:
            print('conn error!')

    # 单条语句的并提交
    def execute(self, sql_code):
        self.cursor.execute(sql_code)
        self.conn.commit()

    # 单条语句的不提交
    def execute_no_commit(self, sql_code):
        self.cursor.execute(sql_code)

    # 构造多条语句，使用%s参数化，对于每个list都进行替代构造
    def execute_many(self, sql_base, param_list):
        self.cursor.executemany(sql_base, param_list)

    # 批量执行（待完善）
    def batch_execute(self, sql_code):
        pass

    def get_headers(self, table_name):
        sql_code = "select COLUMN_NAME from information_schema.COLUMNS \
            where table_name = '%s' and table_schema = '%s';" % (
            table_name, self.database)
        self.execute(sql_code)
        return self.cursor.fetchall()

    # 获取数据
    def get_data(self, sql_code, count=0):
        print(sql_code)
        # sql_code = 'select employee.pin,employee.emp_name,iclock.sn,area.area_name from transaction, employee, iclock, area where transaction.employee_id=employee.id and transaction.iclock_id=iclock.id and iclock.area_id=area.id;'
        self.cursor.execute(sql_code)
        if int(count):
            return self.cursor.fetchmany(count)
        else:
            return self.cursor.fetchall()

    def get_headers_datas(self, sql_code, count=0):
        self.cursor.execute(sql_code)
        headers = []
        for each in self.cursor.description:
            headers.append(each[0])
        if int(count):
            return headers, self.cursor.fetchmany(count)
        else:
            return headers, self.cursor.fetchall()

    # 更新数据
    def update_data(self, sql_code):
        self.cursor(sql_code)

    # 插入数据
    def insert_data(self, sql_code):
        self.cursor(sql_code)

    # 滚动游标
    def cursor_scroll(self, count, mode='relative'):
        self.cursor.scroll(count, mode=mode)

    # 提交
    def commit(self):
        self.conn.commit()

    # 回滚
    def rollback(self):
        self.conn.rollback()

    # 关闭连接
    def close_conn(self):
        self.cursor.close()
        self.conn.close()
