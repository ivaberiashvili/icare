from celery import shared_task

@shared_task
def send_welcome_email(user_id):
    print(f"📨 Sent welcome email to user {user_id}")