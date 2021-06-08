from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=50)
    status = models.IntegerField()
    description = models.CharField(max_length=250)

    def __str__(self):
        return self.title



class Post(models.Model):
    title = models.CharField(max_length=200, default='title')
    content = models.TextField()
    mini_content = models.CharField(max_length=250)
    image = models.ImageField(upload_to='upload')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    pub_date = models.DateField()
    status = models.IntegerField()
    comment_count = models.IntegerField()
    views = models.IntegerField()
    tags = models.CharField(max_length=30)
    rating = models.IntegerField(default=0)
    is_gallery = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class CommentItem(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=500)
    author = models.CharField(max_length=50)
    rating = models.IntegerField()
    status = models.IntegerField()

    def __str__(self):
        return self.author


class About(models.Model):
    owner = models.CharField(max_length=50)
    text = models.TextField(default="")
    achivment = models.CharField(max_length=250)
    link = models.CharField(max_length=70, blank=True)
    image = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.owner


class Contact(models.Model):
    adres = models.CharField(max_length=50)
    city  = models.CharField(max_length=50)
    phone = models.IntegerField()
    contact1 = models.CharField(max_length=50, blank=True)
    contact2 = models.CharField(max_length=50, blank=True)


    def __str__(self):
        return self.adres


class GetInTouch(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    email = models.EmailField()
    title = models.CharField(max_length=250)
    message = models.TextField(default='')

    def __str__(self):
        return self.title