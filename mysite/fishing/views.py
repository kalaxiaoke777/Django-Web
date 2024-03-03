from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import GEOSGeometry
from django.db import connection

@csrf_exempt 
def addPoint(request):
    """
    1.添加点操作(post)
    2.存入数据库
    3.刷新geoserver服务
    """
    with connections['fish'].cursor() as cursor:
        cursor.execute(
                "SELECT * FROM fishing_user"
            )
        rows = cursor.fetchall()
        for row in rows:
            # 处理查询结果
            print(row)
    return JsonResponse(
                    {
                        "message": "查询成功",
                        "code": 200,
                        "success": True,
                    }
                )
    # point = GEOSGeometry(f'POINT({} {})')
    # with connections["fish"].cursor() as cursor:


def updataPoint(request):
    pass


def deletePoint(request):
    pass


def fieldName(request):
    """
    用于渲染表单类(get)
    读取数据库的元数据
    """
    try:
        with connections["fish"].cursor() as cursor:
            cursor.execute(
                "SELECT * FROM fishing_user"
            )
            # 获取查询结果的列信息
            columns = [desc[0] for desc in cursor.description]
            field_list = []
            # 打印列名和数据类型
            for row in cursor.fetchall():
                field_list.append({
                    "id":row[columns.index("user_id")],
                    "name": row[columns.index("english")], 
                    "field": row[columns.index("chinese")], 
                    "type": row[columns.index("type")]
                    })
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
