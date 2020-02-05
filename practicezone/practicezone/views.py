from django.http import HttpResponseRedirect
from django.shortcuts import render
from .test_link_validator import LinkTest
from diary.models import Entry
from gitlog.models import Commit

# Create your views here.


def index(request):
    entries = Entry.objects.order_by('-posted_date')
    commits = Commit.objects.all()
    formated_commits = []
    for commit in commits:
        formated_commit = {}
        formated_commit['weekday'] = commit.datetime_object.strftime('%a')
        formated_commit['day'] = commit.datetime_object.strftime('%d')
        formated_commit['branch'] = commit.branch
        formated_commit['insertions_count'] = commit.insertions_count
        formated_commit['deletions_count'] = commit.deletions_count
        formated_commit['commit_note'] = commit.commit_note
        formated_commits.append(formated_commit)

    context = {
        'entries': entries,
        'commits': formated_commits,

    }

    return render(request, "index_gitlog.html", context)


def showTheTestResult(request):
    linkTest = LinkTest()
    result_list = linkTest.test_url_without_var()
    context = {
        'result_list': result_list
    }
    return render(request, "showTheTestResult.html", context)
