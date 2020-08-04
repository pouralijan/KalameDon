#!/usr/bin/env python3
"""
UploadApp urls ...
"""

from django.urls import path
from .views import FileUploadView

urlpatterns = [
        path('', FileUploadView.as_view()),
        ]
