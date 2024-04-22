from djongo import models

class Cart(models.Model):
    user_id = models.IntegerField()
    product_id = models.CharField(max_length=100)
    product_quantity = models.IntegerField()

    def __str__(self):
        return '%s %s %s' % (self.user_id, self.product_id, self.product_quantity)
