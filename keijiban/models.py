from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=255,
        blank=False,
        null=False,)

    def __str__(self):
        return self.name

class Thread(models.Model):
    title = models.CharField(
        max_length=255,
        blank=False,
        null=False,
        default="無題")

    view = models.IntegerField(
        blank=True,
        null=False,
        default=0)

    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL)

    def __str__(self):
        return self.title


class Tag(models.Model):
    type = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        unique=True)

    def __str__(self):
        return self.type


class Post(models.Model):
    IPaddress = models.GenericIPAddressField(
        blank=False,
        null=False)

    ipID = models.CharField(
        max_length=8,
        blank=True,
        null=False,
        default="xxxxxxxx")

    created = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        blank=False,
        null=False)

    name = models.CharField(
        max_length=15,
        blank=False,
        null=False,
        default="名無しさん")

    body = models.TextField(
        max_length=255,
        blank=False,
        null=False)

    thread = models.ForeignKey(
        Thread,
        on_delete=models.CASCADE)

    tags = models.ManyToManyField(
        Tag,
        blank=True)

    def __str__(self):
        return str(self.id)