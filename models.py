from django.db import models

# Create your models here.
class contactus(models.Model):
    name=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=100,null=True)
    mobile=models.CharField(max_length=25,null=True)
    message=models.TextField(null=True)
    def __str__(self):
        return self.name


class slider(models.Model):
    headlines=models.TextField()
    slider_dec=models.TextField()
    slider_picture=models.ImageField(upload_to='static/slider',null=True)
    def __str__(self):
        return self.headlines

class category(models.Model):
    category_name=models.CharField(max_length=200,null=True)
    category_picture=models.ImageField(upload_to='static/category/',null=True)
    def __str__(self):
        return self.category_name

class city(models.Model):
    city_name=models.CharField(max_length=100,null=True)
    city_picture=models.ImageField(upload_to='static/city/',null=True)
    def __str__(self):
        return self.city_name

class mynews(models.Model):
    news_category=models.ForeignKey(category,on_delete=models.CASCADE)
    news_city=models.ForeignKey(city,on_delete=models.CASCADE)
    news_picture=models.ImageField(upload_to='static/news/',null=True)
    news_headlines=models.TextField()
    news_description=models.TextField()
    news_date=models.DateField()

class vnews(models.Model):
    vcategory=models.ForeignKey(category,on_delete=models.CASCADE)
    city=models.ForeignKey(city,on_delete=models.CASCADE)
    headlines=models.TextField(null=True)
    news=models.TextField(null=True)
    vlink=models.CharField(max_length=300,null=True)
    newsdate=models.DateField()

class jobs(models.Model):
    job_title=models.CharField(max_length=200,null=True)
    job_link=models.CharField(max_length=200,null=True)
    job_picture=models.ImageField(upload_to='static/jobs',null=True)


