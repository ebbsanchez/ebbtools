from django.http import HttpResponseRedirect
from django.shortcuts import render
from .test_link_validator import LinkTest
from diary.models import Entry

# Create your views here.


def index(request):
    entries = Entry.objects.order_by('-posted_date')
    context = {
        'entries': entries,
    }

    return render(request, "index.html", context)


def showTheTestResult(request):
    linkTest = LinkTest()
    result_list = linkTest.test_url_without_var()
    context = {
        'result_list': result_list
    }
    return render(request, "showTheTestResult.html", context)
