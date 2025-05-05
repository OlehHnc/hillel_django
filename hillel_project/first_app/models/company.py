from django.db import models
from django.core.exceptions import ValidationError

class Company(models.Model):


    name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=200, null=False)
    email = models.EmailField(null=True)
    tax_code = models.CharField(max_length=8, null=False)



    def save(self, *args, **kwargs):
        # Забезпечення того, що існує лише один інстанс
        if not self.pk and Company.objects.exists():
            raise ValidationError('There can be only one Company instance.')
        return super(Company, self).save(*args, **kwargs)


    def __str__(self):
        return f" Company {self.name}, податковий код {self.tax_code}, має адресу {self.email}"