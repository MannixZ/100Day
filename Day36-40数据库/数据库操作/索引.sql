EXPLAIN SELECT * FROM tb_student WHERE stu_name='杨过';

-- 创建索引
CREATE INDEX idx_stu_name on tb_student(stu_name);

-- 创建对索引字段前N个字符的索引-前缀索引
CREATE INDEX idx_stu_name_1 on tb_student(stu_name(1));

-- 删除索引
DROP INDEX idx_stu_name on tb_student;
ALTER TABLE tb_student DROP INDEX idx_stu_name;
