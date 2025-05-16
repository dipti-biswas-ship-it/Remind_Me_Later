from django.urls import path
from .views import send_email_reminder

urlpatterns = [
    path('send-email/', send_email_reminder, name='send_email_reminder'),
]
