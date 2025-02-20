import json
from celery import shared_task
from time import sleep
from django_celery_beat.models import PeriodicTask, IntervalSchedule

@shared_task(name="addition_task")
def add(x, y):
    sleep(10)
    return x+y


@shared_task
def sub(x, y):
    sleep(20)
    return x-y

@shared_task
def clear_session_cache(id):
    print(f"Session cache cleared", {id})
    return id

@shared_task
def clear_session_data(id):
    print(f"Session cache cleared", {id})
    return id

@shared_task
def clear_log_data(id):
    print(f"Log data cleared", {id})
    return id


# Create Schedule every 30 seconds
schedule, created = IntervalSchedule.objects.get_or_create(
    every=30,
    period=IntervalSchedule.SECONDS,
)

# Schedule the periodic task programmatically
PeriodicTask.objects.get_or_create(
    name='Clear Log Periodic Task',
    task='myapp.tasks.clear_log_data',
    interval=schedule,
    args=json.dumps(['999']),  # Pass the arguments to the task as a JSON-encoded list
)