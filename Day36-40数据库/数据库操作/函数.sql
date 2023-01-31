-- 自定义函数
-- 说明1：函数声明后面的no sql是声明函数体并没有使用 SQL 语句；如果函数体中需要通过 SQL 读取数据，需要声明为reads sql data。
-- 说明2：定义函数前后的delimiter命令是为了修改定界符，因为函数体中的语句都是用;表示结束，如果不重新定义定界符，那么遇到的;的时候代码就会被截断执行，显然这不是我们想要的效果。

delimiter $$

CREATE FUNCTION truncate_string(
	content VARCHAR(10000),
	max_length INT UNSIGNED
) RETURNS VARCHAR(10000) no SQL
BEGIN
		DECLARE result VARCHAR(10000) DEFAULT content;
		if CHAR_LENGTH(content) > max_length THEN
			set result = LEFT(content,max_length);
			set result = CONCAT(result,'......');
		END if;
		RETURN result;
	END $$

	delimiter ;

	-- 调用自定义函数
	SELECT truncate_string('和我在成都的街头走一走，直到所有的灯都熄灭了也不停留', 10) as short_string;