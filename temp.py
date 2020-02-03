
# inspired by https://gist.github.com/simonw/091b765a071d1558464371042db3b959
import subprocess
import re
import datetime

# commit{} in commits[]
    # commit_hash
    # branch
    # author
    # date
    # commit_note
    # stat

def main():
    raw_text = getGitLog()
    commits  = gitLogToList(raw_text)
    for commit in commits:
        constructred_commit = constructForDB(commit)
        saveCommitToDB(constructred_commit, model)

def getGitLog()
    raw = subprocess.check_output(
        ['git', 'log', '--decorate', '--shortstat'], stderr=subprocess.STDOUT
    ).decode("utf-8")
    return raw

def gitLogToList(raw_text):

    commits = []
    current_commit = {}
    lines = raw.split("\n")
    for line in lines:
        if line == '':
            continue
        if line.startswith('commit '):
            if current_commit:
                commits.append(current_commit)
                current_commit = {}
            commit_hash, branch = parseCommitLine(line)
            current_commit['commit_hash'] = commit_hash
            current_commit['branch'] = branch
        elif line.startswith('  '):
            commit_note = line.strip()
            current_commit["commit_note"] = commit_note
        elif line.startswith(' '):
            current_commit['stat'] = line.strip()
        else:
            key, value = line.split(':', 1)
            current_commit[key.lower()] = value.strip()

    # Save the last commit
    commits.append(current_commit)

    return commits


def parseCommitLine(line):
    _, commit_hash = line[:47].split(' ')
    if '(' in line:
        branch = line[48:][1:-1]
    else:
        branch = 'master'
    return commit_hash, branch

# ----------------------------------------------------------------------------------------------------

def constructForDB(commit):
    constructred_dict = {}
    # commit_hash  40 char
    constructred_dict['commit_hash'] = commit['commit_hash']
    # branch 30 char
    constructred_dict['branch'] = commit['branch']

    # Author 30 char # Mail 30 char
    author, email = commit['author'].split('<')
    constructred_dict['author'] = author.strip()
    constructred_dict['email'] = email[-1].strip()

    # Date timestamp
    datetime_object = datetime.datetime.strptime(
        commit['date'], '%a %b %d %H:%M:%S %Y %z')
    constructred_dict['datetime'] = datetime_object

    # Commit_note  200 char
    constructred_dict['commit_note'] = commit['commit_note']
    
    # file_changed_count int # insertions_count int # deletions_count int
    try:
        file_changed_count, insertions_count, deletions_count = parseStatLine(commit['stat'])
    except KeyError:
        if commit['merge']:
            file_changed_count, insertions_count, deletions_count = (0,0,0)
        else:
            raise KeyError 

    constructred_dict['file_changed_count'] = constructred_dict['file_changed_count']
    constructred_dict['insertions_count'] = insertions_count
    constructred_dict['deletions_count'] = deletions_count

    return constructred_dict


def parseStatLine(statLine):
    
    stats = statLine.split(',')
    
    for stat in stats:
        file_changed_count = 0
        insertions_count = 0
        deletions_count = 0
        if 'changed' in stat:
            file_changed_count = int(stat.split[' '][0])
        elif 'insertion' in stat:
            insertions_count = int(stat.split[' '][0])
        elif 'deletion' in stat:
            deletions_count = int(stat.split[' '][0])
    return (file_changed_count, insertions_count, deletions_count)

def saveCommitToDB(constructred_commit):
    

