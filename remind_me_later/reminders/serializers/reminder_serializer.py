from rest_framework import serializers
from ..models import *

class EmailSendSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmailSend
        fields = ['id', 'to_email', 'subject', 'message', 'sent_at']
        read_only_fields = ['id', 'sent_at']
