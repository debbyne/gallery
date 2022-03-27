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
