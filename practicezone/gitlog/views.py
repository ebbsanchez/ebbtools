from django.shortcuts import render
from django.http import HttpResponseRedirect
from .utils import getCommits
from .models import Commit
# Create your views here.


def index(request):
    context = {}
    return render(request, 'gitlog/index.html', context)


def run(request):
    if request.method == 'POST':
        commits = getCommits()
        for commit in commits:
            instance, created = Commit.objects.get_or_create(
                commit_hash=commit['commit_hash'],
                branch=commit['branch'],
                author=commit['author'],
                email=commit['email'],
                datetime_object=commit['datetime'],
                commit_note=commit['commit_note'],
                file_changed_count=commit['file_changed_count'],
                insertions_count=commit['insertions_count'],
                deletions_count=commit['deletions_count']
            )
            instance.save()

        commits_count = len(Commit.objects.all())
        message = "Create and Save. Got " + str(commits_count) + " Commits"
        commits = Commit.objects.all()
    else:
        commits = Commit.objects.all()
        commits_count = len(Commit.objects.all())
        message = 'wait to run, Got ' + str(commits_count) + " Commits"

    context = {
        'message': message,
        'commits': commits
    }
    return render(request, 'gitlog/run.html', context)
