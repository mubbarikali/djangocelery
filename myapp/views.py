# myapp/views.py
from django.shortcuts import render
# from djangocelery.celery import add
from .tasks import add, sub
from celery.result import AsyncResult
from django.http import JsonResponse




def home(request):
    result = add.delay(10, 5)
    return render(request, 'home.html', {'result': result})

def check_result(request, task_id):
    result = AsyncResult(task_id)
    print("Ready: ", result.ready())
    print("Successful: ", result.successful())
    print("Failed: ", result.failed())
    # print("Get: ", result.get()) # This blocks execution
    
    return render(request, 'result.html', {'result': result})

def about(request):
    print("Home Results: ")
    add_result = add.apply_async(args=[100, 50])
    print("Add_Result: ", add_result)
    
    sub_result = sub.apply_async(args=[100, 50])
    print("Sub_Result: ", sub_result)
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

