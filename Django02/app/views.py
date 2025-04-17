from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def user(request):
    return render(request, 'user.html')

def userEnquiry(request):
    return render(request, 'userEnquiry.html')

def userList(request):
    return render(request, 'userList.html')