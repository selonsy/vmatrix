from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
# Create your views here.

# @login_required
# @require_POST
def JsonTest(request):
    return JsonResponse({'key': 'Hello World!'})


def HtmlTest(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'finance/test.html', context)    
