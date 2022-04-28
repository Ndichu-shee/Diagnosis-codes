from django.db import models

# Create your models here.
class NewUser(models.Model):
    email = models.EmailField()
    password= models.CharField(max_length=6)

    def __str__(self):
        return self.email

class Category(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    category_code = models.CharField(null=True, max_length=6)
    category_title = models.CharField(null=True, max_length=20)

    def __str__(self):
        return self.category_title

class DiagnosisCodes(models.Model):
    id = models.CharField(primary_key=True, max_length=6)
    category_code = models.CharField(null=True, max_length=6)
    code_id = models.CharField(null=True, max_length=5)
    summary= models.CharField(null=True, max_length=30)
    description = models.CharField(max_length=40)
    category_title = models.CharField(null=True, max_length=20)
    icd_code= models.CharField(default='ICD_10',max_length=8,null=True)

    def __str__(self):
        return self.summary
