#���
BVDN=bootstrap+vue+django+nginx
#web��Ŀ����ѧϰ
����npm
node.js����������װ�ڱ���C:\Program Files\nodejs��
CMD:npm install bootstrap vue vue-router jquery
��dist�µ�js�ļ�������static\js ��
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
����sublime html�༭��
http://www.sublimetext.com/3
------------------------------------
��������
������һ���򵥵�requirements/pord.txt����˵���ļ������а��������������������������ͻ�������������
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
�������һ���ȽϾɵ�requirements/test.txt�ļ����г����Ի����µ�����������Щ��������Ŀ�ĵ�Ԫ���Ի��ڡ�

# requirements/test.txt
-r common.txt
django-coverage==1.2.2
django-nose==0.1.3
mock==0.8.0
nosexcover==1.0.7




HTML <link> ��ǩ�� rel ����
rel ����ָʾ�����ӵ��ĵ���һ����ʽ��
<link href="/static/css/bootstrap.css" rel="stylesheet">

nav��ǩ��navigate����������html5�����ı�ǩ����Ҫ���������������䱾��û��ʲô�����ԣ���div����һ�¡�
ʹ��nav��ǩ�Ǵ���������׶��ԣ�������ǩ��ֻ��ʱ�͵�����ء�

HTML <ul> ��ǩ ����html�б�
class="container jumbotron" #���б�Ӱ������
#class="btn btn-primary" ��˼�Ƕ�����������ʽ����btn��btn-primary��btn��ʽ����ʾ����Ϊ��ť��
btn-primary��ָ����ťΪ������ʽ��ť����ɫΪ��ɫ
<input class="btn btn-primary" type="submit" value="{% trans 'Log in' %}" />

����ǩtable
���� thead(��ͷ)��tbody(����) �Լ� tfoot(��β) Ԫ�ص� HTML ���
<td bgcolor="#0000FF"> ��table data cell ����д����Ԫ�񣬿������ñ�Ӱ��ɫ
<tr> ��table row ����д������е�һ��
<th> ��table header cell ����д����ͷ��Ԫ��
<th width="300"> �̶�����

<hr> ��ǩ���� HTML ҳ���е�����仯�����绰���ת�ƣ�������ʾΪһ��ˮƽ�ߡ�
<hr> Ԫ�ر������ָ� HTML ҳ���е����ݣ����߶���һ���仯����

<table border=1> border ָ���Ǳ߿�Ŀ��


#����д����ո�
javascript
	<script language="JavaScript">
	for (var i=1; i<= 40; i++)
	{
		document.write ("&nbsp;")
	}
	</script>
	
class="form-group" �ñ�����

����ص�����

{{ field.label }}���ֶζ�Ӧ��<lable>��ǩ�����֣����硰�����ˡ���
{{ field.label_tag }}���ֶζ�Ӧ��<lable>��ǩ��
{{ field.id_for_label }}���ֶεġ�id������ֵ��
{{ field.value }}���ֶε�ֵ�������������ݡ�
{{ field.html_name }}���ֶζ�Ӧ��HTML��ǩ��name�����Ե�ֵ��
{{ field.help_text }}���ֶεİ����ı���
{{ field.errors }}�������κ��ֶ���֤�����ȫ����Ϣ������ͨ����{% for error in field.errors %}���ķ�ʽ������
{{ field.is_hidden }}���ֶ��Ƿ������ֶΣ���ȡ�����ǲ���ֵ��
{{ field.field }}���ֶζ��󣬿���ͨ���������ֶε����ԣ����硰{{ field.field.max_length }}��,��{{ field.field.required}}����



CMD:

django-admin startproject jzsec_bbs
pip install django-users2
pip install pymysql
1������Django did you install mysqlclient?
ֻҪ��projectĿ¼��__init__.py ��д
2��ͼƬ�޷���ʾ
�޸�setting.py
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'img'),
    ]
��jpg�ŵ�static���档
3��python manage.py migrate

-----------------------------------------
djangoģ��
�� block��extends
block:��ĸ��html�н�һЩ��Ҫ�滻�Ĳ�����{% block xxx %}������{% endblock %}��������
extends:���Ӱ�html�У��ڵ�һ����Ҫд��Ҫ�̳е�ĸ�棬{% extends 'ĸ������·��' %}��������ĸ�档
��������
���һ��������false����Ϊ�գ�ʹ�ø�����Ĭ��ֵ������ʹ�ñ�����ֵ
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
  
VueJS���õ�ָ��:
1��ָ�� (Directives) �Ǵ��� v- ǰ׺����������
v-text;v-model(���޸�);v-bind;v-on(���¼�)
2��vue��������ʹ�õ���jquery��ajax������������׼��ʽΪ��$.post(url, data, function(r, err));
3��ˢ�µ�ǰҳ��
window.location.reload();
this.$router.go(0)


