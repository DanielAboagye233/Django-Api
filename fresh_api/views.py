from django.shortcuts import get_object_or_404
from fresh.models import Post
from .serializers import PostSerializer
from rest_framework import generics, permissions, status, viewsets, filters
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.permissions import SAFE_METHODS, BasePermission, DjangoModelPermissions, IsAuthenticatedOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser
# from django.shortcuts import get_object_or_404
# Display Posts

class PostList(generics.ListAPIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # serializer_class = PostSerializer
    # queryset = Post.objects.all()

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **Kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    
    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()


class PostDetail(generics.RetrieveAPIView):

    serializer_class = PostSerializer

    def get_object(self, queryset=None, **Kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, slug=item)
    

# Post Search


class PostListDetailfilter(generics.ListAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    # '^' Starts-with search.
    # '=' Exact matches.
    search_fields = ['^slug']
    

class CreatePost(APIView):
    serializer_class = PostSerializer
    parser_classes = [MultiPartParser, FormParser]
    def get(self, request):
        queryset = Post.objects.all().values()
        return Response(queryset)
        
    # permission_classes = [permissions.IsAuthenticated]
    # queryset = Post.objects.all()
    # serializer_class = PostSerializer
    # parser_classes = [MultiPartParser, FormParser]

    def post(self, request, format=None):
        print(request.data)
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminPostDetail(generics.RetrieveAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

# class ImageEditView(APIView):
#     def post(self, request):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'Image editing successful'})
#         return Response(serializer.errors, status=400)

class EditPost(generics.UpdateAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Image editing successful'})
        return Response(serializer.errors, status=400)
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DeletePost(generics.RetrieveDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# class ImageEditView(APIView):
#     def put(self, request, *args, **kwargs):
#         serializer = ImageSerializer(data=request.data)
#         if serializer.is_valid():
#             image = serializer.validated_data['image']
#             img = Image.open(image)
#             # Perform your desired edits on the image here
#             edited_image = img.resize((500, 500))  # Example: resizing to 500x500 pixels
#             edited_image.save('path/to/save/edited_image.jpg')
#             return Response({'message': 'Image edited successfully'})
#         return Response(serializer.errors, status=400)


# class PostUserWritePermission(BasePermission):
#     message = 'Editting posts is restricted to the author only'

#     def has_object_permission(self, request, view, obj):

#         if request.method in SAFE_METHODS:
#             return True
#         return obj.author == request.user

# class PostList(viewsets.ModelViewSet):
#     permission_classes = [PostUserWritePermission]
#     serializer_class = PostSerializer

#     def get_object(self, queryset=None, **Kwargs):
#         item = self.kwargs.get('pk')
#         return get_object_or_404(Post, slug=item)
    
#     # Define Custom Queryset
#     def get_queryset(self):
#         return Post.objects.all()
    
    


# class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
#     permission_classes = [PostUserWritePermission]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# POST admin

# class CreatePost(generics.CreateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer




        
    

# # Post Search


# class PostListDetailfilter(generics.ListAPIView):

#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     filter_backends = [filters.SearchFilter]
#     # '^' Starts-with search.
#     # '=' Exact matches.
#     search_fields = ['^slug']

# # Post Admin

# # class CreatePost(generics.CreateAPIView):
# #     permission_classes = [permissions.IsAuthenticated]
# #     queryset = Post.objects.all()
# #     serializer_class = PostSerializer


# class CreatePost(APIView):
#     permission_classes = [permissions.IsAuthenticated]
#     parser_classes = [MultiPartParser, FormParser]

#     def post(self, request, format=None):
#         print(request.data)
#         serializer = PostSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class AdminPostDetail(generics.RetrieveAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class EditPost(generics.UpdateAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()


# class DeletePost(generics.RetrieveDestroyAPIView):
#     permission_classes = [permissions.IsAuthenticated]
#     serializer_class = PostSerializer
#     queryset = Post.objects.all()
