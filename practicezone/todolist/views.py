from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import TodoList, Category
from django.urls import reverse

# Create your views here.
def index(request):
    todos = TodoList.objects.all()
    categories = Category.objects.all()
    if request.method == "POST":
        if "taskAdd" in request.POST:
            title = request.POST["description"]
            date = str(request.POST["date"])
            category = request.POST["category_select"]

            content = title + "--" + date + " " + category
            Todo = TodoList(title=title, content=content, due_date=date, 
                            category=Category.objects.get(name=category))
            Todo.save()
            return HttpResponseRedirect(reverse('todolist'))

        if "taskDelete" in request.POST:
            checkedlist = request.POST["checkedboxlist"].split(',')
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id))
                todo.delete()
    return render(request, "todolist/index.html", {"todos": todos, "categories": categories})
            
