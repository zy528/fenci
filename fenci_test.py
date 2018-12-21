# encoding: utf-8

import jieba
import jieba.posseg as psg
import io

from task_data_model import ReportData
import collections

rd = ReportData()


#读取过滤词语
def stopwordslist(filepath):
 stopwords = [line.strip() for line in io.open(filepath, 'r', encoding='utf-8').readlines()]
 return stopwords


def fenci():
 stopwords = stopwordslist(r'C:\Users\Administrator\Desktop\python\fenci\stopwords.txt')
 #print stopwords
 orders = rd.get_words()
 for order in orders:
  word = order[1]
  result_list = psg.cut(word)
  rusult = []
  for x in result_list:
   if x.word not in stopwords and x.word.strip() != '':
    #print x.word
     rusult.append(x.word)
  #统计词频
  mycount = collections.Counter(rusult)
  words = ''
  for k,v in mycount.items():
   words += (k+':'+str(v))+','
  #print words
  rd.inser_words(order[0],words)


if __name__ == "__main__":
 fenci()














