import json

from Futils.fishing.PointTools import Fpoint
from shapely import wkt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseNotAllowed
from django.db import connections
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def addPoint(request):
    """
    1.添加点操作(post)
    2.存入数据库
    3.刷新geoserver服务
    """
    if request.method == "POST":
        # 解析数据
        json_data = json.loads(request.body)
        if "user_review" not in json_data:
            user_review = ""
        else:
            user_review = json_data["user_review"]
        geom = json_data["geom"]
        spot_name = json_data["spot_name"]
        openning_time = json_data["openning_time"]
        end_time = json_data["end_time"]
        spot_area = json_data["spot_area"]
        locations = json_data["locations"]
        spot_type = json_data["spot_type"]
        address = json_data["address"]
        r_rating = json_data["r_rating"]
        overview = json_data["overview"]
        facilities = json_data["facilities"]
        fish_active = json_data["fish_active"]
        # 检查数据

        check_result = Fpoint(geom, spot_name)
        result = check_result.check_data()
        if result["type"] is False:
            return JsonResponse(
                {
                    "message": result["message"],
                    "code": 400,
                    "success": False,
                }
            )
    else:
        return HttpResponseNotAllowed(["POST"])
    with connections["fish"].cursor() as cursor:

        cursor.execute(
            "INSERT INTO fishing_spots (geom, spot_name, openning_time, end_time, spot_area, locations, spot_type, address, user_review, r_rating, overview, facilities, fish_active) VALUES (ST_GeomFromText(%s, 4490), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [
                geom,
                spot_name,
                openning_time,
                end_time,
                spot_area,
                locations,
                spot_type,
                address,
                user_review,
                r_rating,
                overview,
                facilities,
                fish_active,
            ],
        )
    return JsonResponse(
        {
            "message": "添加成功",
            "code": 200,
            "success": True,
        }
    )
    # point = GEOSGeometry(f'POINT({} {})')
    # with connections["fish"].cursor() as cursor:


def updataPoint(request):
    pass


@csrf_exempt
def deletePoint(request):
    """
    删除逻辑
    """
    try:
        json_data = request.GET.get("fid")
        with connections["fish"].cursor() as cursor:
            # 根据提供的 ID 删除数据
            delete_query = f"DELETE FROM fishing_spots WHERE id = {json_data};"
            cursor.execute(delete_query)
            connections["fish"].commit()
            print("Data deleted successfully!")
        return JsonResponse(
            {
                "message": "查询成功",
                "code": 200,
            }
        )
    except Exception as e:
        return HttpResponse(e)
    pass


def fieldName(request):
    """
    用于渲染表单类(get)
    读取数据库的元数据
    """
    try:
        with connections["fish"].cursor() as cursor:
            cursor.execute("SELECT * FROM fishing_user")
            # 获取查询结果的列信息
            columns = [desc[0] for desc in cursor.description]
            field_list = []
            # 打印列名和数据类型
            for row in cursor.fetchall():
                field_list.append(
                    {
                        "id": row[columns.index("user_id")],
                        "name": row[columns.index("english")],
                        "field": row[columns.index("chinese")],
                        "type": row[columns.index("type")],
                    }
                )
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
