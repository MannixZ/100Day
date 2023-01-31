-- 查询所有学生的所有信息
SELECT * FROM `tb_student`;

-- 查询学生的学号、姓名和籍贯（投影）
SELECT `stu_id`, `stu_name`, `stu_addr` FROM `tb_student`;

-- 查询所有课程的名称及学分（投影和别名）
SELECT `cou_name` as 课程名称, `cou_credit` as 学分 FROM `tb_course`;

-- 查询所有女学生的姓名和出生日期（筛选）
SELECT `stu_name`, `stu_birth` FROM `tb_student` WHERE `stu_sex`=0;

-- 查询籍贯为“四川成都”的女学生的姓名和出生日期(筛选)
SELECT `stu_name`, `stu_birth` FROM `tb_student` WHERE `stu_addr`='四川成都' AND `stu_sex`=0;

-- 查询籍贯为“四川成都”或者性别为“女生”的学生
SELECT * FROM `tb_student` WHERE `stu_addr`='四川成都' or stu_sex=0;

-- 查询所有大于80，小于90后的学生的姓名、性别和出生日期(筛选) 方法一
SELECT `stu_name`, `stu_sex`, `stu_birth` FROM `tb_student` WHERE `stu_birth` >= '1980-01-01' AND `stu_birth` <= '1989-12-31';

-- 查询所有大于80，小于90后的学生的姓名、性别和出生日期(筛选) 方法二
SELECT `stu_name`, `stu_sex`, `stu_birth` FROM `tb_student` WHERE `stu_birth` BETWEEN '1980-01-01' AND '1989-12-31';

-- 补充：将表示性别的 1 和 0 的学生处理成 “男” 和 “女” 方法一
SELECT `stu_name` as '姓名',
if(`stu_sex`, '草莓', '苹果') as '性别',
`stu_birth` as '出生日期'
FROM `tb_student`
WHERE `stu_birth` BETWEEN '1980-01-01' AND '1989-12-31' ;

-- 补充：将表示性别的 1 和 0 的学生处理成 “男” 和 “女” 方法二
SELECT `stu_name` as '姓名',
CASE `stu_sex`
	WHEN 1 THEN
		'男'
	ELSE
		'女'
END as '性别',
`stu_birth` as '出生日期'
FROM `tb_student`
WHERE `stu_birth` BETWEEN '1980-01-01' AND '1989-12-31' ;

-- 查询学分大于2的课程的名称和学分(筛选)
SELECT cou_name, cou_credit FROM tb_course WHERE cou_credit > 2;

-- 查询学分是奇数的课程的名称和学分(筛选)
SELECT cou_name, cou_credit FROM tb_course WHERE cou_credit % 2 <> 0;

SELECT cou_name, cou_credit FROM tb_course WHERE cou_credit % 2 != 0;

SELECT cou_name, cou_credit FROM tb_course WHERE cou_credit MOD 2 <> 0;

-- 查询选择选了1111的课程考试成绩在90分以上的学生学号(筛选)
SELECT stu_id FROM tb_record WHERE cou_id=1111 AND score>90;

-- 查询名字叫“杨过”的学生的姓名和性别
SELECT stu_name, stu_sex FROM tb_student WHERE stu_name='杨过';

-- 查询姓“杨”的学生姓名和性别(模糊)
-- % - 通配符（wildcard），它可以匹配0个或任意多个字符
SELECT stu_name, stu_sex FROM tb_student WHERE stu_name LIKE '杨%';

-- 查询姓“杨”名字两个字的学生姓名和性别(模糊)
-- _ - 通配符（wildcard），它可以精确匹配一个字符
SELECT stu_name, stu_sex FROM tb_student WHERE stu_name LIKE '杨_';

-- 查询姓“杨”名字三个字的学生姓名和性别(模糊)
SELECT stu_name, stu_sex FROM tb_student WHERE stu_name LIKE '杨__';

-- 查询名字中有“不”字或“嫣”字的学生的姓名(模糊)
SELECT stu_name, stu_sex FROM tb_student WHERE stu_name LIKE '%不%' OR stu_name LIKE '%嫣%';

-- 比较下面两个查询的区别
select `stu_name` from `tb_student` where `stu_name` like '%不%'
union
select `stu_name` from `tb_student` where `stu_name` like '%嫣%';

-- union all 会出现2个 岳不嫣, 岳不嫣 是被修改过的，就是说被修改过的记录也会显示在结果中
select `stu_name` from `tb_student` where `stu_name` like '%不%'
union all
select `stu_name` from `tb_student` where `stu_name` like '%嫣%';

-- 查询姓“杨”或姓“林”名字三个字的学生的姓名(正则表达式模糊查询)
SELECT stu_name FROM tb_student WHERE stu_name REGEXP '[杨林].{2}';

