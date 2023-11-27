from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator
from autoslug import AutoSlugField

# Create your models here.


class Products(models.Model):
    title=models.CharField(max_length=200, verbose_name='عنوان')
    description=models.TextField(verbose_name='توضیحات')
    price=models.IntegerField(verbose_name='قیمت')
    price_off=models.IntegerField(verbose_name='قیمت تخقیف',null=True)
    ratting=models.IntegerField(default=1, verbose_name='امتیاز',validators=[MinValueValidator(1),MaxValueValidator(5)])
    slug= AutoSlugField(populate_from='title',editable=False, always_update=True)
    code=models.CharField(max_length=7, null=True, verbose_name='کد کالا')
    created=models.DateField(auto_now_add=True,verbose_name='تاریخ ایجاد', null=True)
    image=models.ImageField(upload_to='products',null=True)



    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title



class Imageofslider(models.Model):
    title=models.CharField(max_length=100,verbose_name='عنوان')
    short_description=models.CharField(max_length=150,verbose_name='توضیح کوتاه')
    description=models.TextField(verbose_name='توضیح ')
    image=models.ImageField(upload_to='slider')
    created=models.DateField(auto_now_add=True,verbose_name='تاریخ ایجاد', null=True)

    
    class Meta:
        verbose_name = 'عکس اسلایدر'
        verbose_name_plural = 'اسلایدر'

    def __str__(self):
        return self.title