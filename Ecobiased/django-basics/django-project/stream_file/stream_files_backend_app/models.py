from django.db import models

# Create your models here.


class StoredFile(models.Model):
    """
    models to store the file name.
    """
    name = models.CharField(max_length=255, null=False)
    file_path = models.TextField(null=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
