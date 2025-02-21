from rest_framework import serializers # type: ignore
from imdb_first.models import Movie

class MovieSerializer(serializers.Serializer):
     id = serializers.IntegerField(read_only=True)
     name = serializers.CharField()
     description = serializers.CharField()
     active = serializers.BooleanField()
     
     def create(self, validated_data):
         return Movie.objects.create(**validated_data)
     
     def update(self, instance, validated_data):
         instance.name = validated_data.get('name', instance.name)
         instance.description = validated_data.get('description', instance.description)
         instance.active = validated_data.get('active', instance.active)
         instance.save()
         return instance
     
    def validate(self,data):
        if data.get('description') == data.get('name'):
            raise serializers.ValidationError("both description and name should not be same")
        else:
            return data

     
     def validate_name(self,value):
         if len(value) < 3:
             raise serializers.ValidationError("Name must be at least 5 characters long.")
         return value

