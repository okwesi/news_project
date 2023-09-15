from celery import shared_task

@shared_task
def task_one():
    print(" task one called and worker is running good")
    return "success"

@shared_task
def task_two(data, *args, **kwargs):
    print(f" task two called with the argument {data} and worker is running good")
    return "success"