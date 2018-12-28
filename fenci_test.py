# encoding: utf-8

import jieba
import jieba.posseg as psg
import io

from task_data_model import ReportData
import collections

#读取过滤词语组装成数组
def stopwordslist(filepath):
 stopwords = [line.strip() for line in io.open(filepath, 'r', encoding='utf-8').readlines()]
 return stopwords


def fenci_deltial():
 #获取关键字过滤文件
 stopwords = stopwordslist(r'C:\Users\Administrator\Desktop\python\fenci\fenci\stopwords.txt')
 #stopwords = stopwordslist(r'/data/zy/fenci/stopwords.txt')

 #获取数据
 rd = ReportData()
 orders = rd.get_doctor_reply()

#遍历问诊对病情描述进行分词和词频统计
 for order in orders:
  word = order[1]
  result_list = psg.cut(word)
  rusult = []
  for x in result_list:
   if x.word not in stopwords and x.word.strip() != '':
     rusult.append(x.word)

  # 统计词频
  mycount = collections.Counter(rusult)

  # 拼接sql保存结果到数据库
  sql = "INSERT INTO t_doctor_reply_fenci(f_order_id,f_wd,f_cnt,f_dep) VALUES"
  if len(mycount.items()) !=0:
   #print mycount.items(),order
   for k, v in mycount.items():
    sql += "('" + order[0] + "','" + k + "','" + str(v) + "','" + order[2] + "'),"

   #print sql[:-1]
   rd.insert_sql(sql[:-1])

if __name__ == "__main__":
 fenci_deltial()














