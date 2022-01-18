from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
import threading
import logging
import time

# Create your views here.
def endlessLogs():
    while True:
        logging.warning('Watch out! here comes a flood of logs')
        print("print log1")
        time.sleep(10)




class TodoView(viewsets.ModelViewSet):
    t = threading.Thread(target=endlessLogs)
    t.setDaemon(True)
    t.start()
    #above is just a thread to write logs
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()