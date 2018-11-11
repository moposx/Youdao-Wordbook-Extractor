# Youdao-Wordbook-Extractor

这个脚本用来提取有道词典或者有道背单词的单词本数据。

## Usage
克隆到本地之后，进入对应的目录，执行：
```
python3 app.py PATH-TO-YOUR-WORDBOOK-DB
```
完成后即可获取到排序过的词单，位于：`out/output.txt`

## Q&A
- 如何得到单词本数据库?  

截止到当前版本（有道背单词 v1.5.3, 有道词典v7.8.0)，脚本都能正常提取。
数据库文件的路径在： 
`/data/data/com.youdao.dict/databases/notes.db`（有道词典）  
`/data/data/com.youdao.reciteword/databases/wordbook`（有道背单词）  
N.B. 有道背单词如果想获取官方词单，需要曾经背过/切换到过该此书（应该是这样，因为我在我的数据库里面发现许多`NULL`值，是属于我没有背过的词书）


## How does it work
[See here](https://moposx.tk/2018/11/08/youdao-wordbook-extractor/)

## Disclaimer
本脚本**仅供交流学习之用**，请遵守相应的法律法规。对于不当使用本脚本产生的不良后果，作者**不承担**任何责任。
对于未提及之事项，作者**保留解释权**。