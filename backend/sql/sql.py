# -*- coding: utf-8 -*-
# @Time : 2022/3/11 18:20
# @Author : suanzi
# @Site : 
# @File : sql.py
# @Software: PyCharm
import pymysql


class sqlDAO:
    def __init__(self):
        self.conn = pymysql.connect(host='114.116.79.120', user='root', password='suanzi', database='zaozao',
                                    charset='utf8')
        # self.conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='zaozao',
        #                             charset='utf8')
        self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)

    def __del__(self):
        # 关闭游标
        self.cursor.close()
        # 关闭连接
        self.conn.close()

    # 登录验证查询
    def login(self, username, password):
        sql = "select * from user where username = %s "
        num = self.cursor.execute(sql, username)
        if (num != 0):
            result = self.cursor.fetchall()
            if result[0].get('password') == password:
                return {
                    "status": 1,
                    "name": result[0].get('name')
                }  # 登录成功
            else:
                return {
                    "status": 0
                }  # 密码错误
        else:
            return {"status": -1}  # 查无此人

    # 注册
    def register(self, name, username, password):
        sql = "insert into user (name,username,password) values(%s,%s,%s)"
        try:
            num = self.cursor.execute(sql, (name, username, password))
            self.conn.commit()
            if (num != 0):
                return 1  # 添加成功
            else:
                return -1  # 添加失败
        except Exception:
            self.conn.rollback()

    # 查询评论
    def comment(self):
        sql = "select * from comment order by id"
        num = self.cursor.execute(sql)
        if (num != 0):
            data = self.cursor.fetchall()
            return {
                "status": 1,
                "comments": data
            }  # 查询所有数据
        else:
            return {
                "status": 0,
            }  # 数据库无数据

    # 插入评论
    def insert_comment(self, name, comment, time=''):
        sql = "insert into comment (name,comments,time) values(%s,%s,%s)"
        try:
            num = self.cursor.execute(sql, (name, comment, time))
            self.conn.commit()
            if (num != 0):
                return 1  # 添加成功
            else:
                return -1  # 添加失败
        except Exception:
            self.conn.rollback()

    # 删除
    def delete_comment(self, id, name):
        # 验证身份
        sql = "delete from comment where id = %s and name = %s"
        try:
            num = self.cursor.execute(sql, (id, name))
            self.conn.commit()
            if (num != 0):
                return 1  # 删除成功
            else:
                return -1  # 删除失败
        except Exception:
            self.conn.rollback()

    # 查询文章
    def getarticle(self, limit=False):
        if limit:
            sql = "select * from article limit 0,5"
        else:
            sql = "select * from article "

        num = self.cursor.execute(sql)
        if (num != 0):
            result = self.cursor.fetchall()
            return {"status": 1, "data": result}
        else:
            return {"status": -1}  # 无内容

    # 增加订单
    def addorder(self, name, region, date, time, type, resource, miaoshu,activename):
        sql = "insert into dingdan (name,activename,date,miaoshu,region,resource,time,type) values(%s,%s,%s,%s,%s,%s,%s,%s)"
        try:
            num = self.cursor.execute(sql, (name,activename, date, miaoshu, region, resource, time, type))
            self.conn.commit()
            if (num != 0):
                return 1  # 添加成功
            else:
                return -1  # 添加失败
        except Exception:
            self.conn.rollback()

    # 查询订单
    def get_order(self,name):
        sql = "select * from dingdan where name = %s order by id"
        num = self.cursor.execute(sql,(name))
        if (num != 0):
            data = self.cursor.fetchall()
            return {
                "status": 1,
                "order": data
            }  # 查询所有数据
        else:
            return {
                "status": 0,
            }  # 数据库无数据
