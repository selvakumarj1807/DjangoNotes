from django.shortcuts import render

# Create your views here.

def userEnquiryIndex(request):
    return render(request, 'userEnquiry/index.html')