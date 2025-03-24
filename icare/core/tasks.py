from celery import shared_task
import random


@shared_task
def send_welcome_email(user_id):
    print(f"📨 Sent welcome email to user {user_id}")

@shared_task
def daily_summary():
    print("📊 Daily summary task ran.")

@shared_task(bind=True, max_retries=3)
def risky_task(self):
    print("⚠️ Running risky task...")
    if random.random() < 0.5:
        raise self.retry(exc=Exception("Random failure!"), countdown=5)
    print("✅ Risky task succeeded!")