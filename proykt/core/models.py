from django.db import models

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
 
class Setting(models.Model):
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    gmail = models.EmailField(blank=True, null=True)
    logo = models.ImageField(upload_to='logos/', blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    whatsapp = models.URLField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    title2 = models.CharField(max_length=255, blank=True, null=True)
    konum = models.CharField(max_length=250, blank=True,null=True)
   

    def __str__(self):
        return self.title if self.title else 'Setting {}'.format(self.pk)



class Edu(BaseModel):
    image = models.ImageField(upload_to="edu",null=True, blank=True)
    price = models.IntegerField()
    name = models.CharField(max_length=255)
    date = models.IntegerField()
    say = models.IntegerField()
    certifcate = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    
    
    

    class Meta:
        verbose_name = "Edu"
        verbose_name_plural = "Edus"

    def __str__(self):
        return self.title
  
