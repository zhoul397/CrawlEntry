import pymysql

class HtmlOutputer(object):
    def __init__(self):
        self.datas = []
    def collect_data(self, new_data):
        if new_data is None:
            return
        print(new_data['summary'])
        self.datas.append(new_data)
    #数据库操作函数
    def into_mysql(self):
        i = 0
        for data in self.datas:
            conn = pymysql.Connect(
                host = '127.0.0.1',
                user = 'ROOT',
                password = '123456',
                db = 'baike',
                port = 3306,
                charset = 'utf8mb4'
            )
            try:
                cursor = conn.cursor()
                i += 1
                sql = 'INSERT INTO `citiao`(`ID`, `CiTiaoName`, `UrlHref`, `Content`) VALUES (%s, %s, %s, %s)'
                #执行上面的SQL语句，并传入3个参数
                cursor.execute(sql, (i, data['title'], data['url'], data['summary']))
                conn.commit()
            finally:
                conn.close()
