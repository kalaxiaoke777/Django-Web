from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections


def addPoint(request):
    """
    1.添加点操作
    2.存入数据库
    3.刷新geoserver服务
    """
    with connections["fish"].cursor() as cursor:
        cursor.execute("SELECT * FROM fishing_spots")
        result = cursor.fetchall()
        if result:
            return HttpResponse(result[0])
        else:
            return HttpResponse("No data")


def updataPoint(request):
    pass


def deletePoint(request):
    pass


def fieldName(request):
    """
    用于渲染表单类
    读取数据库的元数据
    """
    try:
        with connections["fish"].cursor() as cursor:
            cursor.execute(
                "SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'fishing_spots'"
            )
            # 获取查询结果的列信息
            columns = [desc[0] for desc in cursor.description]
            field_list = []
            # 打印列名和数据类型
            for row in cursor.fetchall():
                column_name, data_type = row
                field_list.append({"field": column_name, "type": data_type})
            if len(field_list) > 0:
                return JsonResponse(
                    {
                        "message": "查询成功",
                        "field_list": field_list,
                        "code": 200,
                        "success": True,
                    }
                )
            else:
                return JsonResponse(
                    {
                        "message": "查询失败",
                        "field_list": None,
                        "code": 500,
                        "success": False,
                    }
                )
    except Exception as e:
        return JsonResponse(
            {
                "message": "数据库连接失败",
                "code": 505,
                "success": False,
            }
        )
