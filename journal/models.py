from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=250)
    image = models.FileField(upload_to="journal/image")
    text = models.TextField()
    issue = models.CharField(max_length=100)
    published = models.DateTimeField(auto_now_add=True)
    publication_fees = models.TextField()
    address = models.TextField()
    ISSN = models.CharField(max_length=15,blank=True,null=True)
    SJIF = models.FloatField(blank=True,null=True)
    factor = models.FloatField(blank=True,null=True)
    contact = models.URLField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=250)
    description = models.TextField()
    DOI = models.URLField()
    keywords = models.CharField(max_length=250)
    abstract = models.TextField()
    file = models.FileField(upload_to='journal/pdf')
    published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    text_cite = models.TextField()
    section = models.CharField(max_length=50,blank=True,null=True)
    start_page = models.PositiveSmallIntegerField()
    end_page = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.title
