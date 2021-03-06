from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    city = models.CharField(max_length=300)
    address = models.FloatField()
    def str(self):
        return "Name: %s; description: %s" % (self.name, self.description)
    def to_json(self):
        return {
            'id': self.id,
            'name ': self.name,
            'description': self.description,
            'city': self.city,
            'address': self.address
        }
class Vacancy(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    salary = models.FloatField()
    company_id = models.ForeignKey(Company, on_delete=models.CASCADE, default=1)
    def str(self):
        return "Name: %s; description: %s" % (self.name, self.description)
    def to_json(self):
        return {
        'id': self.id,
        'name':self.name,
        'description ': self.description,
        'salary': self.salary,
        'company_id': self.company_id.id
        }


