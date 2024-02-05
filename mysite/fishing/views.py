from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections


# Create your views here.
def addPoint(request):
    with connections["default"].cursor() as cursor:
        cursor.execute("SELECT * FROM xian")
        result = cursor.fetchall()
        if result:
            return HttpResponse(result[0])
        else:
            return HttpResponse("No data")
