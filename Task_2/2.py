Task.objects.filter(project__pk=1).values('type__type')
