### mysql中文乱码解决方案：
1、use names gbk;

### mysql 登录
1、mysql -u user -p 
2、输入密码

### 导入文件
load data local infile file_name into table table_name character set utf8 FIELDS TERMINATED BY ',';

### 删除表格
delete from table_name;

### 删除表
drop table table_name;


