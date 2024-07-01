from django.utils.text import slugify
from uuid import uuid4 as random

def generate_slug(string:str, model) -> str:

    """
        Returns a unique slug...
    """

    string = slugify(string)

    while (model.objects.filter(slug=string).exists()):
        string = slugify(string) + str(random()[:2])

    return string