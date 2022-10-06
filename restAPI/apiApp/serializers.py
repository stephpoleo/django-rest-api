from dataclasses import fields
from rest_framework import serializers
from .models import Family

class FamilySerializer(serializers.ModelSerializer):

    class Meta:
        model = Family
        fields = ['id', 'name', 'age', 'birthday']

class FamilySerializerAll(serializers.ModelSerializer):

    birthday = serializers.SerializerMethodField('_get_birthday')

    def _get_birthday(self, obj):
        birthday = str(obj.birthday).split(' ')
        birthday = birthday[0].split('-')
        birthday = birthday[2] + '-' + birthday[1] + '-' + birthday[0]
        obj.birthday = birthday
        return obj.birthday

    class Meta:
        model = Family
        fields = ['id', 'name', 'age', 'birthday']