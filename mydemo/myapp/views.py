from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Users

# Create your views here.
def index(request):
    
    # 添加操作
    # ob = Users()
    # ob.name = "yaya"
    # ob.age = 13
    # ob.phone = 1321231231
    # ob.save() # 新对象就是添加，已存在对象则是修改
    
    # 删除操作
    # mod = Users.objects # 获取users的model对象
    # user = mod.get(id=1) # 获取id对应的数据信息
    # print(user.name)
    # user.delete() 
    
    # 修改操作
    # ob = Users.objects.get(id=2)
    # print(ob.name)
    # ob.name = "bb"
    # ob.age = 26
    # ob.save()
    
    # 数据查询
    # mod = Users.objects # 获取Users模型的Model操作对象
    # ulist = mod.all() # 获取所有数据
    # ulist = mod.filter(age__gte=12)
    # ulist = mod.order_by("age")[:3] # 按age升序排序，只获取前3条
    
    # for u in ulist:
    #     print(u.id, u.name, u.age, u.phone, u.addtime)
    
    return HttpResponse("首页")

# 浏览用户信息
def indexUsers(request):
    try:
        ulist = Users.objects.all()
        context = {"userslist":ulist}
        return render(request, "myapp/users/index.html", context) # 加载模板
    except:
        return HttpResponse("没有找到用户信息！")
    
# 加载添加用户信息表单
def addUsers(request):
    return render(request, "myapp/users/add.html")

# 执行用户信息添加
def insertUsers(request):
    try:
        ob = Users()
        # 从表单中获取要添加的信息并封装到ob对象中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save() # 执行保存
        context = {"info":"添加成功！"}
    except:
        context= {"info":"添加失败！"}
    return render(request, "myapp/users/info.html", context)
    
# 执行用户信息删除
def delUsers(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)
        ob.delete() # 执行删除操作
        context = {"info":"删除成功！"}
    except:
        context= {"info":"删除失败！"}
    return render(request, "myapp/users/info.html", context)
# 加载用户信息修改表单
def editUsers(request, uid=0):
    try:
        ob = Users.objects.get(id=uid)
        context = {"user":ob}
        return render(request, "myapp/users/edit.html", context)
    except:
        context= {"info":"没有找到要修改的数据！"}
        return render(request, "myapp/users/info.html", context)
# 执行用户信息修改
def updateUsers(request):
    try:
        uid = request.POST['id']
        ob = Users.objects.get(id=uid)
        # 从表单中获取要添加的信息并封装到ob对象中
        ob.name = request.POST['name']
        ob.age = request.POST['age']
        ob.phone = request.POST['phone']
        ob.save() # 执行保存
        context = {"info":"修改成功！"}
    except:
        context= {"info":"修改失败！"}
    return render(request, "myapp/users/info.html", context)