------------------------------------------
����վ
  <!--csrf token-->
  <script type="text/javascript" src="/static/js/csrf.js"></script>

�����ı���ʾʡ�Ժ�
<style type="text/css">
	.display_one{
		display: -webkit-box;
		-webkit-box-orient: vertical;
		-webkit-line-clamp: 1;
		overflow: hidden;
	}
</style>
  
------------------------------------------------
����Ϊ�գ�
create_at = models.IntegerField(default=un_time,null=True)
��ȡʱ�����
#��ȡ��ǰʱ���
dtime = datetime.datetime.now()
un_time = int(time.mktime(dtime.timetuple()))

���ҳ�룺
����Django��paginator��

model �� form����
model.py
class Book(models.Model):
    title=models.CharField(max_length=32)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    pub_date=models.DateField()
    publish=models.ForeignKey("Publish")
    authors=models.ManyToManyField("Author")
    def __str__(self): return self.title


forms.py
#Modelform��һ��modelת����һ��form���
class BookModelForm(forms.ModelForm):
     class Meta:
        model=models.Book
        fields="__all__"
��һ�����������൱������Ĵ���
'''
class BookModelForm(form.Form):
     title=forms.CharField(max_length=32)
     price=forms.IntegerField()
     pub_date=forms.DateField()

'''  
ǰ�˱��ύsubmit��
<button type="button" onclick="doValidation();">�ύ</button>
<input type="button" onclick="doValidation();" value="�ύ"/>




�����
ForeignKey(Teacher,related_name='student_teacher',on_delete=models.CASCADE)
related_name ��ͨ�������ѯ�ֱ���Ϣ�Ĺ����ֶΡ�
teacher = Teacher()
teacher.student_teacher.all()
#Foreign�ĵڶ������м���on_delete=models.CASCADE  �����ϵ���У�����ɾ����
Ҳ���ǵ�ɾ�����������ʱ��ӱ��е�����Ҳ����һ��ɾ����



class Blog(models.Model):
    name = models.CharField(max_length=50, default='default name')
    blog_id = models.IntegerField(default=None,null=True)
    user_id = models.IntegerField(default=1,null=True)
    user_name = models.CharField(max_length=50,default='default name')
    content = models.CharField(max_length=9999,default='����д����')
    create_at = models.IntegerField(default=un_time,null=True)
    def __str__(self):
        return self.name
class Comment(models.Model):
    to_blog_id = models.ForeignKey(Blog,related_name='to_blog_id',on_delete=models.CASCADE)
    comment_user = models.ForeignKey(User,related_name='comment_user',on_delete=models.CASCADE)
    to_user = models.ForeignKey(User,related_name='to_user',on_delete=models.CASCADE)
    content = models.TextField(default='����д����')
    create_at = models.DateTimeField(auto_now = True,null=False)
    def __str__(self):
        return self.comment_user.name + ":" + self.content
# ��������
models.UserInfo.objects.create(name='aaa',age='18',ut_id='1')  # ע�������һ�ж����ñ��ж�ut_id

# ��ѯ����
models.UserInfo.objects.all()

# ����

models.UserInfo.objects.filter(name='xxx')

# ����

models.UserInfo.objects.update(name='ddd')       

MesModel.objects.get(id=1).delete()  
--
ִ���Զ���sql:
from django.db import connection
cursor=connection.cursor()
#�������
cursor.execute("insert into hello_author(name) values('������')")
#���²���
cursor.execute('update hello_author set name='abc' where name='bcd'')
#ɾ������
cursor.execute('delete from hello_author where name='abc'')
#��ѯ����
cursor.execute('select * from hello_author')
raw=cursor.fetchone() #���ؽ�����α�ֱ����ǰ����ȡһ��
cursor.fetchall() #��ȡ����
--------------------------------------------
��ѧϰdjango��ʱ����template��дformʱ�����ִ���Ҫ��{% csrf_token %}�ſ��ԣ�֮ǰһֱҲû�о���ֻ��֪��Ҫ�Ӹ����������������ʲôҲ�����ס�

Ŀ�ģ�
csrf_token ��Ϊ�˷�ֹcsrf����վ����α�죩��ʲô��csrf����ƪ���½��ĺܺã�����������Ҳ˵���ˣ���ֹcsrf���ֶξ��и�form�Ӹ�token��
���򵥵�˵�����Ƿ�ֹ�ڿ͵����������վ��cookie���ϵ��˻��������Ϣ

