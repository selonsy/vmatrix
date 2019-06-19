from django.db import models


class Password(models.Model):
    order_num = models.IntegerField(
        '序号', default=99, help_text='序号可以用来调整顺序，越小越靠前')
    name = models.CharField('名称', max_length=20)
    password = models.CharField('密码', max_length=20)
    reg_email = models.CharField('注册邮箱', max_length=20)
    reg_phone = models.CharField('注册手机', max_length=20)
    question = models.CharField('密保问题', max_length=20)
    answer = models.CharField('密保答案', max_length=20)
    remark = models.CharField('备注', max_length=20)

    class Meta:
        verbose_name = '密码'
        verbose_name_plural = verbose_name
        ordering = ['order_num', 'id']

    def __str__(self):
        return self.name
