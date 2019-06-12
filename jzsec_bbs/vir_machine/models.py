from django.db import models


# Create your models here.
class vir_machine(models.Model):
    vir_name = models.CharField(max_length=50,null=True)
    vir_id = models.CharField(max_length=50,primary_key=True)
    vir_ip = models.CharField(max_length=50,null=True)
    phy_name = models.CharField(max_length=50,null=True)
    img_name = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)
    account_id = models.CharField(max_length=50)
    account_name = models.CharField(max_length=50)
    vir_cpu = models.IntegerField()
    vir_cpu_rate = models.CharField(max_length=50,null=True)
    vir_memory = models.IntegerField()
    vir_memory_rate = models.CharField(max_length=50,null=True)
    disk_type = models.TextField(null=True)
    disk_total = models.IntegerField(null=True)
    create_time = models.CharField(max_length=100,null=True)
    belong_sys = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.vir_ip

    class Meta():
        db_table = 'vir_machine'