from rest_framework import serializers

from events.models import Event

class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [ 'id', 'level','environment', 'address','log', 'date', 'archive']

