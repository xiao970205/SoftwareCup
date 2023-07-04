from django.http import JsonResponse, Http404
from django.shortcuts import render, HttpResponse, redirect
import json
import os
import chardet


# 文件下载，可以通过get传入参数。
def download_file(requests):
    # 接受传入的参数
    print(requests.GET.get("name"))
    # 服务器上存放文件的路径
    file_path = r"D:\2023年上半年英语六级笔试准考证(130102199702052111).pdf"
    try:
        r = HttpResponse(open(file_path, "rb"))
        print(r)
        r["content_type"] = "application/octet-stream"
        r["Content-Disposition"] = "attachment;filename=1.pdf"
        return r
    except Exception:
        raise Http404("Download error")


def up_file(request):
    # 获取json文件对象
    File = request.FILES.get('file_name')
    filename = os.path.join("D:\\", File.name)
    with open(filename, "wb+") as f:
        data = File.file.read()
        f.write(data)
    data = {
        'name': 'Tony',
        'age': 18,
        'gender': 'male'
    }
    return JsonResponse(data)


def uploadPage(request):
    # 重定向，定向到user_list页面
    return render(request, "uploads.html")


# 测试json格式数据的接受和返回。
def get_post_info_test(request):
    data = json.loads(request.body)
    print(data)
    print(data.get("name"))
    data = {
        'name': '张三',
        'age': 18,
        'gender': 'male'
    }

    return JsonResponse(data)


# Create your views here.
def login(request):
    # 重定向，定向到user_list页面
    return redirect("/user_list")


def user_list(request):
    print(request.method)
    print(request.GET)
    print(request.POST)

    # return HttpResponse("你好")

    # 传入参数
    user_name = "tom"
    data_list = ["tom", "lisa", "david"]
    data_dict = {"user": "tom", "age": 18, "height": 180}
    return render(request, "user.html", {"user": user_name, "user_list": data_list, "user_info": data_dict})


def pic(request):
    return render(request, "pic.html")
