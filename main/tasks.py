from celery import shared_task
import time, random
from .models import TaskLog

@shared_task
def practice_background_task():
    time.sleep(5)
    print("the celery task is executed")

@shared_task(bind=True, max_retries=3, default_retry_delay=5)
def practice_retry_task(self):
    try:
        print("the task has started")
        time.sleep(2)
        if random.choice([True, False]):
            raise ValueError("the random failure has happened")
        print("the task is completed successfully")
        
    except Exception as exc:
        print(f"the task has failed: {exc}")
        raise self.retry(exc=exc)

@shared_task(bind=True, max_retries=3)
def practice_retry_log_task(self):
    name = "practice_retry_log_task"
    try:
        print("the task has started")
        time.sleep(3)

        if random.choice([True, False]):
            raise ValueError("random failure has happened")

        print("the task is completed")

        # logging the success in the db
        TaskLog.objects.create(name=name, status="success", message="has completed without the errors")

    except Exception as exc:
        print(f"Task failed: {exc}")

        # logging the failure in db
        TaskLog.objects.create(name=name, status="failed", message=str(exc))

        # retrying safely after countdown of 5 seconds
        raise self.retry(exc=exc, countdown=5)