-- 查询没有录入籍贯的学生姓名(空值处理)
SELECT stu_name FROM tb_student WHERE stu_addr is NULL;

select `stu_name` from `tb_student` where `stu_addr` <=> null;

-- 查询录入了籍贯的学生姓名(空值处理)
SELECT stu_name FROM tb_student WHERE stu_addr is NOT NULL;

-- 下面的查询什么也查不到，三值逻辑 --> true / false / unknown
SELECT stu_name FROM tb_student WHERE stu_addr = NULL OR stu_addr <> NULL;

-- 查询学生选课的所有日期(去重)
SELECT DISTINCT sel_date FROM tb_record;

-- 查询学生的籍贯(去重)
SELECT DISTINCT stu_addr FROM tb_student WHERE stu_addr is NOT NULL;

-- 查询男学生的姓名和生日按年龄从大到小排列(排序)
-- 升序：从小到大 - asc，降序：从大到小 - desc
SELECT stu_id, stu_name, stu_birth FROM tb_student WHERE stu_sex=1 ORDER BY stu_birth ASC;

SELECT stu_id, stu_name, stu_birth FROM tb_student WHERE stu_sex=1 ORDER BY stu_birth ASC, stu_id DESC;

-- 补充：将上面的生日换算成年龄(日期函数、数值函数)
SELECT
	stu_id AS 学号,
	stu_name as 姓名,
	FLOOR(
	DATEDIFF( CURDATE(), stu_birth) / 365 ) as 年龄
FROM
	tb_student
WHERE
	stu_sex = 1
ORDER BY
	年龄 DESC;

-- 查询年龄最大的学生的出生日期(聚合函数)
SELECT MIN(stu_birth) FROM tb_student;

-- 查询年龄最小的学生的出生日期(聚合函数)
SELECT MAX(stu_birth) FROM tb_student;

-- 查询编号为1111的课程考试成绩的最高分(聚合函数)
SELECT MAX(score) FROM tb_record WHERE cou_id=1111;

-- 查询学号为1001的学生考试成绩的最低分(聚合函数)
SELECT MIN(score) FROM tb_record WHERE stu_id=1001;

-- 查询学号为1001的学生考试成绩的平均分(聚合函数)
SELECT AVG(score) FROM tb_record WHERE stu_id=1001;

select sum(`score`) / count(`score`) from `tb_record` where `stu_id`=1001;

-- 查询学号为1001的学生考试成绩的平均分，如果有null值，null值算0分(聚合函数)
-- COUNT(*) 和  count(`score`)  的区别是， * 不会算上Null 的值，score 会
SELECT SUM(score) / COUNT(*) FROM tb_record WHERE stu_id=1001;

SELECT AVG(IFNULL(score,0)) FROM tb_record WHERE stu_id=1001;

-- 查询学号为1001的学生考试成绩的标准差(聚合函数)
SELECT STD(score), VARIANCE(score) FROM tb_record WHERE stu_id=1001;

-- 查询男女学生的人数(分组和聚合函数)
SELECT CASE stu_sex
	WHEN 1 THEN
		'男'
	ELSE
		'女'
END AS '性别',
COUNT(*) as 人数
 FROM tb_student GROUP BY stu_sex;

 -- 查询每个学院学生人数(分组和聚合函数)
SELECT
	col_id as '学院',
	COUNT(*) AS '人数'
 FROM tb_student GROUP BY col_id;

 -- 查询每个学院男女学生人数(分组和聚合函数)
SELECT
	col_id AS 学院,
IF
	( stu_sex, '男', '女' ) AS 性别,
	COUNT(*) AS 人数
FROM
	tb_student
GROUP BY
	stu_sex,
	col_id;

-- 查询每个学生的学号和平均成绩(分组和聚合函数)
SELECT stu_id, ROUND(AVG(score), 1) as avg_score FROM tb_record GROUP BY stu_id;

-- 查询平均成绩大于等于90分的学生的学号和平均成绩
-- 分组以前的筛选使用where子句，分组以后的筛选使用having子句
SELECT stu_id, ROUND(AVG(score), 1) as avg_score FROM tb_record GROUP BY stu_id HAVING avg_score >= 90;

-- 查询1111、2222、3333三门课程平均成绩大于等于90分的学生的学号和平均成绩
SELECT stu_id, ROUND(AVG(score), 1) AS avg_score FROM tb_record WHERE cou_id IN (1111, 2222, 3333) GROUP BY stu_id HAVING avg_score >= 90;

-- 查询年龄最大的学生的姓名(子查询/嵌套查询)
-- 嵌套查询：把一个select的结果作为另一个select的一部分来使用
SELECT stu_name, stu_birth FROM tb_student WHERE stu_birth=(SELECT MIN(stu_birth) FROM tb_student);

