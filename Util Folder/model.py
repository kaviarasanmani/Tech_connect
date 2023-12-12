from django.db import models

class Manufacturer(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

class Offer(models.Model):
    product_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    link = models.URLField()
    return_days = models.IntegerField()
    initial_price = models.CharField(max_length=100)
    delivery_price = models.CharField(max_length=100)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    merchant_name = models.CharField(max_length=100)
    merchant_domain = models.CharField(max_length=100)
    merchant_country_code = models.CharField(max_length=10)
    merchant_rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    merchant_reviews = models.IntegerField(null=True, blank=True)
    merchant_link = models.URLField()

class Feature(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class SpecificationAttribute(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=100)

class Specification(models.Model):
    category = models.CharField(max_length=100)
    attributes = models.ManyToManyField(SpecificationAttribute)

class Review(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField()
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    rating_out_of = models.IntegerField()

class ProductReview(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    reviews = models.IntegerField()
    review_text = models.TextField()
    date = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)

class EditorialReview(models.Model):
    title = models.CharField(max_length=200)
    review = models.TextField()
    link = models.URLField()
    rating = models.DecimalField(max_digits=3, decimal_places=1, null=True, blank=True)
    rating_out_of = models.IntegerField(null=True, blank=True)

class iPhone14(models.Model):
    kgmid = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    reviews = models.IntegerField()
    description = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    offers = models.ManyToManyField(Offer)
    features = models.ManyToManyField(Feature)
    specifications = models.ManyToManyField(Specification)
    web_reviews = models.ManyToManyField(Review, related_name='web_reviews')
    product_reviews = models.ManyToManyField(ProductReview)
    editorial_reviews = models.ManyToManyField(EditorialReview)
    images = models.JSONField()  # Storing images as JSON list of URLs
