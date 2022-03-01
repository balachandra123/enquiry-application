from django.db import models

# Create your models here.
class Enquiry(models.Model):
    Enquiryid=models.IntegerField(primary_key=True)
    enquiryname=models.CharField(max_length=30)
    course=models.CharField(max_length=20)
    contact_number=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    def __str__(self):
        return f'{self.Enquiryid}-{self.enquiryname}-{self.course}'