-- 查询选了两门以上的课程的学生姓名(子查询/分组条件/集合运算)
SELECT stu_id, stu_name FROM tb_student WHERE stu_id in (SELECT stu_id FROM tb_record GROUP BY stu_id HAVING COUNT(*) > 2);

-- 查询学生的姓名、生日和所在学院名称
SELECT stu_name, stu_birth, col_name FROM tb_student, tb_college WHERE tb_student.col_id=tb_college.col_id;

SELECT stu_name, stu_birth, col_name FROM tb_student INNER JOIN tb_college on tb_student.col_id = tb_college.col_id;

SELECT stu_name, stu_birth, col_name FROM tb_student NATURAL JOIN tb_college;

-- 查询学生姓名、课程名称以及成绩(连接查询/联结查询)
SELECT stu_name, col_name, score FROM tb_student, tb_college, tb_record WHERE
tb_student.col_id=tb_college.col_id AND
tb_student.stu_id=tb_record.stu_id AND score IS NOT NULL;

SELECT stu_name, col_name, score FROM tb_student NATURAL JOIN tb_college NATURAL JOIN tb_record WHERE score is NOT NULL;

SELECT stu_name, col_name, score FROM tb_student INNER JOIN tb_college ON tb_student.col_id = tb_college.col_id INNER JOIN
tb_record ON tb_student.stu_id = tb_record.stu_id WHERE score is not NULL

-- 补充：上面的查询结果取前5条数据(分页查询)
SELECT
	stu_name,
	col_name,
	score
FROM
	tb_student,
	tb_college,
	tb_record
WHERE
	tb_student.col_id = tb_college.col_id
AND
	tb_student.stu_id = tb_record.stu_id
AND
	score is NOT NULL
ORDER BY
	score DESC
LIMIT 0,5;

-- 补充：上面的查询结果取第6-10条数据(分页查询)
SELECT
	stu_name,
	col_name,
	score
FROM
	tb_student,
	tb_college,
	tb_record
WHERE
	tb_student.col_id = tb_college.col_id
AND
	tb_student.stu_id = tb_record.stu_id
AND
	score is NOT NULL
ORDER BY
	score DESC
LIMIT 5 OFFSET 5;

-- 补充：上面的查询结果取第11-15条数据(分页查询)
SELECT
	stu_name,
	col_name,
	score
FROM
	tb_student,
	tb_college,
	tb_record
WHERE
	tb_student.col_id = tb_college.col_id
AND
	tb_student.stu_id = tb_record.stu_id
AND
	score is NOT NULL
ORDER BY
	score DESC
LIMIT 5 OFFSET 10;

-- 查询选课学生的姓名和平均成绩(子查询和连接查询)
SELECT stu_id as sid, ROUND(AVG(score), 1) AS avg_score FROM tb_record GROUP BY stu_id;
SELECT stu_name, avg_score FROM tb_student INNER JOIN (SELECT stu_id as sid, ROUND(AVG(score), 1) AS avg_score FROM tb_record GROUP BY stu_id
) as t2 on stu_id=sid;

-- 查询学生的姓名和选课的数量
SELECT stu_id, COUNT(*) as total FROM tb_record GROUP BY stu_id;
SELECT stu_name, total FROM tb_student INNER JOIN (SELECT stu_id, COUNT(*) as total FROM tb_record GROUP BY stu_id) as t2 ON tb_student.stu_id=t2.stu_id;

-- 查询每个学生的姓名和选课数量(左外连接和子查询)
-- 左外连接：左表（写在join左边的表）的每条记录都可以查出来，不满足连表条件的地方填充null。
SELECT stu_name, COALESCE(total,0) FROM tb_student INNER JOIN (SELECT stu_id, COUNT(*) as total FROM tb_record GROUP BY stu_id) as t2 ON tb_student.stu_id=t2.stu_id;

-- 右外连接：右表（写在join右边的表）的每条记录都可以查出来，不满足连表条件的地方填充null。
SELECT stu_name, total FROM tb_student RIGHT OUTER JOIN (SELECT stu_id, COUNT(*) as total FROM tb_record GROUP BY stu_id) as t2 ON tb_student.stu_id=t2.stu_id;

-- 全外连接：左表和右表的每条记录都可以查出来，不满足连表条件的地方填充null。
-- 说明：MySQL不支持全外连接，所以用左外连接和右外连接的并集来表示。
SELECT stu_name, COALESCE(total,0) FROM tb_student INNER JOIN (SELECT stu_id, COUNT(*) as total FROM tb_record GROUP BY stu_id) as t2 ON tb_student.stu_id=t2.stu_id;
UNION
SELECT stu_name, total FROM tb_student RIGHT OUTER JOIN (SELECT stu_id, COUNT(*) as total FROM tb_record GROUP BY stu_id) as t2 ON tb_student.stu_id=t2.stu_id;