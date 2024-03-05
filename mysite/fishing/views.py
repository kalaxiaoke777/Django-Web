import json
from shapely import wkt
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse,HttpResponseNotAllowed
from django.db import connections
from django.views.decorators.csrf import csrf_exempt
from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.geos import Point
def check_data(geom,spot_name):
    """
    检查数据是否符合中国坐标系标准
    """
    chiniGeometry = {
        "min_E":73.5,
        "max_E":135.0,
        "min_N":15.5,
        "max_N":55.0
    }
    # 创建Geometry对象
    geom = wkt.loads(geom)
    # 提取坐标
    coordinates = geom.coords[0]
    if (coordinates[0] > chiniGeometry["min_E"] and coordinates[0] < chiniGeometry["max_E"]) or (coordinates[1] > chiniGeometry["min_N"] and coordinates[1] < chiniGeometry["max_N"]):
        return {
        "type": True,
        "message": ""
    }
    if spot_name is None or spot_name == '':
        return {
            "type": False,
            "message": "spot_name不能为空"
        }
    return {
        "type": True,
        "message": ""
    }
@csrf_exempt 
def addPoint(request):
    """
    1.添加点操作(post)
    2.存入数据库
    3.刷新geoserver服务
    """
    if request.method == 'POST':
        # 解析数据
        json_data = json.loads(request.body)
        if "user_review" not in json_data:
            user_review=""
        else:
            user_review=json_data["user_review"]
        geom=json_data["geom"]
        spot_name=json_data["spot_name"]
        openning_time=json_data["openning_time"]
        end_time=json_data["end_time"]
        spot_area=json_data["spot_area"]
        locations=json_data["locations"]
        spot_type=json_data["spot_type"]
        address=json_data["address"]
        r_rating=json_data["r_rating"]
        overview=json_data["overview"]
        facilities=json_data["facilities"]
        fish_active=json_data["fish_active"]
        # 检查数据
        check_result = check_data(geom,spot_name)
        if check_result["type"] is False:
            return JsonResponse(
                        {
                            "message": check_result["message"],
                            "code": 400,
                            "success": False,
                        }
                    )
    else:
        return HttpResponseNotAllowed(['POST'])
    with connections['fish'].cursor() as cursor:
        cursor.execute(
            "INSERT INTO fishing_spots (geom, spot_name, openning_time, end_time, spot_area, locations, spot_type, address, user_review, r_rating, overview, facilities, fish_active) VALUES (ST_GeomFromText(%s, 4490), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [geom, 
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
            fish_active]
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
