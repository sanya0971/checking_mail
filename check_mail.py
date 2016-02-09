import re

def check_email(str):
    data = re.split(r'@', str)
    name = data[0]
    host = data[1]
    name_valid = re.match(r'^([-_a-z0-9]+(\.)?(("!*|:*|,*")|("!*|,*|:*")|(":*|!*|,*")|(":*|,*|!*")|'
                          r'(",*|:*|!*")|(",*|!*|:*")|"")*){0,127}$', name)
    host_valid = re.match(r'^[_a-z0-9]{1,1}[-_a-z0-9]{2,254}[^\-]$', host)

    if name_valid and host_valid:
        return True
    else:
        return False


