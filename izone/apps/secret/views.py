from django.shortcuts import render

# Create your views here.
def HtmlTest(request):
    context = {}
    context['hello'] = 'Hello World!'
    return render(request, 'secret/test.html', context)