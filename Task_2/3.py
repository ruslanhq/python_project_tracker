Task.objects.filter(description__icontains='Надо').values('project__name')
