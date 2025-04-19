from django.shortcuts import render

# Create your views here.

def userListIndex(request):
    return render(request, 'userList/index.html')