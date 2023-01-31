-- 创建名为hrs的数据库并指定默认的字符集
CREATE DATABASE `hrs`  DEFAULT charset utf8mb4;

-- 切换到hrs数据库
USE hrs

-- 创建部门表
CREATE TABLE tb_dept
(
dno int NOT NULL COMMENT '编号',
dname VARCHAR(10) not NULL COMMENT '部门名称',
dloc VARCHAR(20) NOT NULL COMMENT '部门所在地',
PRIMARY KEY (dno)
);

-- 插入4个部门
INSERT INTO tb_dept VALUES
		(10, '会计部', '北京'),
    (20, '研发部', '成都'),
    (30, '销售部', '重庆'),
    (40, '运维部', '深圳');

-- 创建员工表
CREATE TABLE tb_emp
(
eno INT NOT NULL COMMENT '员工编号',
ename VARCHAR(20) NOT NULL COMMENT '员工名字',
job VARCHAR(20) NOT NULL COMMENT '员工职位',
mgr int COMMENT '主管编号',
sal int NOT NULL COMMENT '员工月薪',
comn int COMMENT '员工补贴',
dno INT NOT NULL COMMENT '所在部门编号',
PRIMARY KEY (eno),
CONSTRAINT fk_emp_mgr FOREIGN KEY (mgr) REFERENCES tb_emp (eno),
CONSTRAINT fk_emp_dno FOREIGN KEY (dno) REFERENCES tb_dept (dno)
);

-- 插入14个员工
INSERT INTO tb_emp VALUES
    (7800, '张三丰', '总裁', null, 9000, 1200, 20),
    (2056, '乔峰', '分析师', 7800, 5000, 1500, 20),
    (3088, '李莫愁', '设计师', 2056, 3500, 800, 20),
    (3211, '张无忌', '程序员', 2056, 3200, null, 20),
    (3233, '丘处机', '程序员', 2056, 3400, null, 20),
    (3251, '张翠山', '程序员', 2056, 4000, null, 20),
    (5566, '宋远桥', '会计师', 7800, 4000, 1000, 10),
    (5234, '郭靖', '出纳', 5566, 2000, null, 10),
    (3344, '黄蓉', '销售主管', 7800, 3000, 800, 30),
    (1359, '胡一刀', '销售员', 3344, 1800, 200, 30),
    (4466, '苗人凤', '销售员', 3344, 2500, null, 30),
    (3244, '欧阳锋', '程序员', 3088, 3200, null, 20),
    (3577, '杨过', '会计', 5566, 2200, null, 10),
    (3588, '朱九真', '会计', 5566, 2500, null, 10);

	-- 查询按月薪从高到低排在第4到第6名的员工的姓名和月薪。
	SELECT ename, sal, ROW_NUMBER() over (ORDER BY sal desc) as `rank` FROM tb_emp;
	SELECT * FROM (SELECT ename, sal, ROW_NUMBER() over (ORDER BY sal desc) as `rank` FROM tb_emp)
	temp WHERE `rank` BETWEEN 4 and 6;

	-- 在MySQL 8以前的版本，我们可以通过下面的方式来完成类似的操作
	select `rank`, `ename`, `sal` from (
    select @a:=@a+1 as `rank`, `ename`, `sal`
    from `tb_emp`, (select @a:=0) as t1 order by `sal` desc
) t2 where `rank` between 4 and 6;

-- 例子2：查询每个部门月薪最高的两名的员工的姓名和部门名称。
	SELECT ename, sal, dno, RANK() over (PARTITION by dno ORDER BY sal desc) as `rank` FROM tb_emp;
	SELECT ename, sal, dname FROM (	SELECT ename, sal, dno, RANK() over (PARTITION by dno ORDER BY sal desc) as `rank` FROM tb_emp)
	as temp NATURAL JOIN tb_dept WHERE `rank` <= 2;
