from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.fields.CharField(max_length=250)

    def __str__(self):
        return self.name

class Partner(models.Model):
    full_name = models.fields.CharField(max_length=250)
    photo = models.ImageField(upload_to='partner/')

    def __str__(self):
        return self.full_name


class SocialNetwork(models.Model):
    SOCIAL_NETWORK_CHOICES = (
        ('YT', 'YOU TUBE'),
        ('TT', 'TIK TOK'),
        ('TG', 'TELEGRAM'),
        ('INST', 'INSTAGRAM')
    )
    name = models.CharField(choices=SOCIAL_NETWORK_CHOICES, max_length=250)
    sub_count = models.IntegerField(default=0)
    url = models.URLField()
    price = models.CharField(max_length=250)
    partner = models.ForeignKey('Partner', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='social_network')

    def __str__(self):
        return "{} | {}".format(self.name, self.partner.full_name)
