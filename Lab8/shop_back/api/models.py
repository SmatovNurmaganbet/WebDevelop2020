from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=300)
    def __str__(self):
        return self.name
    def to_json(self):
        return {
            'id': self.id,
            'name ': self.name
        }
class Product(models.Model):
    name = models.CharField(max_length=300)
    price = models.FloatField()
    description = models.TextField()
    count = models.IntegerField()
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    def __str__(self):
        return self.name
    def to_json(self):
        return {
        'id': self.id,
        'name':self.name,
        'price ': self.price,
        'description ': self.description,
        'count ': self.count,
        'category_id': self.category_id.id
        }

#from api.models import Product, Category
#c = Category(name = 'Laptops')
#p = Product(name='Lenovo Thinkpad', price=1000, description='no', count=5, category_id=c[0])

