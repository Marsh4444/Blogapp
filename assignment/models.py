from django.db import models

# Create your models here.
class About(models.Model):
    title = models.CharField(max_length=100)
    short_desc = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "About"
        verbose_name_plural = "About"

    def __str__(self):
        return self.title
    

class FollowUS(models.Model):
    platform_name = models.CharField(max_length=50)
    url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Follow US"
        verbose_name_plural = "Follow US"
    
    def __str__(self):
        return self.platform_name
