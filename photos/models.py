from email.mime import image
from turtle import update
from unicodedata import category, name
from django.db import models

# Create your models here.
class Images(models.Model):
    image = models.ImageField(upload_to = 'photos/',default="",null=True)
    name = models.CharField(max_length=50,null=True)
    description = models.CharField(max_length=100,null=True)
    # location = models.ForeignKey(Location,on_delete=models.RESTRICT,)
    # category = models.ForeignKey(Category, on_delete=models.RESTRICT,)


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
    # @classmethod
    # def search_image_by_id(cls,search_term):
    #     try:
    #     category = Images.objects.get(id = image_id)
    # except ObjectDoesNotExist:
    #     raise Http404()
    # return images
    