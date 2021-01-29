linux命令
1、文件浏览命令
格式： 命令 [option] file
(1)cat  由第一行开始显示文件内容 
(2)tac  从最后一行开始显示，tac 是 cat 的倒写
(3)nl   显示行号
(4)more  一页一页的显示文件内容
(5)less  more 类似，但他可以往前翻页
(6)head  看头几行
(7)tail  看尾部几行
(8)od  以二进制的方式读取文件内容
2、文件目录操作命令
(1)mkdir
(2)rm
(3)mv
(4)ls
(5)tar,gzip,bzip2,compress,rar,zip

3、文件查找命令
(1)find
(2)which
(3)whereis
(4)locate
4、文件权限设置命令
(1)chmod
(2)chgrp
(3)chown
5、系统性能监控命令
(1)top  实时显示系统中各个进程的资源占用状况，常用于服务端性能分析。
(2)free  显示系统使用和空闲的内存情况
(3)vmstat  显示关于内核线程、虚拟内存、磁盘、陷阱和 CPU 活动的统计信息。
(4)iostat  统计系统的磁盘操作活动
(5)lsof  列出当前系统打开的文件
(6)ps  (Process Status)列出系统当前运行的进程。
6、网络查看命令
(1)ifconfig  获取或修改网络接口配置信息
(2)ip  用来显示或操纵Linux主机的路由、网络设备、策略路由和隧道。
(3)netstat  显示网络连接状态及其相关信息
(4)ss    (Socket Statistics) 用来获取socket统计信息[替换netstat]
(5)ping  用来测试与目标主机的连通性
(6)telnet  远程登录
(7)ssh  远程登录
(8)rcp  (remote file copy) 远程文件拷贝
(9)scp  (secure copy) 远程文件拷贝
(10)route   显示和操作IP路由表
(11) traceroute  检测发出数据包的主机到目标主机之间所经过的网关
7、其他命令
(1)grep 文本搜索
(2)wc 统计指定文件中的字节数、字数、行数
(3)watch  周期性执行命令/定时执行命令
(4)ln 文件链接
(5)make,rpm,dpkg,yum 编译命令
(6)awk
