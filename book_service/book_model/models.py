from djongo import models

class BookCategory(models.Model):
    category_name = models.CharField(max_length=255)
    
    def __str__(self):
        return '%s' % ( self.category_name )

class Book(models.Model):
    pid = models.CharField(max_length=100)
    category = models.IntegerField()  
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=255)  
    image_url = models.CharField(max_length = 255)
    description = models.TextField()
    quantity = models.IntegerField()
    price = models.IntegerField()
    meta_keyword = models.CharField(max_length = 255)
    
    def __str__(self):
        return '%s %s %s %s %s %s %s %s %s' % (self.pid,self.category,
        self .name, self.brand, self.image_url, self.description, self.quantity, self.price, self.meta_keyword)
    
