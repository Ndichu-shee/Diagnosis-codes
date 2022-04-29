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
    icd_code = models.CharField(max_length=20,choices=CODES,default='icd_10')
    category_code = models.CharField(null=True, max_length=6)
    code_id = models.CharField(null=True, max_length=5)
    addition_code = models.CharField(max_length=10)
    summary= models.TextField(null=True)
    description = models.TextField(default="")
    category_title = models.CharField(null=True, max_length=20)


    def __str__(self):
        return self.summary

    def save(self,*args,**kwargs):
        self.addition_code = self.category_code + str(self.code_id)
        super(DiagnosisCodes, self).save(*args, **kwargs)
