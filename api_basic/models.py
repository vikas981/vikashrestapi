from django.db import models


class Test(models.Model):
    TESTSTEP=(
        ('TC_1', 'TC_1'),
        ('TC_2', 'TC_2'),
        ('TC_3', 'TC_3')
    )
    STATUS=(
        ('200', '200'),
        ('400', '400'),
        ('404', '404')
    )
    teststep = models.CharField(max_length=10,choices=TESTSTEP)
    testcase = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    url = models.CharField(max_length=100, default='vikas.com')
    status = models.IntegerField(choices=STATUS)
    authkey = models.CharField(max_length=100)

    def __str__(self):
        return self.teststep
