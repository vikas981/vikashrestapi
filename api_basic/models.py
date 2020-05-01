from django.db import models


class Test(models.Model):
    teststep = models.CharField(max_length=10)
    testcase = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='vikas.com')
    status = models.IntegerField()
    authkey = models.CharField(max_length=100)

    def __str__(self):
        return self.teststep
