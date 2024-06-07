from django.db import models


class Manage(models.Model):
    id = models.AutoField(primary_key=True)
    user_number = models.CharField(max_length=32, verbose_name='账号')
    user_password = models.CharField(max_length=32, verbose_name='密码')
    user_name = models.CharField(max_length=32, verbose_name='名字')

    class Meta:
        db_table = 'manage'


class Publisher(models.Model):

    publisher_name = models.CharField(max_length=32, verbose_name='出版社名称')
    publisher_address = models.CharField(max_length=32, verbose_name='出版社地址')

    class Meta:
        db_table = 'publisher'


class Author(models.Model):

    author_name = models.CharField(max_length=32, verbose_name='作者名')
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')

    class Meta:
        db_table = 'author'


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, verbose_name='书名')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='作者')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='价格')
    inventory = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='库存')
    sale_num = models.DecimalField(max_digits=10, decimal_places=0, verbose_name='销量')
    publisher = models.ForeignKey(to=Publisher, on_delete=models.CASCADE, verbose_name='出版社')

    class Meta:
        db_table = 'book'


# python manage.py makemigrations
# python manage.py migrate

