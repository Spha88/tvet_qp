from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from papers.models import Subject

def index(request):
    subjects = Subject.objects.all().order_by('name')[:10]
    return render(request, 'pages/index.html', {'subjects': subjects})


def subjects(request):
    subjects = Subject.objects.all().order_by('name')

    paginator = Paginator(subjects, 10)
    page = request.GET.get('page')
    paged_subjects = paginator.get_page(page)

    return render(request, 'pages/subjects.html', {'subjects': paged_subjects})


def subject(request, id): 
    subject = get_object_or_404(Subject, id=id)
    question_papers = subject.questionpaper_set.all().order_by('-year')
    return render(request, 'pages/subject.html', {'subject': subject, 'question_papers': question_papers})


def subject_level(request, level):
    subjects = Subject.objects.all().filter(level=level)
    return render(request, 'pages/subject_level.html', {'subjects': subjects, 'level': level})


def search(request):
    query_list = Subject.objects.order_by('name')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        print(keyword)
        if keyword:
            query_list = query_list.filter(name__icontains=keyword)

    return render(request, 'pages/search.html', {'subjects': query_list, 'values': request.GET })