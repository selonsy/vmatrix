# public BsonResult GetList()
# {
#     APIReturn json = new privateService(Operator).get_finance_list(_("begin_time"), _("end_time"), _("is_show_by_monthly").ToBool(), _("is_show_gjjyb").ToBool());
#     return MyReturn.ResponseBson(json);
# }
import time
import datetime
from finance.mongo import DBFinance


def get_finance_list(begin_time, end_time, is_show_by_monthly, is_show_gjjyb, is_show_origial=False):
    """[summary]

    Arguments:
        begin_time {[string]} -- [description]
        end_time {[string]} -- [description]
        is_show_by_monthly {bool} -- [description]
        is_show_gjjyb {bool} -- [description]

    Keyword Arguments:
        is_show_origial {bool} -- [description] (default: {False})
    """
    if(not begin_time or not end_time):
        # 时间处理
        now = datetime.datetime.now()
        delta1 = datetime.timedelta(days=-200)
        delta2 = datetime.timedelta(days=1)
        if not begin_time:
            begin_time = (now + delta1).strftime('%Y-%m-%d')
        if not end_time:
            end_time = (now + delta2).strftime('%Y-%m-%d')
    total = 0
    finance = DBFinance()
    conditions = {'add_time': {'$gte': datetime.datetime.strptime(
        begin_time, "%Y-%m-%d"), '$lte': datetime.datetime.strptime(end_time, "%Y-%m-%d")}}
    list_data = finance.find_many(conditions).sort([("add_time", 1)])
    # 直接打印出来是 <pymongo.cursor.Cursor object at 0x02096DF0>  其实就是一个游标，数据还不在内存中
    # 如果需要处理的话，可以使用：
    # from bson import json_util as jsonb
    # print(jsonb.dumps(list(list_data)))
    if is_show_origial:
        return list_data
    list_result = []
    for data in list_data:
        tuple_now = get_asset_debt_total(data, is_show_gjjyb)
        temp = {}
        temp["asset"] = tuple_now[0]
        temp["debt"] = tuple_now[1]
        temp["name"] = data["name"]
        temp["id"] = str(data["_id"])
        temp["add_time"] = data["add_time"].strftime('%Y-%m-%d')
        list_result.append(temp)
    return list_result


def get_finance_detail_byname(name, is_show_gjjyb):
    """[summary]

    Arguments:
        name {[type]} -- [description]
    """
    _time = datetime.datetime.strptime(name, '%Y-%m-%d')
    last_year = (_time + datetime.timedelta(days=-365)).strftime('%Y-%m')
    last_month = (_time + datetime.timedelta(days=-30)).strftime('%Y-%m')
    finance = DBFinance()
    conditions = {'name': name}
    list_data = finance.find_one(conditions)
    list_last_year = list(finance.find_like('name', last_year))
    list_last_month = list(finance.find_like('name', last_month))

    list_last_year = list_last_year[0] if len(list_last_year) > 0 else None
    list_last_month = list_last_month[0] if len(list_last_month) > 0 else None
    
    tuple_lastyear = get_asset_debt_total(list_last_year, is_show_gjjyb)
    tuple_lastmonth = get_asset_debt_total(list_last_month, is_show_gjjyb)
    tuple_now = get_asset_debt_total(list_data, is_show_gjjyb)

    list_data["asset"] = tuple_now[0]
    list_data["debt"] = tuple_now[1]
    list_data["total"] = tuple_now[2]

    huanbi = huanbi_money = tongbi = tongbi_money = 0
    if tuple_lastmonth:
        huanbi = ((tuple_now[2] - tuple_lastmonth[2]) /
                  tuple_lastmonth[2])*100 if tuple_lastmonth[2] > 0 else 0
        huanbi_money = tuple_now[2] - tuple_lastmonth[2]
    if tuple_lastyear:
        tongbi = ((tuple_now[2] - tuple_lastyear[2]) /
                  tuple_lastyear[2])*100 if tuple_lastyear[2] > 0 else 0
        tongbi_money = tuple_now[2] - tuple_lastyear[2]

    list_data["huanbi"] = huanbi
    list_data["huanbi_money"] = huanbi_money
    list_data["tongbi"] = tongbi
    list_data["tongbi_money"] = tongbi_money

    list_data["_id"] = str(list_data["_id"])
    list_data["add_time"] = list_data["add_time"].strftime('%Y-%m-%d')
    list_data["modify_time"] = list_data["modify_time"].strftime('%Y-%m-%d')    
    return list_data


def get_asset_debt_total(data, is_show_gjjyb=True):
    """[ 汇总资产和负债 ]

    Arguments:
        data {[type]} -- [description]

    Keyword Arguments:
        is_show_gjjyb {bool} -- [description] (default: {True})
    """    
    if not data:
        return None    
    asset = 0
    debt = 0
    for d in data["detail"]:
        if not is_show_gjjyb and d["name"] in ('公积金', '医保'):
            continue
        if d["type"] == '资产':
            asset += d["number"]
        elif d["type"] == '负债':
            debt += d["number"]
    total = asset - debt
    return int(asset), int(debt), int(total)
