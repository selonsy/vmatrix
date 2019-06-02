# _*_ encoding:utf-8 _*_
# _*_ author:wen _*_

import pymongo
from pymongo import MongoClient

class MG(object):
    def __init__(self):
        self.client = MongoClient("127.0.0.1", 27017)
        self.db = self.client["shenjinlong"]        

"""
mongodb_operation 静态方法，用来和 mongodb 操作交互 
"""
class BaseHandle(object):
    @staticmethod
    def insert_one(collection, data):
        """直接使用insert() 可以插入一条和插入多条 不推荐 明确区分比较好"""
        res = collection.insert_one(data)
        return res.inserted_id

    @staticmethod
    def insert_many(collection, data_list):
        res = collection.insert_many(data_list)
        return res.inserted_ids

    @staticmethod
    def find_one(collection, data, data_field={}):
        if len(data_field):
            res = collection.find_one(data, data_field)
        else:
            res = collection.find_one(data)
        return res

    @staticmethod
    def find_many(collection, data, data_field={}):
        """ data_field 是指输出 操作者需要的字段"""
        if len(data_field):
            res = collection.find(data, data_field)
        else:
            res = collection.find(data)
        return res

    @staticmethod
    def update_one(collection, data_condition, data_set):
        """修改一条数据"""
        res = collection.update_one(data_condition, data_set)
        return res

    @staticmethod
    def update_many(collection, data_condition, data_set):
        """ 修改多条数据 """
        res = collection.update_many(data_condition, data_set)
        return res

    @staticmethod
    def replace_one(collection, data_condition, data_set):
        """ 完全替换掉 这一条数据， 只是 _id 不变"""
        res = collection.replace_one(data_condition, data_set)
        return res

    @staticmethod
    def delete_many(collection, data):
        res = collection.delete_many(data)
        return res

    @staticmethod
    def delete_one(collection, data):
        res = collection.delete_one(data)
        return res


'''
mongodb_base 和 mongo 连接的信息 
'''
class DBBase(object):
    """ 各种query 中的数据 data 和 mongodb 文档中的一样"""

    def __init__(self, collection):
        self.mg = MG()
        self.collection = self.mg.db[collection]

    def insert_one(self, data):
        res = BaseHandle.insert_one(self.collection, data)
        return res

    def insert_many(self, data_list):
        res = BaseHandle.insert_many(self.collection, data_list)
        return res

    #  ========================= Query Documents Start =========

    def find_one(self, data, data_field={}):
        res = BaseHandle.find_one(self.collection, data, data_field)
        return res

    def find_many(self, data, data_field={}):
        """ 有多个键值的话就是 AND 的关系"""
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_all(self, data={}, data_field={}):
        """select * from table"""
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_in(self, field, item_list, data_field={}):
        """SELECT * FROM inventory WHERE status in ("A", "D")"""
        data = dict()
        data[field] = {"$in": item_list}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_or(self, data_list, data_field={}):
        """db.inventory.find(
        {"$or": [{"status": "A"}, {"qty": {"$lt": 30}}]})

        SELECT * FROM inventory WHERE status = "A" OR qty < 30
        """
        data = dict()
        data["$or"] = data_list
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_between(self, field, value1, value2, data_field={}):
        """获取俩个值中间的数据"""
        data = dict()
        data[field] = {"$gt": value1, "$lt": value2}
        # data[field] = {"$gte": value1, "$lte": value2} # <>   <= >=
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_more(self, field, value, data_field={}):
        data = dict()
        data[field] = {"$gt": value}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_less(self, field, value, data_field={}):
        data = dict()
        data[field] = {"$lt": value}
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def find_like(self, field, value, data_field={}):
        """ where key like "%audio% """
        data = dict()
        data[field] = {'$regex': '.*' + value + '.*'}
        print(data)
        res = BaseHandle.find_many(self.collection, data, data_field)
        return res

    def query_limit(self, query, num):
        """db.collection.find(<query>).limit(<number>) 获取指定数据"""
        res = query.limit(num)
        return res

    def query_count(self, query):
        res = query.count()
        return res

    def query_skip(self, query, num):
        res = query.skip(num)
        return res

    def query_sort(self, query, data):
        """db.orders.find().sort( { amount: -1 } ) 根据amount 降序排列"""
        res = query.sort(data)
        return res

    def delete_one(self, data):
        """ 删除单行数据 如果有多个 则删除第一个"""
        res = BaseHandle.delete_one(self.collection, data)
        return res

    def delete_many(self, data):
        """ 删除查到的多个数据 data 是一个字典 """
        res = BaseHandle.delete_many(self.collection, data)
        return res

class DBFinance(DBBase):
    def __init__(self):
        super(DBFinance, self).__init__("finance")

class DBNeiHan(DBBase):
    def __init__(self):
        super(DBNeiHan, self).__init__("neihan_content")

class DBPerson(DBBase):
    def __init__(self):
        super(DBPerson, self).__init__("person")



if __name__ == '__main__':
    person = DBPerson()
    data={
            "weixin": [
                {
                    "name": "开源优测",
                    "uid": "DeepTest",
                    "desc": "分享开源测试技术"
                },
                {
                    "name": "开源优测_demo",
                    "uid": "DeepTest_demo",
                    "desc": "分享开源测试技术_demo"
                }
            ],
            "web": [
                {
                    "url": "www.testingunion.com",
                    "name": "开源优测社区",
                    "desc": "分享各类开源测试技巧"
                },
                {
                    "url": "www.testingunion.com_demo",
                    "name": "开源优测社区_demo",
                    "desc": "分享各类开源测试技巧_demo"
                }
            ]
        }
    for key ,value in data.items():
        for item in value:
              person.insert_one(item)
    f = person.find_like("name", "开源")
    print(list(f))