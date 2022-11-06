# Generated by Django 4.1.2 on 2022-10-27 21:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='User_ID')),
                ('name', models.CharField(default='Anonymous', error_messages={'max_length': 'Name must not pass 200 characters', 'unique': 'This name is already taken'}, help_text='Name of Demiz visitor', max_length=200, unique=True, verbose_name="Visitor's Name")),
                ('comment', models.TextField(help_text='Enter comments here')),
            ],
        ),
    ]
