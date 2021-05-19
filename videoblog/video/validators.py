from django.core.exceptions import ValidationError



def file_size(value):
    filesize=value.size
    if filesize>8e+9:
        raise ValidationError("max size is 100 mb")
