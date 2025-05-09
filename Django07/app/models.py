from django.db import models

# Create your models here.

class StudentEnquiry(models.Model):
    name = models.CharField(max_length=255)
    dob = models.CharField(max_length=255)  
    mobile = models.CharField(max_length=10)  
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:  
        db_table = "studentTable"

    def __str__(self):
        return f"{self.name} - {self.mobile}"