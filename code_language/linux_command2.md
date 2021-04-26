@[TOC](linux命令之md5sum)
## `md5sum`
查看文件的md5值，用来比较两个文件是否相同。可以应用于文件传输、文件校验等等。
使用方法：
```
Usage: md5sum [OPTION]... [FILE]...
Print or check MD5 (128-bit) checksums.

With no FILE, or when FILE is -, read standard input.

  -b, --binary         read in binary mode (default unless reading tty stdin)
  -c, --check          read MD5 sums from the FILEs and check them
      --tag            create a BSD-style checksum
  -t, --text           read in text mode (default if reading tty stdin)
  -z, --zero           end each output line with NUL, not newline,
                       and disable file name escaping

The following five options are useful only when verifying checksums:
      --ignore-missing  don't fail or report status for missing files
      --quiet          don't print OK for each successfully verified file
      --status         don't output anything, status code shows success
      --strict         exit non-zero for improperly formatted checksum lines
  -w, --warn           warn about improperly formatted checksum lines

      --help     display this help and exit
      --version  output version information and exit

```
### md5校验
```
md5sum * > md5.txt
md5sum -c md5.txt
```

### 类似的命令
```
sha1sum
sha224sum
sha256sum
sha384sum
sha512sum
```
参考网址:[https://www.cnblogs.com/zhuxiaohou110908/p/5786893.html](https://www.cnblogs.com/zhuxiaohou110908/p/5786893.html)



