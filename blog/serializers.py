from rest_framework import serializers
from .models import Blog, Contact,Project


class AllBlogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class AllProjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['website_name','image_url','stack_use','preview_url','github_url','color']

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'project']