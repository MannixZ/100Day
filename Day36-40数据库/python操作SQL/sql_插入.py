import pymysql

no = int(input('部门编号: '))
name = input('部门名称: ')
location = input('部门所在地: ')

# 1. 创建连接（Connection）
conn = pymysql.connect(host='192.168.31.45', port=3306, user='guest', password='Guest.618', database='hrs', charset='utf8mb4')

try:
    # 2. 获取游标对象（Cursor）
    with conn.cursor() as cursor:
        # 3. 通过游标对象向数据库服务器发出SQL语句
        # 批量添加可以用 cursor.executemany() 方法
        affected_rows = cursor.executemany(
            'insert into `tb_dept` values (%s, %s, %s)',
            ((18, "冲锋部1", "连州"), (19, "充值部1", "罗镜"), (21, "人事部1", "云浮"), (22, "业务部1", "珠海"))
        )
        print(affected_rows)  # 返回 int 值，和列表或元祖内的数据组数一致
        # 单条插入数据  cursor.execute（）
        # affected_rows = cursor.execute(
        #     'insert into `tb_dept` values (%s, %s, %s)',
        #     (no, name, location)
        # )
        if affected_rows == 1:
            print('新增部门成功')
    # 4. 提交事务（transaction）
    conn.commit()
except pymysql.MySQLError as err:
    # 4. 回滚事务
    conn.rollback()
    print(type(err), err)
finally:
    # 5. 关闭连接释放资源
    conn.close()