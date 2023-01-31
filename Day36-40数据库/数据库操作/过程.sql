-- 创建过程
DROP PROCEDURE if EXISTS sp_score_stat;

delimiter $$

CREATE PROCEDURE sp_score_stat(
		courseId int,
		OUT maxScore DECIMAL(4, 1),
		OUT minScore DECIMAL(4, 1),
		OUT avgScore DECIMAL(4, 1)
)
BEGIN
		SELECT max(score) INTO maxScore FROM tb_record WHERE cou_id=courseId;
		SELECT min(score) INTO minScore FROM tb_record WHERE cou_id=courseId;
		SELECT avg(score) INTO avgScore FROM tb_record WHERE cou_id=courseId;
END $$

delimiter ;

-- 调用过程
call sp_score_stat(1111, @a, @b, @c);

-- 获取输出参数的值
SELECT @a AS 最高分, @b AS 最低分, @c AS 平均分;

-- 删除过程
DROP PROCEDURE sp_score_stat;