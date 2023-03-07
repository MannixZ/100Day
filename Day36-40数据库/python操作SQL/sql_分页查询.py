import pymysql

page = int(input('页码: '))
size = int(input('大小: '))

# 1. 创建连接（Connection）
conn = pymysql.connect(host='192.168.31.45', port=3306, user='guest', password='Guest.618', database='hrs', charset='utf8mb4')

try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        # 删除多条
        cursor.execute(
            'select `eno`, `ename`, `job`, `sal` from `tb_emp` order by `sal` desc limit %s, %s ',
            ((page - 1) * size, size)
        )
        # 4. 通过游标对象抓取数据
        for emp_dict in cursor.fetchall():
            print(emp_dict)

finally:
    # 5. 关闭连接释放资源
    conn.close()