# # # from django.db import models

# # # class Category(models.Model):
# # #     name = models.CharField(max_length=255)
# # #     slug = models.SlugField(unique=True)  # SEO-friendly URL slug

# # #     def __str__(self):
# # #         return self.name


# # # class Subcategory(models.Model):
# # #     name = models.CharField(max_length=255)
# # #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# # #     slug = models.SlugField(unique=True)  # SEO-friendly URL slug

# # #     def __str__(self):
# # #         return f"{self.category} - {self.name}"


# # # class Brand(models.Model):
# # #     name = models.CharField(max_length=255)
# # #     slug = models.SlugField(unique=True)  # SEO-friendly URL slug

# # #     def __str__(self):
# # #         return self.name


# # # class Product(models.Model):
# # #     name = models.CharField(max_length=255)
# # #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# # #     subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
# # #     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
# # #     model = models.CharField(max_length=255)
# # #     color = models.CharField(max_length=50)
# # #     storage_internal = models.IntegerField(default=0)  # in GB
# # #     storage_external = models.BooleanField(default=True)
# # #     display_size = models.DecimalField(max_digits=4, decimal_places=2)  # in inches
# # #     display_type = models.CharField(max_length=255)
# # #     display_resolution = models.CharField(max_length=255)
# # #     camera_main_resolution = models.CharField(max_length=255)
# # #     camera_main_video = models.BooleanField(default=True)
# # #     camera_front_resolution = models.CharField(max_length=255)
# # #     camera_front_video = models.BooleanField(default=True)
# # #     processor_type = models.CharField(max_length=255)
# # #     processor_speed = models.DecimalField(max_digits=4, decimal_places=2)  # in GHz
# # #     memory_ram = models.IntegerField(default=0)  # in GB
# # #     memory_expandable = models.BooleanField(default=True)
# # #     battery_capacity = models.IntegerField(default=0)  # in mAh
# # #     battery_removable = models.BooleanField(default=True)
# # #     operating_system = models.CharField(max_length=255)
# # #     connectivity_network = models.CharField(max_length=255)
# # #     connectivity_wifi = models.BooleanField(default=True)
# # #     connectivity_bluetooth = models.BooleanField(default=True)
# # #     connectivity_usb = models.BooleanField(default=True)
# # #     features = models.JSONField(default=list)
# # #     price = models.DecimalField(max_digits=10, decimal_places=2)  # in your local currency
# # #     availability = models.BooleanField(default=True)

# # #     # SEO fields
# # #     meta_title = models.CharField(max_length=255, blank=True, null=True)
# # #     meta_description = models.TextField(blank=True, null=True)
# # #     meta_keywords = models.CharField(max_length=255, blank=True, null=True)

# # #     def __str__(self):
# # #         return f"{self.brand} {self.model} - {self.color}"


# # # class Variant(models.Model):
# # #     mobile_phone = models.ForeignKey(Product, on_delete=models.CASCADE)
# # #     variant_color = models.CharField(max_length=50)

# # #     def __str__(self):
# # #         return f"{self.mobile_phone} - {self.variant_color}"



# # from django.db import models

# # class Category(models.Model):
# #     name = models.CharField(max_length=255)
# #     slug = models.SlugField(unique=True)  # SEO-friendly URL slug

# #     def __str__(self):
# #         return self.name


# # class Brand(models.Model):
# #     name = models.CharField(max_length=255)
# #     slug = models.SlugField(unique=True)  # SEO-friendly URL slug
# #     description = models.TextField(blank=True, null=True)
# #     website = models.URLField(blank=True, null=True)

# #     def __str__(self):
# #         return self.name


# # class Specification(models.Model):
# #     name = models.CharField(max_length=255)
# #     unit = models.CharField(max_length=50, blank=True, null=True)

# #     def __str__(self):
# #         return self.name


# # class Product(models.Model):
# #     name = models.CharField(max_length=255)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
# #     model = models.CharField(max_length=255)
# #     description = models.TextField(blank=True, null=True)
# #     price = models.DecimalField(max_digits=10, decimal_places=2)  # in your local currency
# #     availability = models.BooleanField(default=True)

# #     # SEO fields
# #     meta_title = models.CharField(max_length=255, blank=True, null=True)
# #     meta_description = models.TextField(blank=True, null=True)
# #     meta_keywords = models.CharField(max_length=255, blank=True, null=True)

