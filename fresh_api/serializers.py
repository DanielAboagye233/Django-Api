from rest_framework import serializers
from fresh.models import Post
from django.conf import settings

# class ImageSerializer(serializers.Serializer):
#     edited_image = serializers.ImageField()

#     def update(self, instance, validated_data):
#         edited_image = validated_data.get('edited_image')
#         # Perform image editing or modifications using libraries like Pillow or OpenCV
#         # Save the edited image to a desired location
#         instance.save()
#         return instance


# class ImageSerializer(serializers.Serializer):
#     image = serializers.ImageField()

#     def update(self, instance, validated_data):
#         image = validated_data.get('image')
#         instance.image = image
#         instance.save()
#         return instance


class PostSerializer(serializers.ModelSerializer):
    # image = serializers.ImageField(required=False)  # Add this line for the image field
    image = serializers.ImageField()
    def update(self, instance, validated_data):
        image = validated_data.get('image')
        # Perform image editing or modifications using libraries like Pillow or OpenCV
        # Save the edited image to a desired location
        instance.save()
        return instance
    class Meta:
        model = Post
        fields = ('category', 'id', 'title', 'image', 'slug', 'author', 
                  'excerpt', 'content', 'status')

# class PostSerializer(serializers.ModelSerializer):
#     # image = serializers.ImageField(required=False)  # Add this line for the image field
#     class Meta:
#         model = Post
#         fields = ('category', 'id', 'title', 'image', 'slug', 'author', 
#                   'excerpt', 'content', 'status')


class UserRegisterSerializer(serializers.ModelSerializer):

    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8, write_only=True)

    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('email', 'username', 'first_name')
        extra_kwargs = {'password': {'write_only': True}}