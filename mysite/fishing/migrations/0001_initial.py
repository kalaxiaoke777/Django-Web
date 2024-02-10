from django.db import migrations


def add_initial_values(apps, schema_editor):
    User = apps.get_model("fishing", "User")
    User.objects.create(
        english="spot_name",
        chinese="渔场名称",
    )
    User.objects.create(
        english="openning_time",
        chinese="营业时间",
    )
    User.objects.create(
        english="spot_area",
        chinese="水域面积",
    )
    User.objects.create(
        english="r_rating",
        chinese="推荐指数",
    )
    User.objects.create(
        english="fish_active",
        chinese="鱼情",
    )
    User.objects.create(
        english="adress",
        chinese="地址",
    )
    User.objects.create(
        english="user_review",
        chinese="用户评价",
    )
    User.objects.create(
        english="facilities",
        chinese="设施情况",
    )
    User.objects.create(
        english="overview",
        chinese="简介",
    )
    User.objects.create(
        english="locations",
        chinese="地理位置",
    )


class Migration(migrations.Migration):

    dependencies = [
        ("fishing", "0001_initial"),  # 指定之前的迁移文件
    ]

    operations = [
        migrations.RunPython(add_initial_values),
    ]
