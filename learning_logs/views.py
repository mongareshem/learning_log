from django.shortcuts import render

from .models import Topic

def index(request):
    """The home page for learning_log"""

    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics_available = Topic.objects.order_by('date_added')
    context = {'topics': topics_available}

    return render(request, 'learning_logs/topics.html', context)
