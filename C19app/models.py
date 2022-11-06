from email.policy import default
from enum import unique
import uuid
from django.db import models
from uuid import uuid4

# Create your models here.



class Comments(models.Model): 

    id = models.UUIDField(
        primary_key=True,
        verbose_name='User_ID', 
        default=uuid4, 
        editable=False
    )

    name = models.CharField(
        verbose_name="Visitor's Name", 
        help_text='Name of Demiz visitor', 
        max_length=200, 
        error_messages={
            'max_length': 'Name must not pass 200 characters', 
        }, 
        default='Anonymous'
    )

    comment = models.TextField(
        help_text='Enter comments here',
        default='You did a great job Demiz'
    )


    date = models.DateField(
        auto_now=True
    )

    def __str__(self) -> str:
        return str(self.name) + " " + str(self.date)