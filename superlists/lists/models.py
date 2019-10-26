"""models module of lists application"""
from django.db import models


class Item(models.Model):
    """Item table representation"""

    text = models.TextField(default="")
