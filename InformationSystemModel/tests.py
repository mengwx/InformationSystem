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

    if pid == 0:
        dic = {"PID": pid, "Name": name, "Layer": 1}
        models.Tree.objects.create(**dic)
        dic = {"ID": models.Tree.objects.get(PID=pid, Name=name).ID, "Name": name}
        models.XT.objects.create(**dic)
        return
    parent = models.Tree.objects.filter(ID = pid)
    if parent.count() == 0:
        return False
    layer = parent[0].Layer + 1
    if layer > 5:
        return
    dic = {"PID":pid,"Name":name,"Layer":layer}
    models.Tree.objects.create(**dic)

    if layer == 2:
        dic = {"ID":models.Tree.objects.get(PID = pid, Name = name).ID,"Name":name}
        models.FXT.objects.create(**dic)
    if layer == 3:
        dic = {"ID":models.Tree.objects.get(PID = pid, Name = name).ID,"Name":name}
        models.ZXT.objects.create(**dic)
    if layer == 4:
        dic = {"ID":models.Tree.objects.get(PID = pid, Name = name).ID,"Name":name}
        models.DJ.objects.create(**dic)
    if layer == 5:
        dic = {"ID":models.Tree.objects.get(PID = pid, Name = name).ID,"Name":name}
        models.BZJ.objects.create(**dic)

    return True

#根据id删除树中一项
def treeDelete(id):
    deleteObj = models.Tree.objects.filter(ID = id)
    if deleteObj.count() == 0:
        return
    if deleteObj[0].Layer == 1:
        models.XT.objects.filter(ID=id).delete()
    if deleteObj[0].Layer == 2:
        models.FXT.objects.filter(ID=id).delete()
    if deleteObj[0].Layer == 3:
        models.ZXT.objects.filter(ID=id).delete()
    if deleteObj[0].Layer == 4:
        models.DJ.objects.filter(ID=id).delete()
    if deleteObj[0].Layer == 5:
        models.BZJ.objects.filter(ID=id).delete()
    deleteObj.delete()



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
    treeCreat(222,"测试测试1")

    #树中删除一项
    #treeDelete(22)

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