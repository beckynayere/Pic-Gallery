from django.db import models
import sys  
sys.setrecursionlimit(10000)

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def update_category(self):
        self.update()


    def delete_category(self):
        self.delete()



class Location(models.Model):
    name = models.CharField(max_length=60)

    @classmethod
    def get_locations(cls):
        locations = Location.objects.all()
        return locations

    def __str__(self):
        return self.name

    @classmethod
    def update_location(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def update_location(self):
        self.update()





class Image(models.Model):

    image = models.ImageField(upload_to='images/')
    name =models.CharField(max_length=60)
    description =models.TextField()
    author =models.CharField(max_length=40, default='admin')
    date =models.DateTimeField(auto_now_add=True)
    category =models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )
    location =models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        )

    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location

    @classmethod
    def update_image(cls, id, value):
        cls.objects.filter(id=id).update(image=value)

    @classmethod
    def get_image_by_id(cls, id):
        image = cls.objects.filter(id=id)
        return image

    @classmethod
    def search_by_category(cls, category):
        images = cls.objects.filter(category__name__icontains=category)
        return images

    @classmethod
    def update_image(cls, id, updates):
        cls.objects.filter(id=id).update(updates)


    def __str__(self):
        return self.name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    class Meta:
        ordering = ['date']