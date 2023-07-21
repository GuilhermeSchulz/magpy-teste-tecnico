from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import PackageRelease, Project
import requests


class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ['name', 'version']
        extra_kwargs = {'version': {'required': False}}


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'packages']

    packages = PackageSerializer(many=True)

    def create(self, validated_data):
        project = Project(name=validated_data['name'])
        project.save()
        packages = validated_data['packages']
        for package in packages:
            r = requests.get(f'https://pypi.org/pypi/{package["name"]}/json')
            if r.status_code == 200:
                if 'version' not in package:
                    package['version'] = r.json()['info']['version']
            else:
                project.delete()
                raise ValidationError(
                    {"error": "One or more packages doesn't exist"})
            package['project'] = project
            package = PackageRelease(**package)
            print(package)
            package.save()
        return project
