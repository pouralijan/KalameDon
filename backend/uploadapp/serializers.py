#!/usr/bin/env python3
"""
UploadApp serilizers ...
"""

from rest_framework import serializers
from .models import File

class FileSerializer(serializers.ModelSerializer):
    """
    UploadApp files serializer
    """
    # pylint: disable=R0903
    class Meta:
        """
        File serializer Meta class
        """
        model = File
        fields = '__all__'