��������ʲô��
����Ⱦģ��ʱ��django��� {% csrf_token %} �滻��һ��<input type=��hidden��, name=��csrfmiddlewaretoken�� value=������������ɵ�token>Ԫ�ء�
���ύ����ʱ�򣬻�����token���ύ��ȥ��

djangoĬ������ 'django.middleware.csrf.CsrfViewMiddleware���м���� ����м����������֤csrf_token�ġ����û�м�csrf_token���ͻ����

��ֹ��վ���󹥻���csrf_token,�������һ��token���ύ��ʱ������token�ύ��ȥ��ֻ��Я��token���ܼ���ʹ�ñ���

----------------------------------------------------------
���ɾ�������⣺
���Ǩ���ļ� rm -rf app/migrations/* ��app��Ӧ������ģ�����
�� python manage.py makemigrations app ����Ǩ���ļ�
Ȼ��
ɾ��vim app/migrations/0001_initial.py ��Ӧ��������ֶΣ�ֻɾ�������ڱ�Ĳ��֣�
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

���
python manage.py makemigrations
python manage.py migrate
----------------------------------------
    if request.method == 'POST':
        form = DiscussForm(request.POST)
        if form.is_valid():
            blog = Blog.objects.get(blog_id=blog_id)
            #newcomment = request.POST.get('content')
			#cleaned_data �ǻ�ȡ���� input name=content ��value
            newcomment = form.cleaned_data['content']
            #oldcomment = Discuss.objects.get(blog_id=blog_id)
            comment_info = Discuss(to_blog_id=blog,to_user=blog.user_name,comment_user=request.user,content=newcomment)
            comment_info.save()
            redirect_url = "/blog/"+blog_id
            return HttpResponseRedirect(redirect_url,{"form":form})
        return HttpResponseRedirect("/blog/"+blog_id)

������������ƶ��ֶα����� ���ʵ�������Ǿ�����ֶ���Ϣ��
-------------------------------------------------------------------
django META ����
1�������� abstract
�ؼ��֣�
    class Meta:
        abstract=True

���룺
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
HUman��һ�������࣬���������ݿ��н���Employee��Cunstomer �̳�Human����������ᴴ����Human����Ϊһ���������ԡ�

2��ָ��Ӧ�ã���Щʱ��ģ���಻���Լ�Ӧ�õ� models.py�У���Ҫָ��app
app_label='myapp' 

3�������model�����ݿ��еı����� db_table
db_table = 'Students'

4����ռ����� db_teblespace
�����setting���趨��ʹ�����ֵ

5��get_latest_by ����ģ������ DateField �� DateTimeField ���͵��ֶΣ������ͨ�����ѡ����ָ��lastest()�ǰ����ĸ��ֶν���ѡȡ�ġ�
get_latest_by = "order_date"����ģ�齫ӵ��һ�� get_latest() �����Եõ� "���µ�" ����

6��manged
����Django���Զ�����ģ��������ӳ������ݿ������㲻ϣ��Django��ô�������԰�managed��ֵ����ΪFalse

7��ordering �����Ǹ��ֶ�����
ordering=['order_date'] # ��������������
ordering=['-order_date'] # �������������У�-��ʾ����
ordering=['?order_date'] # ������򣬣���ʾ��� 

8��permissions
������������Կ�����ָ���ķ���Ȩ�������������ɶ���Django�Զ�Ϊÿ��������admin�Ķ��󴴽���ӣ�ɾ�����޸ĵ�Ȩ�ޡ�
permissions = (('can_deliver_pizzas','Can deliver pizzas'))

9�����ֶν�� ������Ψһ��
unique_together = (("first_name", "last_name"),)

10��verbose_name
�����ģ������һ�����ɶ�������һ�㶨��Ϊ���ģ�verbose_name = "ѧУ"��

11��verbose_name_plural
ģ�͵ĸ�����ʽ��verbose_name_plural = "ѧУ"�������ָ��Django���Զ���ģ�����ƺ��һ����s��
------------------------------------------------
����1��TypeError: expected string or buffer�����ʹ���:Ԥ�ڵ��ַ����򻺳�����
�ַ�ƴ��ʱֱ����""��д�˱�������ɣ�Ӧ���ȶ������Ȼ���� ""+����+""
����2��Not all parameters were used in the SQL statement�����������еı�����ʹ�ã�
cursor.executemany �����ô��ˡ�
����3��1265 Data truncated for column at row 1�������������
�������͸�ΪTextField





�ַ���ƴ�ӣ� str = 'There are'+fruit1+','+fruit2+','+fruit3+' on the table' 

@python ��������mysql
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
@ʵʱ��ʾʱ��
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

        document.getElementById("navbar_time").innerHTML = yy+"��"+mo+"��"+dd+"��"+"   "+hh+":"+mm+":"+ss;
        }
    function extra(x) {
        if(x < 10){
            return "0" + x;
        }else{
            return x;
        }
    }
    </script>
@��ʾ����������
<table class="table table-hover form-group hovertable" vcontext="subusers.table" id="tableSort">	 #id
     <th onclick="$.sortTable.sort('tableSort',9)" style="cursor: pointer;">�û�����</th>
     <th onclick="$.sortTable.sort('tableSort',10)" style="cursor: pointer;">CPU</th>        		 #sortTable �����򷽷�


js 	 ��Ԫ������css
  .abc {
    background: red;
    }
test div
    var div = document.getElementById('d1');
    div.setAttribute("className", "abc");	 
	 
���ֶα�ע


 $(this).next('ul').toggleClass('active')
 toggleclass ��������˼�� �л������Ӻ�ɾ��active class

��ȡ��Ԫ�أ�
$(document).ready(function(){
  $("div").children("p.1");
});

$(document).ready(function(){
  $("div").find("span");
});
 
 
----------------------------------------------------------------------------
app ģ���޷��������⣬����Ϊ������Ŀ��֪��source root��ʲô��
���������
pycharm ������MARK directory as source root
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

����ķ�����

1������favicon.ico�ļ����ڸ�Ŀ¼�£���head��ǩ����favicon.ico�ļ�����

<link href="favicon.ico" rel="shortcut icon">

-------------------------------------------------------
###�ֲ�ʽ�첽����

celery+redis  ʵ�ֲַ�ʽ�첽�������ٸ����ӣ������ҳ���Ϸ����ʼ�(�ֻ���֤��)���ܣ�ҳ��������Ҫ��ʾ����������������첽�ں�̨����ִ�У����û��и��õ����飩
pip install celery
pip install redis
celery�� ��python���Կ����ģ������²�����ɣ�
1������task��python����
2������queue������Ҫִ�е�����ӵ������У�������ϸ��Ϣ���� redis ����key value ����ʽ�洢��
3������worker����һ���µĽ����У�����ִ�ж����е�����
4��������broker��������ȣ�һ����redis rabbit
��ע��celery����û����Ϣ�洢�����ȹ��ܣ�ֻ��������첽ִ�У���Ҫ����Ϣ����һ��ʹ�á�

ִ�й��̣�
client �˲�������task��Ȼ��ŵ�queue�����У�������redis��֪ͨ�����������񣬿��е�worker��ȥ�Ӷ�����ȡ���������ִ�С�
celery �� redis ֮�佻���Ļ���ԭ��
1��������һ�� task ʱ������ redis �� celery key �в���һ����¼��
2�������ʱ�����ڴ����Ŀ��� worker����� task �������� worker ��ȡ��
3�������ʱû�п��е� worker����� task �ļ�¼�ᱣ���� celery key �С�
4����ʱ�Ὣ��� task �ļ�¼�� key celery ���Ƴ�������������Ϣ�� unacked �� unacked_index �С�
5��worker ���� task �趨������ִ��ʱ��ִ����������ӵ��Ĳ�����ʱ��������Ѿ�����������ʱ�䣬������ִ�С�
6��worker ��ʼִ������ʱ��֪ͨ redis������������� CELERY_ACKS_LATE = True ��ô��������ִ�н���ʱ��֪ͨ��
7��redis �ӵ�֪ͨ�󣬽� unacked �� unacked_index ����ؼ�¼�Ƴ���
8������ڽӵ�֪ͨǰ��worker �ж��ˣ���ʱ redis �е� unacked �� unacked_index ��¼�����»ص� celery key �С�(�����д�Ĳ������� worker �� �������� ǰ�Լ���ɵģ������ڹر� worker ʱΪ��ֹ����ʧ�������ʹ����ȷ�ķ���ֹͣ������: celery multi stop w1 -A proj1)
9���� celery key �е� task �����ٴ��ظ����� 2 ���µ����̡�



###redis��ҳ�滺��
yum -y isntall redis-server
��֤��
vim /etc/redis.conf
requirepass django
1,redis-cli -h 127.0.0.1 -p 6379 -a reson
2,
$redis-cli 
>auth django
>get a
-----------------------------------------
view �������룺
������Ǹ�ϲ��͵���ĳ���Ա�����ô��뿴�������Ӽ������������� Python ���ڽ����� locals() ��
�����ص��ֵ�����оֲ�������������ֵ����ӳ�䡣 ��ˣ�ǰ�����ͼ������д������������ӣ�
def current_datetime(request):
  current_date = datetime.datetime.now()
  return render_to_response('current_datetime.html', locals())