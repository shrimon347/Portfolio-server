from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog,Project
from .serializers import AllBlogSerializers,ContactSerializer,AllProjectSerializers
from rest_framework import status

# Create your views here.
@api_view(['GET'])
def getbloglist(request):
    blogs = Blog.objects.all()
    serializer = AllBlogSerializers(blogs, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getprojects(request):
    projects = Project.objects.all()
    serializer = AllProjectSerializers(projects, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getblogpost(request,pk):
    blog = Blog.objects.get(pk=pk)
    serializer = AllBlogSerializers(blog, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def contact_view(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)