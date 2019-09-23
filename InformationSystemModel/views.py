from django.shortcuts import render

# Create your views here.
from InformationSystemModel import models       #导入blog模块
from django.shortcuts import HttpResponse

'''
# creat
def db_handle(request):
    # models.UserInfo.objects.create(username='andy',password='123456',age=33)
    dic = {"username":"bruce","password":"123456","age":23}
    models.UserInfo.objects.create(**dic)
    return HttpResponse('OK')

# read
def db_handle(request):
    user_list_obj = models.UserInfo.objects.all()
    return render(request,'t1.html',{'li':user_list_obj})

# update
def db_handle(request):
    models.UserInfo.objects.filter(id=1).update(age=18) #找到id=1的数据，将age改为18
    return HttpResponse('OK')

# delete
def db_handle(request):
    models.UserInfo.objects.filter(id=2).delete()
    return HttpResponse('OK')
'''

def hello(request):
    return HttpResponse("Hello world ! ")

def db_handle(request):
    if request.method == "POST":
        models.UserInfo.objects.create(username=request.POST['username'],password=request.POST['password'],age=request.POST['age'])
    user_list_obj = models.UserInfo.objects.all()
    return render(request, 't1.html', {'li': user_list_obj})
