from django.db import models
import datetime
import time
from users.models import User
# Create your models here.

#获取当前时间戳
dtime = datetime.datetime.now()
un_time = int(time.mktime(dtime.timetuple()))




class Blog(models.Model):
    name = models.CharField(max_length=50, default='default name')
    blog_id = models.IntegerField(default=1,unique=True)
    user_id = models.IntegerField(default=1,null=True)
    user_name = models.CharField(max_length=50,default='default name')
    content = models.TextField(default='请填写内容')
    create_at = models.IntegerField(default=un_time,null=True)
    def __str__(self):
        return self.name
class Discuss(models.Model):
    to_blog_id = models.ForeignKey(Blog,to_field='blog_id',related_name='to_blog_id',on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    to_user = models.CharField(max_length=50, default='default name')
    content = models.TextField(default='请填写内容')
    create_at = models.DateTimeField(auto_now = True,null=False)


    class Meta:
        db_table = 'Discuss'

class img(models.Model):
    img_info = models.TextField(default='请填写内容')