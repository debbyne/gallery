from django.test import TestCase
from .models import Images,Category,Location

# Create your tests here.
class CategoryTestClass(TestCase):
    def setUp(self):
        self.test_category= Category(name = 'fashion')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test_category,Category))

     # Testing Save Method
    def test_update_category(self):
        self.test_category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(Category.objects.all()) ==1)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(Category.objects.all()) ==1)

class LocationTestClass(TestCase):
    def setUp(self):
        self.test_location= Location(name = 'nakuru')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.test_location,Location))

     # Testing Save Method
    def test_save_location(self):
        self.test_location.save_location()
        location = Location.objects.all()
        self.assertTrue(len(Category.objects.all()) ==1)

    def test_delete_location(self):
        self.test_location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(Location.objects.all()) ==1)

class ImageTestClass(TestCase):
    def setUp(self):
        self.location = Location(name='Nakuru')
        self.location.save_location()
        self.category= Category(name = 'fashion')
        self.category.save_category()
        self.image=Images(name = 'dress',description = 'masterpiece handstiched for two years',location = 'nakuru',category = 'fashion')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.test_image,Images))
     
    def test_save_image(self):
        self.image.save_image()
        self.assertTrue(len(Images.objects.all()) == 1)
    def test_delete_image(self):
        self.test_image.delete_image()
        image = Images.objects.all()
        self.assertTrue(len(Images.objects.all()) ==1)
    def test_get_image_by_id(self):
        self.image.save_image()
        self.assertTrue(len(Images.get_image_by_id(self.image.id))>0)

    def test_filter_by_location(self):
        self.image.save_image()
        self.assertTrue(len(Images.filter_by_location(self.Nakuru)) == 1)

    def test_search_image_by_category(self):
        self.image.save_image()
        self.assertTrue(len(Images.search_image_by_category(self.fashion)) == 1)