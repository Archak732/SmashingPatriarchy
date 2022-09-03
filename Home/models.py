from django.db import models

# Create your models here.
class About(models.Model):
    about= models.CharField(max_length=200)
    image = models.CharField(max_length=100)


    def __str__(self):
        return self.about

    



class Contact(models.Model):
    name= models.CharField(max_length=20)
    email=models.EmailField()
    address= models.CharField(max_length=50)
    message   = models.TextField()


    def __str__(self):
        return self.name


class Homee(models.Model):
    title=models.CharField(max_length=50)
    image = models.CharField(max_length=500)   

    def __str__(self):
        return self.title



class Teamm(models.Model):
    name=models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    about=models.CharField(max_length=50)
    image = models.CharField(max_length=100)   

    def __str__(self):
        return self.name
    
    

