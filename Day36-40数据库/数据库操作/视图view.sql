-- 创建视图, 使用 or REPLACE 字段，保证视图每次都能被更新
CREATE or REPLACE VIEW vm_avg_score
AS
SELECT stu_id, ROUND(avg(score), 1) as avg_score FROM tb_record GROUP BY stu_id;

-- 基于已有的视图创建视图
CREATE VIEW vm_student_score
AS
SELECT stu_name, avg_score FROM tb_student NATURAL JOIN vm_avg_score;

-- 使用视图
SELECT * FROM vm_student_score ORDER BY avg_score DESC;

-- 删除视图
DROP VIEW vm_avg_score;

