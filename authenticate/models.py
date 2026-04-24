from django.db import models
from django.urls import reverse

# Create your models here.
class Society(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField(null=True, blank=True)
  contact_email_address = models.EmailField(max_length=255, blank=True, null=True)
  location = models.CharField(max_length=100, help_text='Enter general area your society resides')
  image_url = models.CharField(max_length=500, null=True, blank=True)
  image = models.ImageField(upload_to="uploads/society/",null=True, blank=True)
  date_created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.name}"

  def get_absolute_url(self):
        # return reverse("society_update", kwargs={"pk": self.pk})
        return reverse(f"society_update/{self.pk}/")

