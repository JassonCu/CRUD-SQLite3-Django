from django.http import JsonResponse
from django.shortcuts import render
from .models import Course

# Create your views here.

def course_list(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        courses = list(Course.objects.values())
        return JsonResponse({'data': courses})
    return render(request, 'courses/course_list.html')
