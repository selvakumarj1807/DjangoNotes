from django.shortcuts import render
from rest_framework import generics
from .models import Student
from .serializers import StudentSerializer

class StudentListCreateView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    

def student_page(request):
    return render(request, 'students/student_list.html')

def student_form(request, pk=None):
    return render(request, 'students/student_form.html', {'pk': pk})

def student_detail_page(request, pk):
    return render(request, 'students/student_detail.html', {'pk': pk})
