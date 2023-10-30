from .models import Link

def ctx_dict(request):
    ctx = {l.key : l.url for l in Link.objects.all()}
    return ctx