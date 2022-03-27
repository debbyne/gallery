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
