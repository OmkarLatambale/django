from rest_framework import serializers

from .models import Student

class StudentSerializers(serializers.Serializer):
    name = serializers.CharField(max_length=15)
    age = serializers.IntegerField()
    email = serializers.EmailField()
    course = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name',instance.name)
        instance.age = validated_data.get('age',instance.email)
        instance.email = validated_data.get('email',instance.email)
        instance.course = validated_data.get('course',instance.course)
        instance.save()
        return instance

    def validate_age(self,value):
        if value <= 18:
            raise serializers.ValidationError("Age must be 18 or greater than 18.")
        return value
  