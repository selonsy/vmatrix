from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .service import get_finance_list, get_finance_detail_byname


# Create your views here.

# @login_required
# @require_POST
def JsonTest(request):
    return JsonResponse({'key': 'Hello World!'})


def HtmlTest(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'finance/test.html', context)


def Index(request):
    return render(request, 'finance/index.html')


def Detail(request):
    return render(request, 'finance/detail.html')


def GetList(request):
    """[获取列表]

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    begin_time = request.POST.get('begin_time')
    end_time = request.POST.get('end_time')
    is_show_by_monthly = int(request.POST.get('is_show_by_monthly'))
    is_show_gjjyb = int(request.POST.get('is_show_gjjyb'))
    data = get_finance_list(begin_time, end_time,
                            is_show_by_monthly, is_show_gjjyb)
    dic = {}
    dic["code"] = 1
    dic["data"] = data
    dic["msg"] = "success"
    return JsonResponse(dic, safe=False)
    # In order to allow non-dict objects to be serialized set the safe = False
    # 


def GetDetailByName(request):
    """[获取详情]

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    name = request.POST.get('name')
    is_show_gjjyb = int(request.POST.get('is_show_gjjyb'))
    data = get_finance_detail_byname(name, is_show_gjjyb)
    
    dic = {}
    dic["code"] = 1
    dic["data"] = data
    dic["msg"] = "success"
    return JsonResponse(dic, safe=False)


def Add(request):
    """[新增资产]

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    begin_time = ""
    end_time = ""
    is_show_by_monthly = True
    is_show_gjjyb = False
    data = get_finance_list(begin_time, end_time,
                            is_show_by_monthly, is_show_gjjyb)
    return JsonResponse({'key': 'Hello World!'})


def GetLocations(request):
    """[获取最新资产位置]

    Arguments:
        request {[type]} -- [description]

    Returns:
        [type] -- [description]
    """
    return JsonResponse({'key': 'Hello World!'})
