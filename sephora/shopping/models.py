from django.db import models

# Create your models here.


class Products(models.Model):
    title=models.CharField(max_length=200, verbose_name='عنوان')
    description=models.TextField(verbose_name='توضیحات')
    price=models.IntegerField(verbose_name='قیمت')
    price_off=models.IntegerField(verbose_name='قیمت تخقیف',null=True)
    ratting=models.IntegerField(default=0, verbose_name='امتیاز')
    slug=models.SlugField(null=True,blank=True,unique=True)
    code=models.CharField(max_length=7, null=True, verbose_name='کد کالا')
    created=models.DateField(auto_now_add=True,verbose_name='تاریخ ایجاد', null=True)
    image=models.ImageField(upload_to='products',null=True)


    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title