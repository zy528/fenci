#coding=utf-8
import MySQLdb

class ReportData:  
    def __init__(self):  

        self.conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='welcome123',
            db='d_easyhin_stat_ret',
            charset="utf8",
        )
    def changeDB(self,dbname):
        if dbname=='d_easyhin_card_center':
            self.conn.close()
            self.conn = MySQLdb.connect(
                host='localhost',
                port=3306,
                user='root',
                passwd='welcome123',
                db='d_easyhin_card_center',
                charset="utf8",
            )
        return 'change db to %s successfully' %(dbname)
    def __del__(self):
	    self.conn.close()

    def jdbc(self,sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            results = cursor.fetchall()
            #print cursor.description
            cursor.close()
            return results
        except:
            print("Error: unable to fecth data")

    def update(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return True
        except:
            print("Error: unable to update data")
            self.conn.rollback

    def insert(self, sql):
        cursor = self.conn.cursor()
        try:
            cursor.execute(sql)
            self.conn.commit()
            cursor.close()
            return True
        except:
            print ("Error: unable to insert data")
            self.conn.rollback


    #获取订单数据
    def get_words(self):
        sql = """ 
            SELECT f_order_id,f_msg_content AS f_msg_content
FROM t_easyhin_fact_inquiry_record WHERE  f_order_id != '' AND f_type !=4 AND f_msg_content !='' 
AND f_crt_time>='2018-01-01'
 GROUP BY f_order_id
         """
        #print sql
        return self.jdbc(sql);
    def inser_words(self,f_order_id,words):
        sql = "INSERT t_order_fenci(f_order_id,f_wd) VALUES('%s','%s')"%(f_order_id,words)
        #print sql
        return self.insert(sql);



if __name__ == "__main__":
    rd=ReportData()
    #rs=rd.get_ktr_by_name("test111111111111111111111111111111111111111111111")
    #rs = rd.get_ker_by_id("1,2")
    rs = rd.get_words()
    print rs

