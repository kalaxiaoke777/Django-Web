# Django-Web
基于Django框架的Web项目，用于展示和分享各种编程语言的代码。

## 安装

确保已安装Python 3.9或更高版本，并已安装Django 3.2或更高版本

数据库只针对业务层

依赖包执行
pip install django-cors-headers django proj Geoip GEOS

外部安装：
geodjango
osgeo4安装：https://trac.osgeo.org/osgeo4w/

OSGeo4W installer 可以帮助安装 GeoDjango 所需的 PROJ、GDAL 和 GEOS 库。首先，下载 OSGeo4W installer 并运行它。选择 Express Web-GIS Install 然后点击下一步。在 'Select Packages' 列表中，确保选择了 GDAL。如果默认启用了其他任何软件包，它们对于 GeoDjango 是不需要的，可以安全地取消选中。点击下一步并接受许可协议后，软件包将被自动下载和安装，然后您可以退出安装程序。

批处理配置环境变量
-
set OSGEO4W_ROOT=C:\OSGeo4W64
set GDAL_DATA=%OSGEO4W_ROOT%\share\gdal
set PROJ_LIB=%OSGEO4W_ROOT%\share\proj
set PATH=%PATH%;%OSGEO4W_ROOT%\bin
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path /t REG_EXPAND_SZ /f /d "%PATH%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v GDAL_DATA /t REG_EXPAND_SZ /f /d "%GDAL_DATA%"
reg ADD "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v PROJ_LIB /t REG_EXPAND_SZ /f /d "%PROJ_LIB%"
## 开发环境