# #     def __str__(self):
# #         return f"{self.brand} {self.model}"


# # class ProductSpecification(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
# #     value = models.CharField(max_length=255)

# #     def __str__(self):
# #         return f"{self.product} - {self.specification}: {self.value}"


# # class ProductImage(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     image = models.ImageField(upload_to='product_images/')

# #     def __str__(self):
# #         return f"{self.product} - Image"
# # class ProductReview(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     rating = models.PositiveIntegerField()
# #     review_text = models.TextField()
# #     reviewer_name = models.CharField(max_length=255)

# #     def __str__(self):
# #         return f"{self.product} - {self.reviewer_name}"
# # class ProductVariant(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     price_modifier = models.DecimalField(max_digits=10, decimal_places=2, default=0)
# #     def __str__(self):
# #         return f"{self.product} - {self.name if self.name else 'Variant'}"


# # models.py

# # from django.db import models
# # from django.utils.text import slugify
# # from django.contrib.auth.models import User
# # from django.urls import reverse


# # class Category(models.Model):
# #     name = models.CharField(max_length=255)
# #     slug = models.SlugField(unique=True, blank=True, null=True)
# #     def save(self, *args, **kwargs):
# #         if not self.slug:
# #             self.slug = slugify(self.name)
# #         super(Category, self).save(*args, **kwargs)
# #     def __str__(self):
# #         return self.name

# # class Brand(models.Model):
# #     name = models.CharField(max_length=255)
# #     slug = models.SlugField(unique=True, blank=True, null=True)
# #     description = models.TextField(blank=True, null=True)
# #     website = models.URLField(blank=True, null=True)

# #     def save(self, *args, **kwargs):
# #         if not self.slug:
# #             self.slug = slugify(self.name)
# #         super(Brand, self).save(*args, **kwargs)

# #     def __str__(self):
# #         return self.name


# # class Specification(models.Model):
# #     name = models.CharField(max_length=255)
# #     unit = models.CharField(max_length=50, blank=True, null=True)

# #     def __str__(self):
# #         return self.name


# # class Product(models.Model):

# #     AVAILABILITY_CHOICES = [
# #         ('in_stock', 'In Stock'),
# #         ('out_of_stock', 'Out of Stock'),
# #     ]

    
# #     name = models.CharField(max_length=255)
# #     category = models.ForeignKey(Category, on_delete=models.CASCADE)
# #     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
# #     model = models.CharField(max_length=255)
# #     description = models.TextField(blank=True, null=True)
# #     price = models.DecimalField(max_digits=10, decimal_places=2)
# #     # availability = models.BooleanField(default=True)
# #     availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default='in_stock')
# #     created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="created_by")
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     updated_at = models.DateTimeField(auto_now=True)
# #     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null= True, related_name="updated_by")

# #     def __str__(self):
# #         return f"{self.brand} {self.model}  - {self.get_availability_display()}"


# # class ProductSpecification(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
# #     value = models.CharField(max_length=255)

# #     def __str__(self):
# #         return f"{self.product} - {self.specification}: {self.value}"


# # class ProductImage(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     image = models.ImageField(upload_to='product_images/')

# #     def __str__(self):
# #         return f"{self.product} - Image"


# # class ProductReview(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     rating = models.PositiveIntegerField()
# #     review_text = models.TextField()
# #     reviewer_name = models.CharField(max_length=255)

# #     def __str__(self):
# #         return f"{self.product} - {self.reviewer_name}"


# # class ProductVariant(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     name = models.CharField(max_length=255, blank=True, null=True)
# #     size = models.IntegerField(null=True, blank=True)
# #     price_modifier = models.DecimalField(max_digits=10, decimal_places=2, default=0)

# #     def __str__(self):
# #         return f"{self.product} - {self.name if self.name else 'Variant'}"




# # class RecentStory(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     title = models.CharField(max_length=255)
# #     content = models.TextField()
# #     author = models.ForeignKey(User, on_delete=models.CASCADE)
# #     pub_date = models.DateTimeField(auto_now_add=True)
# #     slug = models.SlugField(unique=True, blank=True, null=True)

# #     def save(self, *args, **kwargs):
# #         if not self.slug:
# #             self.slug = slugify(self.title)
# #         super(RecentStory, self).save(*args, **kwargs)

