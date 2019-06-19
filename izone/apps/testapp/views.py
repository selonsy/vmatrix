from django.shortcuts import render

# Create your views here.
def HtmlTest(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'testapp/test.html', context)