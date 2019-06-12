from django.db import models

# Create your models here.
class ver_repostory(models.Model):
    sys_name = models.CharField(max_length=500)
    mod_name = models.CharField(max_length=500)
    process_name = models.CharField(max_length=500)
    version = models.CharField(max_length=100)
    process_path =models.CharField(max_length=500)
    md5 = models.CharField(max_length=100)
    remark = models.TextField(null=True)
    def __str__(self):
        return self.md5

    class Meta():
        db_table = 'ver_repostory'
        unique_together = ("sys_name","mod_name")

class ser_version(models.Model):
    sys_name = models.CharField(max_length=500)
    ope_director = models.CharField(max_length=500)
    mod_name = models.CharField(max_length=500)
    ser_ip = models.CharField(max_length=50)
    process_name = models.CharField(max_length=500)
    version = models.CharField(max_length=100)
    process_path = models.CharField(max_length=500)
    conf_path = models.CharField(max_length=500)
    log_path = models.CharField(max_length=500)
    change_path = models.CharField(max_length=500)
    md5 = models.CharField(max_length=100)
    remark = models.TextField(null=True)
    def __str__(self):
        return self.sys_name + self.mod_name

    class Meta():
        db_table = 'ser_version'
        unique_together = ("sys_name", "mod_name",)