# #     def get_absolute_url(self):
# #         return reverse('recent-story-detail', kwargs={'slug': self.slug})

# #     def __str__(self):
# #         return self.title
    


# # class Videos(models.Model):
# #     product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     url = models.URLField(blank=True, null=True)

# #     def __str__(self):
# #         return self.title
    
    

# # class Competitor(models.Model):
# #     Product = models.ForeignKey(Product, on_delete=models.CASCADE)
# #     name = models.CharField(max_length=255, null=True,blank=True)
# #     url =  models.URLField(blank=True,null=True)
# #     price = models.ImageField(blank=True,null=True)
    


# from django.db import models
# from django.utils.text import slugify
# from django.contrib.auth.models import User
# from django.urls import reverse


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Category, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name


# class Brand(models.Model):
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True, blank=True, null=True)
#     description = models.TextField(blank=True, null=True)
#     website = models.URLField(blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.name)
#         super(Brand, self).save(*args, **kwargs)

#     def __str__(self):
#         return self.name


# class Specification(models.Model):
#     name = models.CharField(max_length=255)
#     unit = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.name


# class Product(models.Model):

#     name = models.CharField(max_length=255)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
#     model = models.CharField(max_length=255)
#     description = models.TextField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default='in_stock')
#     created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_by")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="updated_by")

#     def __str__(self):
#         return f"{self.brand} {self.model}  - {self.get_availability_display()}"


# class ProductSpecification(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
#     value = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.product} - {self.specification}: {self.value}"


# class ProductImage(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='product_images/')

#     def __str__(self):
#         return f"{self.product} - Image"


# class ProductReview(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     rating = models.PositiveIntegerField()
#     review_text = models.TextField()
#     reviewer_name = models.CharField(max_length=255)

#     def __str__(self):
#         return f"{self.product} - {self.reviewer_name}"


# class ProductVariant(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, blank=True, null=True)
#     size = models.IntegerField(null=True, blank=True)
#     price_modifier = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     item_code = models.CharField(max_length=50, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.item_code:
#             # Generate a simple item code based on the product and variant IDs
#             self.item_code = f"{self.product.id}-{self.id}"
#         super(ProductVariant, self).save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.product} - {self.name if self.name else 'Variant'}"


# class RecentStory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     title = models.CharField(max_length=255)
#     content = models.TextField()
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now_add=True)
#     slug = models.SlugField(unique=True, blank=True, null=True)

#     def save(self, *args, **kwargs):
#         if not self.slug:
#             self.slug = slugify(self.title)
#         super(RecentStory, self).save(*args, **kwargs)

#     def get_absolute_url(self):
#         return reverse('recent-story-detail', kwargs={'slug': self.slug})

#     def __str__(self):
#         return self.title


# class Videos(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     url = models.URLField(blank=True, null=True)
#     def __str__(self):
#         return self.product


# class Competitor(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255, null=True, blank=True)
#     url = models.URLField(blank=True, null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)


#     def __str__(self):
#         return self.name



from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Specification(models.Model):
    name = models.CharField(max_length=255)
    unit = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name

AVAILABILITY_CHOICES = [
        ('in_stock', 'In Stock'),
        ('out_of_stock', 'Out of Stock'),
    ]

class Product(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.CharField(max_length=15, choices=AVAILABILITY_CHOICES, default='in_stock')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name="created_by")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="updated_by")

    def __str__(self):
        return f"{self.brand} {self.model} - {self.get_availability_display()}"

class ProductSpecification(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    specification = models.ForeignKey(Specification, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product} - {self.specification}: {self.value}"

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='product_images/')

    def __str__(self):
        return f"{self.product} - Image"

class ProductReview(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField()
    review_text = models.TextField()
    reviewer_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.product} - {self.reviewer_name}"

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, blank=True, null=True)
    size = models.IntegerField(null=True, blank=True)
    price_modifier = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    item_code = models.IntegerField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.item_code:
            # Generate an item code based on the product and variant IDs
            self.item_code = int(f"{self.product.id}{self.id}")
        super(ProductVariant, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.product} - {self.name if self.name else 'Variant'}"

class RecentStory(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(RecentStory, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('recent-story-detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.title

class Videos(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    url = models.URLField(blank=True, null=True)

class Competitor(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    url = models.URLField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
