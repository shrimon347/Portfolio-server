# Generated by Django 5.1 on 2024-08-23 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_blog_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='color',
            field=models.CharField(choices=[('#025A4E', 'green'), ('#EDE7DE', 'cream')], max_length=50),
        ),
    ]
