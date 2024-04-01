from shapely import wkt


class Fpoint:
    chiniGeometry = {"min_E": 73.5, "max_E": 135.0, "min_N": 15.5, "max_N": 55.0}

    def __init__(self, geom, spot_name):
        self.geom = geom
        self.spot_name = spot_name

    def check_data(self):
        """
        检查数据是否符合中国坐标系标准
        """
        # 创建Geometry对象
        geom = wkt.loads(self.geom)
        # 提取坐标
        coordinates = geom.coords[0]
        if (
            coordinates[0] > self.chiniGeometry["min_E"]
            and coordinates[0] < self.chiniGeometry["max_E"]
        ) or (
            coordinates[1] > self.chiniGeometry["min_N"]
            and coordinates[1] < self.chiniGeometry["max_N"]
        ):
            return {"type": True, "message": ""}
        if self.spot_name is None or self.spot_name == "":
            return {"type": False, "message": "spot_name不能为空"}
        return {"type": True, "message": ""}
