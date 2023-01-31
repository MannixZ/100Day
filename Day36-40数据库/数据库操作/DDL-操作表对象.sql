-- 如果存在名为school的数据库就删除它
DROP DATABASE
IF
	EXISTS `scheool`;

	-- 创建名为school的数据库并设置默认的字符集和排序方式
CREATE DATABASE `school` DEFAULT CHARACTER
SET utf8mb4 COLLATE utf8mb4_general_ci;

-- 切换到school数据库上下文环境
USE `school`;

-- 创建学院表
CREATE TABLE `tb_college` (
	`col_id` INT UNSIGNED auto_increment COMMENT '编号',
	`col_name` VARCHAR ( 50 ) NOT NULL COMMENT '名称',
	`col_intro` VARCHAR ( 500 ) DEFAULT '' COMMENT '介绍',
	PRIMARY KEY ( `col_id` )
) ENGINE = INNODB auto_increment = 1 COMMENT '学院表';

-- 创建学生表
CREATE TABLE `tb_student` (
	`stu_id` INT UNSIGNED NOT NULL COMMENT '学号',
	`stu_name` VARCHAR ( 20 ) NOT NULL COMMENT '姓名',
	`stu_sex` boolean DEFAULT 1 NOT NULL COMMENT '性别',
	`stu_birth` date NOT NULL COMMENT '出生日期',
	`stu_addr` VARCHAR ( 255 ) DEFAULT '' COMMENT '籍贯',
	`col_id` INT UNSIGNED NOT NULL COMMENT '所属学院',
	PRIMARY KEY ( `stu_id` ),
	CONSTRAINT `fk_student_col_id` FOREIGN KEY ( `col_id` ) REFERENCES `tb_college` ( `col_id` )
) ENGINE = INNODB COMMENT '学生表';

-- 创建教师表
CREATE TABLE `tb_teacher` (
	`tea_id` INT UNSIGNED NOT NULL COMMENT '工号',
	`tea_name` VARCHAR ( 20 ) NOT NULL COMMENT '姓名',
	`tea_title` VARCHAR ( 10 ) DEFAULT '助教' COMMENT '职称',
	`col_id` INT UNSIGNED NOT NULL COMMENT '所属学院',
	PRIMARY KEY ( `tea_id` ),
	CONSTRAINT `fk_teacher_col_id` FOREIGN KEY ( `col_id` ) REFERENCES `tb_college` ( `col_id` )
) ENGINE = INNODB COMMENT '老师表';

-- 创建课程表
CREATE TABLE `tb_course` (
	`cou_id` INT UNSIGNED NOT NULL COMMENT '编号',
	`cou_name` VARCHAR ( 50 ) NOT NULL COMMENT '名称',
	`cou_credit` INT NOT NULL COMMENT '学分',
	`tea_id` INT UNSIGNED NOT NULL COMMENT '授课老师',
	PRIMARY KEY ( `cou_id` ),
	CONSTRAINT `fk_course_tea_id` FOREIGN KEY ( `tea_id` ) REFERENCES `tb_teacher` ( `tea_id` )
) ENGINE = INNODB COMMENT '课程表';

-- 创建选课记录
CREATE TABLE `tb_record` (
	`rec_id` BIGINT UNSIGNED auto_increment COMMENT '选课记录号',
	`stu_id` INT UNSIGNED NOT NULL COMMENT '学号',
	`cou_id` INT UNSIGNED NOT NULL COMMENT '课程标号',
	`sel_date` date NOT NULL COMMENT '选课日期',
	`score` DECIMAL ( 4, 1 ) COMMENT '考试成绩',
	PRIMARY KEY ( `rec_id` ),
	CONSTRAINT `fk_record_stu_id` FOREIGN KEY ( `stu_id` ) REFERENCES `tb_student` ( `stu_id` ),
	CONSTRAINT `fk_record_cou_id` FOREIGN KEY ( `cou_id` ) REFERENCES `tb_course` ( `cou_id` ),
	CONSTRAINT `uk_record_stu_cou` UNIQUE ( `stu_id`, `cou_id` )
) ENGINE = INNODB COMMENT '选课记录表';

-- 修改选课记录表，去掉 stu_id 列的外键约束
alter table `tb_record` drop foreign key `fk_record_stu_id`;
