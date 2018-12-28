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
            print sql
            print ("Error: unable to insert data")
            self.conn.rollback


    #获取病情描述数据
    def get_words(self):
        sql = """ 
SELECT f_uuid
,f_msg_content AS f_msg_content
,f_doctor_dep
FROM t_easyhin_fact_inquiry_record a
LEFT JOIN t_easyhin_dim_doctor b ON a.f_doctor_id = b.id
WHERE  f_uuid != '' 
AND f_type !=4 AND f_msg_content !='' 
AND f_crt_time>='2018-01-01'
GROUP BY f_uuid
         """
        #print sql
        return self.jdbc(sql);

    #获取医生回复数据
    def get_doctor_reply(self):
        sql = """
SELECT 
a.f_uuid
,a.f_msg_content AS f_msg_content
,c.f_doctor_dep 
FROM t_easyhin_dim_app_records a 
LEFT JOIN t_easyhin_fact_inquiry_record b ON a.f_uuid=b.f_uuid
LEFT JOIN t_easyhin_dim_doctor c ON b.f_doctor_id = c.id
WHERE b.f_crt_time>='2018-01-01'
AND c.f_doctor_dep = '小儿皮肤科'
AND a.f_msg_direct =1
AND a.f_msg_type = 1
"""
        return self.jdbc(sql);

    def inser_words(self,f_order_id,word,cnt,dep):
        sql = "INSERT t_order_fenci(f_order_id,f_wd,f_cnt,f_dep) VALUES('%s','%s','%s','%s')"%(f_order_id,word,cnt,dep)
        #print sql
        return self.insert(sql);

    def insert_sql(self,sql):
        return self.insert(sql);



if __name__ == "__main__":
    rd=ReportData()
    #rs=rd.get_ktr_by_name("test111111111111111111111111111111111111111111111")
    #rs = rd.get_ker_by_id("1,2")
    rs = rd.get_words()
    print rs

