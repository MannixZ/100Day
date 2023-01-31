-- 创建有 json 字段类型的列

CREATE table tb_test
(
user_id BIGINT UNSIGNED,
login_info json,
PRIMARY KEY (user_id)
) ENGINE=INNODB;

-- 插入数据
INSERT INTO tb_test VALUES
    (1, '{"tel": "13122335566", "QQ": "654321", "wechat": "jackfrued"}'),
    (2, '{"tel": "13599876543", "weibo": "wangdachui123"}');

# 查询用户的手机号和微信号
SELECT
	user_id,
	JSON_UNQUOTE(
	JSON_EXTRACT( login_info, '$.tel' )) AS 手机号,
	JSON_UNQUOTE(
	JSON_EXTRACT( login_info, '$.wechat' )) AS 微信
FROM
	tb_test;
-- 方法二
SELECT user_id, login_info ->> '$.tel' as 手机号, login_info ->> '$.wechat' AS 微信 FROM tb_test;

############# 用户画像 json 操作例子

-- 创建画像标签表
create table `tb_tags`
(
`tag_id` int unsigned not null comment '标签ID',
`tag_name` varchar(20) not null comment '标签名',
primary key (`tag_id`)
) engine=innodb;

insert into `tb_tags`
values
    (1, '70后'),
    (2, '80后'),
    (3, '90后'),
    (4, '00后'),
    (5, '爱运动'),
    (6, '高学历'),
    (7, '小资'),
    (8, '有房'),
    (9, '有车'),
    (10, '爱看电影'),
    (11, '爱网购'),
    (12, '常点外卖');

-- 为用户打上标签
CREATE TABLE if not EXISTS tb_users_tags(
user_id BIGINT UNSIGNED not NULL COMMENT '用户ID',
user_tags json not NULL COMMENT '用户标签'
)ENGINE=INNODB;

INSERT INTO tb_users_tags VALUES
(1, '[2, 6, 8, 10]'),
    (2, '[3, 10, 12]'),
    (3, '[3, 8, 9, 11]');

-- 查询爱看电影（有10这个标签）的用户ID。
SELECT * FROM tb_users_tags WHERE 10 member of (user_tags->'$');

-- 查询爱看电影（有10这个标签）的80后（有2这个标签）用户ID。
SELECT * FROM tb_users_tags WHERE 10 AND 2 member of (user_tags->'$');

SELECT * FROM tb_users_tags WHERE JSON_CONTAINS(user_tags->'$', '[2, 10]');

-- 查询爱看电影或80后或90后的用户ID。
SELECT * FROM tb_users_tags WHERE json_overlaps(user_tags->'$', '[2, 3, 10]');
