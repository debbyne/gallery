from email.mime import image
# from turtle import update
from unicodedata import category, name
from django.db import models

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

    def save_location(self):
        self.save()
    
    def delete_location(self):

        self.delete()

    @classmethod
    def update_location(cls ,id ,name):
      return cls.objects.filter(id = id).update(name = name)

class Category(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name

    def save_category(self):
        self.save()
    
    def delete_category(self):

        self.delete()
    @classmethod
    def update_category(cls ,id ,name):
      return cls.objects.filter(id = id).update(name = name)



class Images(models.Model):
    image = models.ImageField(upload_to = 'photos/',default="",null=True)
    name = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=100,null=True)
    location = models.ForeignKey(Location,on_delete=models.RESTRICT,)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT,)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()

    @classmethod
    def update_image(cls ,id ,image):
        return cls.objects.filter(id = id).update(image = image)
    @classmethod
    def get_image_by_id(cls,id):
        return cls.objects.filter(id = id).all
    @classmethod
    def search_image_by_category(cls,category):
        images = cls.objects.filter(category)
        return images
    # try:
    #     category = Category.objects.get(category_name_icontains = category )
    # except Category.DoesNotExist:
    #     return images
    
    @classmethod
    def filter_by_location(cls, location):
        return cls.objects.filter(location=location).all()
    