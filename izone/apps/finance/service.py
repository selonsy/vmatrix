# public BsonResult GetList()
# {
#     APIReturn json = new privateService(Operator).get_finance_list(_("begin_time"), _("end_time"), _("is_show_by_monthly").ToBool(), _("is_show_gjjyb").ToBool());
#     return MyReturn.ResponseBson(json);
# }
import time

def get_finance_list(begin_time, end_time, is_show_by_monthly, is_show_gjjyb, is_show_origial = False):
    """[summary]
    
    Arguments:
        begin_time {[string]} -- [description]
        end_time {[string]} -- [description]
        is_show_by_monthly {bool} -- [description]
        is_show_gjjyb {bool} -- [description]
    
    Keyword Arguments:
        is_show_origial {bool} -- [description] (default: {False})
    """
    if(not begin_time):
        # data=time.strftime('%Y-%m-%d %H%:%M',time.localtime(time.time()))     #time.strftime将data格式转成指定的字符串格式
        begin_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))
    if(not end_time):
        begin_time = time.strftime('%Y-%m-%d',time.localtime(time.time()))

    pass

def get_locations():
    """[summary]
    """
    pass

def get_item_details(begin_time, end_time, is_show_all, dic):
    """[summary]
    
    Arguments:
        begin_time {[string]} -- [description]
        end_time {[string]} -- [description]
        is_show_all {bool} -- [description]
        dic {[Dictionary]} -- [description]
    """
    pass

def get_item_detail_by_name(name):
    """[summary]
    
    Arguments:
        name {[type]} -- [description]
    """
    pass

