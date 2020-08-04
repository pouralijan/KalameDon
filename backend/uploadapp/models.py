#!/usr/bin/env python3
"""
UploadApp models ...
"""
from django.db import models

# Create your models here.

class File(models.Model):
    """
    File class for upload file.
    """
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        """
        Return name of uploaded file.
        """

        return self.file.name
