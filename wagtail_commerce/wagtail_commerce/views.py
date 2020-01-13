from django.shortcuts import HttpResponse


def testing_page(request):
    return HttpResponse("Testing Page Here.")
