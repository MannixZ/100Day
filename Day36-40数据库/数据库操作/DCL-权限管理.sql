-- 创建名为 wangdachui 的账号并为其指定口令，允许该账号从任意主机访问
CREATE USER 'wangdachui'@'%' IDENTIFIED by '123456';

-- 授权 wangdachui 可以对名为school的数据库执行 select 和 insert 操作
GRANT SELECT, INSERT on school.* to 'wangdachui'@'%';

-- 召回 wangdachui 对school数据库的 insert 权限
REVOKE INSERT on school.* FROM 'wangdachui'@'%';