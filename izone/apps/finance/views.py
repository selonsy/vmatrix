# from django.shortcuts import render
# from django.http import JsonResponse
# from django.contrib.auth.decorators import login_required
from .service import *


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
    return JsonResponse({'key': 'Hello World!'})


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
    data = get_finance_list(begin_time, end_time, is_show_by_monthly, is_show_gjjyb)
    return JsonResponse({'key': 'Hello World!'})


def GetDetailById(request):
    """[获取详情]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return JsonResponse({'key': 'Hello World!'})


def GetDetailByName(request):
    """[获取详情]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return JsonResponse({'key': 'Hello World!'})


def GetLocations(request):
    """[获取最新资产位置]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return JsonResponse({'key': 'Hello World!'})


def GetItemDetails(request):
    """[获取所有项目详情]
    
    Arguments:
        request {[type]} -- [description]
    
    Returns:
        [type] -- [description]
    """
    return JsonResponse({'key': 'Hello World!'})
