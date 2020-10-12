from django.test import TestCase
from .models import Location,Image,Category

# Create your tests here.
class ImageTest(TestCase):
    # setup method
    def setUp(self):
        self.new_location=Location(name='place')
        self.new_category=Category(name='home')
        self.new_image=Image(name='pic',description='memories',author='becky',category=self.new_category,location=self.new_location)

        # testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_image,Image))
        
        #Testing save method
    def test_save_method(self):
        self.new_location.save_location()
        self.new_category.save_category()
        self.new_image.save_image()
        after=Image.objects.all()
        self.assertTrue(len(after) > 0)
        
        # delete image

    def test_delete_image(self):
        self.new_image.delete_image()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

        # get image test

    def test_get_image_by_id(self):       
        id = 1       
        image = Image.get_image_by_id(id)       
        self.assertTrue(len(image)==0)

            # test for id
    def test_get_image_by_id(self):
        found_image = self.new_image.get_image_by_id(self.new_image.id)
        image = Image.objects.filter(id=self.new_image.id)
        self.assertEquals(found_image, image)

            # update image test
    def test_update_image(self):
        self.new_image.save_image()
        self.new_image.update_image(self.image_test.id, 'photos/test.jpg')
        changed_img = Image.objects.filter(image='photos/test.jpg')
        self.assertTrue(len(changed_img) > 0)

        # search image by location test
    def test_search_image_by_location(self):
        self.image_test.save_image()
        found_images = self.new_image.filter_by_location(location='place')
        self.assertTrue(len(found_images) == 1)

        # search image by category
    def test_search_image_by_category(self):
        category = 'home'
        found_img = self.new_image.search_by_category(category)
        self.assertTrue(len(found_img) > 1)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

        # testcase Location

        class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(name='place')
        self.location.save_location()

            # test instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

                # test savelocation
    def test_save_location(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 0)

    def test_get_locations(self):
        self.location.save_location()
        locations = Location.get_locations()
        self.assertTrue(len(locations) > 1)

    # def test_update_location(self):
    #     new_location = 'kericho'
    #     self.location.update_location(self.location.id, new_location)
    #     changed_location = Location.objects.filter(name='kericho')
    #     self.assertTrue(len(changed_location) > 0)

    def test_delete_location(self):
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)

            # testcase Category

class CategoryTestClass(TestCase):

    def setUp(self):
        self.category = Category(name='home')
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_category(self):
        self.category.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_category(self):
        self.category.delete_category()
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)




            