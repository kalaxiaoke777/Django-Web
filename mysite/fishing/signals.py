from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        # 在此处可以添加你想要的逻辑，例如创建新的记录、修改属性等。
        # 你可以访问 instance 的属性和方法来获取有关创建的用户的信息。

        # 示例：创建一个相关的 UserProfile 对象
        UserProfile.objects.create(user=instance)
