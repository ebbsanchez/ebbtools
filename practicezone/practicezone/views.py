from django.http import HttpResponseRedirect
from django.shortcuts import render
from .test_link_validator import LinkTest

# Create your views here.


def index(request):
    return render(request, "index.html")


def showTheTestResult(request):
    linkTest = LinkTest()
    result_list = linkTest.test_url_without_var()
    context = {
        'result_list': result_list
    }
    return render(request, "showTheTestResult.html", context)
