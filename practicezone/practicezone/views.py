from django.http import HttpResponseRedirect
from django.shortcuts import render
from .test_link_validator import LinkTest
from diary.models import Entry
from gitlog.models import Commit

# Create your views here.
def humanFormat(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.2f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

def onlyYMD(datetime_object):
    return (datetime_object.year, datetime_object.month, datetime_object.day)


def index(request):
    entries = Entry.objects.order_by('-posted_date')
    commits = Commit.objects.all()
    formated_commits = []
    work_days = []
    line_of_code = 0
    for commit in commits:
        formated_commit = {}
        formated_commit['weekday'] = commit.datetime_object.strftime('%a')
        formated_commit['month'] = commit.datetime_object.strftime('%b')
        formated_commit['day'] = commit.datetime_object.strftime('%d')
        formated_commit['branch'] = commit.branch
        formated_commit['insertions_count'] = commit.insertions_count
        formated_commit['deletions_count'] = commit.deletions_count
        formated_commit['commit_note'] = commit.commit_note
        formated_commits.append(formated_commit)

        line_of_code += commit.insertions_count - commit.deletions_count
        if onlyYMD(commit.datetime_object) not in work_days:
            work_days.append(onlyYMD(commit.datetime_object))

    context = {
        'entries': entries,
        'commits': formated_commits,
        'commits_count': len(formated_commits),
        'line_of_code': humanFormat(line_of_code),
        'days_of_work': len(work_days)

    }

    return render(request, "index_gitlog.html", context)


def showTheTestResult(request):
    linkTest = LinkTest()
    result_list = linkTest.test_url_without_var()
    context = {
        'result_list': result_list
    }
    return render(request, "showTheTestResult.html", context)
