from django.test import TestCase
from InformationSystemModel import models       #导入blog模块
from django.shortcuts import HttpResponse

# Create your tests here.

#递归排序建树
def buildTreeSort(inputList, outputList, pid = 0):
    for var in inputList:
        if var.PID == pid:
            outputList.append(var)
            buildTreeSort(inputList,outputList,var.ID)

#在树中新建一项
def treeCreat(pid, name):
    #重复判断 已存在的就不再添加
    temp = models.Tree.objects.filter(PID = pid, Name = name)
    if temp.count() != 0:
        return False
    parent = models.Tree.objects.get(ID = pid)
    layer = parent.Layer + 1
    dic = {"PID":pid,"Name":name,"Layer":layer}
    models.Tree.objects.create(**dic)
    return True

#根据id删除树中一项
def treeDelete(id):
    models.Tree.objects.filter(ID = id).delete()



#根据ID、Layer进行关联表查询
def getMessage(id, layer):
    output = []
    if layer == 2:
        output = models.FXT.objects.get(ID = id)
    else:
        return output, False
    return output, True



#数据库测试
def Test(request):

    #树中新创建一项
    #treeCreat(2,"测试测试1")

    #树中删除一项
    treeDelete(18)

    #建树
    #初始化
    sortList = []
    response = "Layer  Name  ID  <br/>"
    response1 = ""

    # 通过objects这个模型管理器的all()获得所有数据行，相当于SQL中的SELECT * FROM
    list = models.Tree.objects.all()
    #建树
    buildTreeSort(list,sortList,0)

    # 输出所有数据 
    for var in sortList:
        response1 += str(var.Layer) + "  " + var.Name+ "  "+ str(var.ID) + "<br/>"
    response += response1



    #其他表查询
    #response += "查询id=3，layer=2的对象<br/>"
    #out, isOK = getMessage(3,2)
    #if isOK == 1:
    #    response += str(out.ID) + " " + out.temp1 +" " + out.temp2  + "<br/>"

    

    return HttpResponse("<p>" + response + "</p>")