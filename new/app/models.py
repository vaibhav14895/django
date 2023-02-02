from django.db import models


class forms(models.Model):
    s_name=models.CharField(max_length=20)
    s_roll=models.IntegerField( null=False)
    s_sec =models.IntegerField(blank=False)
    s_CGPA = models.IntegerField(blank=True)

