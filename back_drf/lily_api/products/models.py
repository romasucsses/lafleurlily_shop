from django.db import models


class BaseReviewsModel(models.Model):
    name = models.CharField(max_length=55)
    stars_count = models.IntegerField(null=True)
    review = models.TextField()
    date = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class ReviewsBastina(BaseReviewsModel):
    product = models.ForeignKey('products.ProductBastina', on_delete=models.PROTECT, default=None)


class ReviewsLily(BaseReviewsModel):
    product = models.ForeignKey('products.ProductLily', on_delete=models.PROTECT, default=None)


class ReviewsDA(BaseReviewsModel):
    product = models.ForeignKey('products.ProductDA', on_delete=models.PROTECT, default=None)


class ProductCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class BaseProductModel(models.Model):
    name = models.CharField(max_length=355)
    image = models.ImageField(upload_to="img/%y/%m/%d/")
    price = models.FloatField()
    description = models.TextField(blank=True)
    date_added = models.DateField(auto_now=True)
    quantity = models.IntegerField()
    slug_url = models.SlugField(max_length=255, db_index=True, unique=True, verbose_name='URL')

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class ProductBastina(BaseProductModel):
    pass

class ProductDA(BaseProductModel):
    pass

class ProductLily(BaseProductModel):
    category = models.ForeignKey('products.ProductCategory', on_delete=models.PROTECT)


class BaseLinksStoresModel(models.Model):
    name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255)
    link_google_maps = models.TextField()

    def __str__(self):
        return self.pk

    class Meta:
        abstract = True


class StoresBastina(BaseLinksStoresModel):
    pass


class StoresDA(BaseLinksStoresModel):
    pass


class StoresLily(BaseLinksStoresModel):
    pass
