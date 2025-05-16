from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..serializers import *

@api_view(['POST'])
def send_email_reminder(request):
    serializer = EmailSendSerializer(data=request.data)
    if serializer.is_valid():
        # Send email
        to_email = serializer.validated_data['to_email']
        subject = serializer.validated_data['subject']
        message = serializer.validated_data['message']
        
        try:
            send_mail(
                subject,
                message,
                'your_email@gmail.com',  # From email (must match EMAIL_HOST_USER)
                [to_email],
                fail_silently=False,
            )
        except Exception as e:
            return Response({'error': 'Failed to send email', 'details': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        # Save log to DB
        serializer.save()

        return Response({'message': 'Email sent and log saved successfully', 'data': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
