#
from django.shortcuts import render
from django.http import HttpResponse

from . import *
# fun:Function

def function_open_index_page(request):
    """
    Shows the homepage with a welcome message that is translated in the
    user's language.
    """
    send_data = 'Welcome'
    # Put the data to be displayed on the page in context
    context={
                'send_data':send_data , 
            }
    return render(request,'index.html' , context)

