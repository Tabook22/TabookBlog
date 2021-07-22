from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    context={
        "title":"First Page",
        "details":"In the Name of God Most Merci most Mercifull"
    }
    return render(request, "index.html",context)
