# 导入包
from pymongo import MongoClient
import datetime
#########################################################
# 数据库连接
#########################################################
conn = MongoClient('localhost', 27017)
db = conn.vmatrix       #连接vmatrix数据库，没有则自动创建
my_set = db.finance     #使用test_set集合，没有则自动创建

conditions = {'add_time': {'$gte': datetime.datetime.strptime("2018-11-01","%Y-%m-%d"),'$lte': datetime.datetime.strptime("2019-06-03","%Y-%m-%d")}}
list_data = my_set.find(conditions).sort([("add_time", 1)])
for a in list_data:
    print(a)