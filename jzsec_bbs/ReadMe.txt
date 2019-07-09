#框架
BVDN=bootstrap+vue+django+nginx
#web项目开发学习
下载npm
node.js中文网（安装在本机C:\Program Files\nodejs）
CMD:npm install bootstrap vue vue-router jquery
把dist下的js文件拷贝到static\js 下
23 cd .\node_modules
24 ls
25 cd .\jquery
26 ls
27 cd .\dist
28 ls
29 cp -rp * E:\Django\static\js\
30 cp -r ./* E:\Django\static\js\
31 cd E:\Django
32 npm install vue
33 npm install vue-router
34 cd .\node_modules
35 ls
36 cd vue
37 ls
38 cd .\dist
39 ls
40 cp -r ./* E:\Django\static\js
41 cd ..
42 ls
43 cd ..
44 ls
45 cd .\vue-router
46 ls
47 cd .\dist
48 ls
49 cp -r ./* E:\Django\static\js\
50 cd E:\Django\static\js
51 ls
52 rm .\README.md
53 ls
下载sublime html编辑器
http://www.sublimetext.com/3
------------------------------------
依赖包：
下面是一个简单的requirements/pord.txt需求说明文件。其中包含了所有生产环境的依赖包和基本的依赖包：
pip install -r requirements.txt
# requirements/prod.txt
-r common.txt
boto==2.1.1
cssmin==0.1.4
django-compressor==1.1.2
django-htmlmin==0.5.1
django-pylibmc-sasl==0.2.4
django-storages==1.1.3
gunicorn==0.14.1
newrelic==1.2.0.246
psycopg2==2.4.5
pylibmc==1.2.2
raven==1.3.5
slimit==0.6
最后，这是一个比较旧的requirements/test.txt文件，列出测试环境下的依赖包。这些包用于项目的单元测试环节。

# requirements/test.txt
-r common.txt
django-coverage==1.2.2
django-nose==0.1.3
mock==0.8.0
nosexcover==1.0.7




HTML <link> 标签的 rel 属性
rel 属性指示被链接的文档是一个样式表
<link href="/static/css/bootstrap.css" rel="stylesheet">

nav标签（navigate导航），是html5新增的标签，主要用于制作导航。其本身没有什么特殊性，和div功能一致。
使用nav标签是代码更具有易读性，看到标签就只到时和导航相关。

HTML <ul> 标签 无序html列表。
class="container jumbotron" #带有背影的容器
#class="btn btn-primary" 意思是对象有两个样式，即btn和btn-primary，btn样式来显示对象为按钮，
btn-primary来指定按钮为基本样式按钮，颜色为蓝色
<input class="btn btn-primary" type="submit" value="{% trans 'Log in' %}" />

表格标签table
带有 thead(表头)、tbody(主题) 以及 tfoot(表尾) 元素的 HTML 表格：
<td bgcolor="#0000FF"> 是table data cell 的缩写，单元格，可以设置背影颜色
<tr> 是table row 的缩写，表格中的一行
<th> 是table header cell 的缩写，表头单元格
<th width="300"> 固定长度

<hr> 标签定义 HTML 页面中的主题变化（比如话题的转移），并显示为一条水平线。
<hr> 元素被用来分隔 HTML 页面中的内容（或者定义一个变化）。

<table border=1> border 指的是边框的宽度


#连续写多个空格
javascript
	<script language="JavaScript">
	for (var i=1; i<= 40; i++)
	{
		document.write ("&nbsp;")
	}
	</script>
	
class="form-group" 让表单数据

表单相关的属性

{{ field.label }}：字段对应的<lable>标签的文字，例如“发件人”。
{{ field.label_tag }}：字段对应的<lable>标签。
{{ field.id_for_label }}：字段的“id”属性值。
{{ field.value }}：字段的值，例如标题的内容。
{{ field.html_name }}：字段对应的HTML标签“name”属性的值。
{{ field.help_text }}：字段的帮助文本。
{{ field.errors }}：包含任何字段验证错误的全部信息，可以通过“{% for error in field.errors %}”的方式遍历。
{{ field.is_hidden }}：字段是否隐藏字段，获取到的是布尔值。
{{ field.field }}：字段对象，可以通过它访问字段的属性，例如“{{ field.field.max_length }}”,“{{ field.field.required}}”。



CMD:

django-admin startproject jzsec_bbs
pip install django-users2
pip install pymysql
1，报错：Django did you install mysqlclient?
只要在project目录的__init__.py 下写
2，图片无法显示
修改setting.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'img'),
    ]
把jpg放到static下面。
3，python manage.py migrate

-----------------------------------------
django模板
中 block和extends
block:在母版html中将一些需要替换的部分用{% block xxx %}。。。{% endblock %}括起来，
extends:在子版html中，在第一行需要写上要继承的母版，{% extends '母版的相对路径' %}这样引入母版。
过滤器：
如果一个变量是false或者为空，使用给定的默认值。否则，使用变量的值
{%  blog.create_at | datetime %}


---------------------------------------------
vuejs

<div id="app" class="form-group">

var vm = new Vue({
    el: '#app',
    data: {
      email: '{{ request.user.email}}',
      name: '{{ request.user.name}}',
      job: '{{ request.user.job}}',
    },
    methods: {
    	submit(){
    		data_to_send = {
    			email: this.email,
    			name: this.name,
    			job: this.job,

    		};
    		console.log(data_to_send);
    	},
    },
  });
  
VueJS常用的指令:
1，指令 (Directives) 是带有 v- 前缀的特殊特性
v-text;v-model(可修改);v-bind;v-on(绑定事件)
2，vue发送数据使用的是jquery的ajax解决方案，其标准格式为：$.post(url, data, function(r, err));
3，刷新当前页面
window.location.reload();
this.$router.go(0)


------------------------------------------
防跨站
  <!--csrf token-->
  <script type="text/javascript" src="/static/js/csrf.js"></script>

多行文本显示省略号
<style type="text/css">
	.display_one{
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 1;
		overflow: hidden;
	}
</style>
  
------------------------------------------------
允许为空：
create_at = models.IntegerField(default=un_time,null=True)
获取时间戳：
#获取当前时间戳
dtime = datetime.datetime.now()
un_time = int(time.mktime(dtime.timetuple()))

添加页码：
导入Django的paginator类

model 和 form区别：
model.py
class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    pub_date=models.DateField()
    publish=models.ForeignKey("Publish")
    authors=models.ManyToManyField("Author")
    def __str__(self): return self.title


forms.py
#Modelform将一个model转化成一个form组件
class BookModelForm(forms.ModelForm):
     class Meta:
        model=models.Book
        fields="__all__"
这一步做的事情相当于下面的代码
'''
class BookModelForm(form.Form):
     title=forms.CharField(max_length=32)
     price=forms.IntegerField()
     pub_date=forms.DateField()

'''  
前端表单提交submit：
<button type="button" onclick="doValidation();">提交</button>
<input type="button" onclick="doValidation();" value="提交"/>




外键：
ForeignKey(Teacher,related_name='student_teacher',on_delete=models.CASCADE)
related_name 是通过主表查询字表信息的关联字段。
teacher = Teacher()
teacher.student_teacher.all()
#Foreign的第二参数中加入on_delete=models.CASCADE  主外关系键中，级联删除，
也就是当删除主表的数据时候从表中的数据也随着一起删除。



class Blog(models.Model):
    name = models.CharField(max_length=50, default='default name')
    blog_id = models.IntegerField(default=None,null=True)
    user_id = models.IntegerField(default=1,null=True)
    user_name = models.CharField(max_length=50,default='default name')
    content = models.CharField(max_length=9999,default='请填写内容')
    create_at = models.IntegerField(default=un_time,null=True)
    def __str__(self):
        return self.name
class Comment(models.Model):
    to_blog_id = models.ForeignKey(Blog,related_name='to_blog_id',on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    content = models.TextField(default='请填写内容')
    create_at = models.DateTimeField(auto_now = True,null=False)
    def __str__(self):
        return self.comment_user.name + ":" + self.content
# 增加数据
models.UserInfo.objects.create(name='aaa',age='18',ut_id='1')  # 注意外键是一行对象，用表中额ut_id

# 查询数据
models.UserInfo.objects.all()

# 过滤

models.UserInfo.objects.filter(name='xxx')

# 更新

models.UserInfo.objects.update(name='ddd')       

MesModel.objects.get(id=1).delete()  
--
执行自定义sql:
from django.db import connection
cursor=connection.cursor()
#插入操作
cursor.execute("insert into hello_author(name) values('郭敬明')")
#更新操作
cursor.execute('update hello_author set name='abc' where name='bcd'')
#删除操作
cursor.execute('delete from hello_author where name='abc'')
#查询操作
cursor.execute('select * from hello_author')
raw=cursor.fetchone() #返回结果行游标直读向前，读取一条
cursor.fetchall() #读取所有
--------------------------------------------
在学习django的时候，在template中写form时，出现错误。要加{% csrf_token %}才可以，之前一直也没研究，只是知道要加个这个东西，具体是什么也不明白。

目的：
csrf_token 是为了防止csrf（跨站请求伪造），什么是csrf，这篇文章讲的很好：这里。文章最后也说到了，防止csrf的手段就有给form加个token。
更简单的说：就是防止黑客盗用你存在网站（cookie）上的账户密码和信息

具体做了什么：
在渲染模板时，django会把 {% csrf_token %} 替换成一个<input type=“hidden”, name=‘csrfmiddlewaretoken’ value=服务器随机生成的token>元素。
在提交表单的时候，会把这个token给提交上去。

django默认启动 'django.middleware.csrf.CsrfViewMiddleware’中间件， 这个中间件就是来验证csrf_token的。如果没有加csrf_token，就会出错。

防止跨站请求攻击，csrf_token,随机生成一个token，提交表单时会把这个token提交上去，只有携带token才能继续使用表单。

----------------------------------------------------------
解决删除表问题：
清空迁移文件 rm -rf app/migrations/* （app对应表所在模块儿）
先 python manage.py makemigrations app 生成迁移文件
然后
删除vim app/migrations/0001_initial.py 对应创建表的字段（只删除不存在表的部分）
        migrations.CreateModel(

            name='table',

            fields=[

                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),

               .....

            ],  

            options={

              ...

            },  

        ),

最后
python manage.py makemigrations
python manage.py migrate
----------------------------------------
    if request.method == 'POST':
        form = DiscussForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.get(blog_id=blog_id)
            #newcomment = request.POST.get('content')
			#cleaned_data 是获取表单中 input name=content 的value
            newcomment = form.cleaned_data['content']
            #oldcomment = Discuss.objects.get(blog_id=blog_id)
            comment_info = Discuss(to_blog_id=blog,to_user=blog.user_name,comment_user=request.user,content=newcomment)
            comment_info.save()
            redirect_url = "/blog/"+blog_id
            return HttpResponseRedirect(redirect_url,{"form":form})
        return HttpResponseRedirect("/blog/"+blog_id)

当设置外键，制定字段必须是 类的实例而不是具体的字段信息。
-------------------------------------------------------------------
django META 属性
1，抽象类 abstract
关键字：
    class Meta:
        abstract=True

代码：
class Human(models.Model):
    name=models.CharField(max_length=100)
    GENDER_CHOICE=((u'M',u'Male'),(u'F',u'Female'),)
    gender=models.CharField(max_length=2,choices=GENDER_CHOICE,null=True)
    class Meta:
        abstract=True
class Employee(Human):
    joint_date=models.DateField()
class Customer(Human):
    first_name=models.CharField(max_length=100)
    birth_day=models.DateField() 
	
	------------------------------
    vir_name = models.CharField(max_length=50,null=True)
    vir_id = models.CharField(max_length=50,primary_key=True)
    vir_ip = models.CharField(max_length=50,null=True)
    phy_name = models.CharField(max_length=50,null=True)
    img_name = models.CharField(max_length=100)
    os_name = models.CharField(max_length=100)	
HUman是一个抽象类，不会在数据库中建表。Employee和Cunstomer 继承Human，这两个表会创建，Human就作为一个公共属性。

2，指定应用，有些时候模型类不在自己应用的 models.py中，需要指定app
app_label='myapp' 

3，定义该model在数据库中的表名称 db_table
db_table = 'Students'

4，表空间设置 db_teblespace
如果在setting中设定会使用这个值

5，get_latest_by 数据模型中有 DateField 或 DateTimeField 类型的字段，你可以通过这个选项来指定lastest()是按照哪个字段进行选取的。
get_latest_by = "order_date"，该模块将拥有一个 get_latest() 函数以得到 "最新的" 对象

6，manged
由于Django会自动根据模型类生成映射的数据库表，如果你不希望Django这么做，可以把managed的值设置为False

7，ordering 按照那个字段排序
ordering=['order_date'] # 按订单升序排列
ordering=['-order_date'] # 按订单降序排列，-表示降序
ordering=['?order_date'] # 随机排序，？表示随机 

8，permissions
设置了这个属性可以让指定的方法权限描述更清晰可读。Django自动为每个设置了admin的对象创建添加，删除和修改的权限。
permissions = (('can_deliver_pizzas','Can deliver pizzas'))

9，多字段结合 必须是唯一性
unique_together = (("first_name", "last_name"),)

10，verbose_name
给你的模型类起一个更可读的名字一般定义为中文，verbose_name = "学校"。

11，verbose_name_plural
模型的复数形式，verbose_name_plural = "学校"，如果不指定Django会自动在模型名称后加一个’s’
------------------------------------------------
报错1：TypeError: expected string or buffer（类型错误:预期的字符串或缓冲区）
字符拼接时直接在""中写了变量的组成，应该先定义变量然后再 ""+变量+""
报错2：Not all parameters were used in the SQL statement（并不是所有的变量都使用）
cursor.executemany 方法用错了。
报错3：1265 Data truncated for column at row 1错误代码解决方法
数据类型改为TextField





字符串拼接： str = 'There are'+fruit1+','+fruit2+','+fruit3+' on the table' 

@python 批量插入mysql
import mysql.connector

config = {
  'user': 'root',
  'password': '******',
  'host': '127.0.0.1',
  'database': 'test',
  'raise_on_warnings': True,
}
cnx = mysql.connector.connect(**config)

class ReadFile:
    def readLines(self):
        f = open("E:/data/2013-11-5.txt", "r", 1, "utf-8")
        i=0
        list=[]
        for line in f:
            strs = line.split("\t")
            if len(strs) != 5:
                continue
            data=(strs[0], strs[1], strs[2], strs[3], strs[4].replace("\n",""))
            list.append(data)
            cursor=cnx.cursor()
            sql = "insert into data_test(uid,log_date,fr,is_login,url)values(%s,%s,%s,%s,%s)"
            if i>5000:
                cursor.execute(sql,list)
                cnx.commit()
@实时显示时间
<h4><li class="nav-item btn_right" style="color: white"><span id="navbar_time"> </span></li></h4>
    <script type="text/javascript">
    setInterval(getlocaltime, 1000);
    function getlocaltime() {
        var localtime = new Date();
        var yy = localtime.getFullYear();
        var mo = localtime.getMonth()+1;
        var dd = localtime.getDate();
        var hh = localtime.getHours();
        var mm = localtime.getMinutes();
		
        var ss = localtime.getSeconds();

        mm = extra(mm);
        ss = extra(ss);

        document.getElementById("navbar_time").innerHTML = yy+"年"+mo+"月"+dd+"日"+"   "+hh+":"+mm+":"+ss;
        }
    function extra(x) {
        if(x < 10){
            return "0" + x;
        }else{
            return x;
        }
    }
    </script>
@显示表单数据排序
<table class="table table-hover form-group hovertable" vcontext="subusers.table" id="tableSort">	 #id
     <th onclick="$.sortTable.sort('tableSort',9)" style="cursor: pointer;">用户名称</th>
     <th onclick="$.sortTable.sort('tableSort',10)" style="cursor: pointer;">CPU</th>        		 #sortTable 是排序方法


js 	 给元素设置css
  .abc {
    background: red;
    }
test div
    var div = document.getElementById('d1');
    div.setAttribute("className", "abc");	 
	 
加字段备注


 $(this).next('ul').toggleClass('active')
 toggleclass 方法的意思是 切换，增加和删除active class

获取子元素：
$(document).ready(function(){
  $("div").children("p.1");
});

$(document).ready(function(){
  $("div").find("span");
});
 
 
----------------------------------------------------------------------------
app 模块无法引用问题，是因为整个项目不知道source root是什么，
解决方法：
pycharm 中设置MARK directory as source root
https://blog.csdn.net/moniicoo/article/details/83037359
















		setInterval(second_switch, 3000);
		function second_switch(){
			if ($("a").children("h1").text() != {{ item.0 }}) {
				if ({{ item.4 }} != {{ item.6 }} }) {
					$(this).remove('first')
					$(this).toggleClass('second');
				}
			}
		}
		
------------------
		 "GET /favicon.ico HTTP/1.1" 404 2181

解决的方法：

1、做个favicon.ico文件放在根目录下，在head标签引入favicon.ico文件即可

<link href="favicon.ico" rel="shortcut icon">

-------------------------------------------------------
###分布式异步处理

celery+redis  实现分布式异步任务处理（举个例子，当点击页面上发送邮件(手机验证码)功能，页面请求还是要显示出来，发送任务就异步在后台继续执行，让用户有更好的体验）
pip install celery
pip install redis
celery是 用python语言开发的，有以下部分组成：
1，任务task：python函数
2，队列queue：将需要执行的任务加到队列中（任务详细信息会在 redis 中以key value 的形式存储）
3，工人worker：在一个新的进程中，负责执行队列中的任务
4，代理人broker：负责调度，一般是redis rabbit
备注：celery本身没有消息存储，调度功能，只是任务的异步执行，需要和消息队列一起使用。

执行过程：
client 端产生任务task，然后放到queue队列中，代理人redis会通知队列中有任务，空闲的worker会去从队列中取出任务进行执行。
celery 和 redis 之间交互的基本原理：
1、当发起一个 task 时，会向 redis 的 celery key 中插入一条记录。
2、如果这时有正在待命的空闲 worker，这个 task 会立即被 worker 领取。
3、如果这时没有空闲的 worker，这个 task 的记录会保留在 celery key 中。
4、这时会将这个 task 的记录从 key celery 中移除，并添加相关信息到 unacked 和 unacked_index 中。
5、worker 根据 task 设定的期望执行时间执行任务，如果接到的不是延时任务或者已经超过了期望时间，则立刻执行。
6、worker 开始执行任务时，通知 redis。（如果设置了 CELERY_ACKS_LATE = True 那么会在任务执行结束时再通知）
7、redis 接到通知后，将 unacked 和 unacked_index 中相关记录移除。
8、如果在接到通知前，worker 中断了，这时 redis 中的 unacked 和 unacked_index 记录会重新回到 celery key 中。(这个回写的操作是由 worker 在 “临死” 前自己完成的，所以在关闭 worker 时为防止任务丢失，请务必使用正确的方法停止它，如: celery multi stop w1 -A proj1)
9、在 celery key 中的 task 可以再次重复上述 2 以下的流程。



###redis做页面缓存
yum -y isntall redis-server
认证：
vim /etc/redis.conf
requirepass django
1,redis-cli -h 127.0.0.1 -p 6379 -a reson
2,
$redis-cli 
>auth django
>get a
-----------------------------------------
view 变量传入：
如果你是个喜欢偷懒的程序员并想让代码看起来更加简明，可以利用 Python 的内建函数 locals() 。
它返回的字典对所有局部变量的名称与值进行映射。 因此，前面的视图可以重写成下面这个样子：
def current_datetime(request):
  current_date = datetime.datetime.now()
  return render_to_response('current_datetime.html', locals())