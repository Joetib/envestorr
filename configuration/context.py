from configuration.models import Configuration


def global_context(request):
    
    return {"configuration": Configuration.object()}
