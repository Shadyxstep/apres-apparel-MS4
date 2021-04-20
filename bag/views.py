from django.shortcuts import render

# Create your views here.

def view_bag(request):
    """ A view that renders shopping cart content """

    return render(request, 'bag/bag.html')