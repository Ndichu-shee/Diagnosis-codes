from django.db import models

# Create your models here.
class NewUser(models.Model):
    email = models.EmailField()
    password= models.CharField(max_length=6)

    def __str__(self):
        return self.email


class DiagnosisCodes(models.Model):
    CODES=(
        ('icd_9','ICD_9 2008'),
        ('icd_10','ICD_10 2015'),
        ('icd_11','ICD_11 2022'),
        )
    icd_code = models.CharField(max_length=10,choices=CODES,default='icd_10')
    code_id = models.CharField(null=True, max_length=5)
    category_code = models.CharField(null=True, max_length=6)
    full_code = models.CharField(max_length=10)
    category_title = models.CharField(null=True, max_length=20)
    summary= models.TextField(null=True)
    description = models.TextField(default="")

    def __str__(self):
        return self.summary

    def save(self,*args,**kwargs):
        self.full_code = self.category_code + str(self.code_id)
        super(DiagnosisCodes, self).save(*args, **kwargs)
