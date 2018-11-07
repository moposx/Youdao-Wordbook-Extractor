# Youdao-Wordbook-Extractor

这个脚本用来提取有道词典或者有道背单词的单词本数据。

## Usage
克隆到本地之后，进入对应的目录，执行：
```
python3 app.py PATH-TO-YOUR-WORDBOOK-DB
```
完成后即可获取到排序过的词单，位于：`out/output.txt`

## Q&A
- 如何得到单词本数据库？
> 截止到当前版本（有道背单词 v1.5.3, 有道词典v7.8.0)，脚本都能正常提取。
> 数据库文件的路径在： 
>`/data/data/com.youdao.reciteword/databases/wordbook`（有道背单词）
> `/data/data/com.youdao.dict/databases/notes.db`（有道词典）

## How does it work
使用`file`指令：
```shell-source
file ./notes.db
```
```output
./notes.db: SQLite 3.x database, user version 7, last written using SQLite version 3019004
```

可以看出这个数据库是SQLite写成的。打开数据库发现这个数据库有很多张表，而单词存储在`notes`表中，这张表里面包含很多信息，包括单词的拼写，简单释义和音标等。这样通过操作对应的项目便可取得对应的数据。

PS: 我最初的想法是只取得英文单词，方便未来一键导入别的背单词app，但是后来发现也需要保留别的单词，于是移除了筛选。 