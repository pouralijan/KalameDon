#!/usr/bin/env python3

from database import DataBaseEngines

DATABASES = {
        'default': {
            'ENGINE': DataBaseEngines.SQLite,
            'NAME': 'mydatabase',
            }
        }
