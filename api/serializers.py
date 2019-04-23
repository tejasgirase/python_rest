from rest_framework import serializers
from .models import Bucketlist

class BucketlistSerializers(serializers.ModelSerializer):
    """Serializer map to modal instance into JSON format"""

    class Meta:
        """Meta Class to map serializer fields with th modal fields"""
        model = Bucketlist
        fields = ('id', 'name', 'date_created', 'date_modified','owner')
        read_only_fields = ('date_created', 'date_modified')