#!/usr/bin/env python3

import settings
from kalamedon import KalameDon
from database import DataBase

print("Start ...")
d = KalameDon(settings.DATABASES)
print("End ...")
