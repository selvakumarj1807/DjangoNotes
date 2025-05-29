from django.urls import path
from .views import StudentListCreateView, StudentDetailView
from students import views

urlpatterns = [
    path('students/', StudentListCreateView.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student-detail'),
    
    
    path('', views.student_page, name='student-list'),
    path('add/', views.student_form, name='student-add'),
    path('edit/<int:pk>/', views.student_form, name='student-edit'),
    path('detail/<int:pk>/', views.student_detail_page, name='student-detail'),
]