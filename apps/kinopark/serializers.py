from rest_framework import serializers
from apps.kinopark.models import Movie
from apps.kinopark.models import Movie_details


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'description',
            'producer',
            'rating',
            'published'
        )


class MovieDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie_details
        fields = '__all__'



