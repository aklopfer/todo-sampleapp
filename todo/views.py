from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer
from .models import Todo
import threading
import logging
import time

# Create your views here.
# Austin perhaps have a huge log message either ssaved or constructed that's constant and only emit logs every 1 second so I know how many logs to expect exactly so I can see if were missing any
def endlessLogs():
    while True:
        logging.warning('Watch out! here comes a flood of logs')
        logging.info('ERROR hello hello')
        logging.error('wow wow ')
        print("print log1")
        time.sleep(15)




class TodoView(viewsets.ModelViewSet):
    t = threading.Thread(target=endlessLogs)
    t.setDaemon(True)
    t.start()
    #above is just a thread to write logs
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()