from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Address(models.Model):
    street = models.CharField(max_length=100)
    post_code = models.IntegerField()
    city = models.CharField(max_length=50)
    
    def __str__(self):
      return f"{self.street}, {self.post_code}, {self.city}"

    # class Meta:
    #     verbose_name_plural = "Address Entries"
        
class Country(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField()   
    
    def __str__(self):
        return f"{self.name} ({self.code})"     

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.OneToOneField(Address,on_delete=models.CASCADE,null=True)
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
         
    def __str__(self):
        return self.full_name()

class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)
    rating = models.IntegerField(
        validators=[MinValueValidator(1),MaxValueValidator(10)])
    is_bestSelling = models.BooleanField(default=False)
    country_publised = models.ManyToManyField(Country,)
    
    def __str__(self):
        return f"{self.title} ({self.author}) -- ({self.rating})"

    def get_absolute_url(self):
        return reverse("book-detail",args=[self.id])
    
    def save(self, *args, **kwargs):
     super().save(*args, **kwargs)  # Call the original save method

        
