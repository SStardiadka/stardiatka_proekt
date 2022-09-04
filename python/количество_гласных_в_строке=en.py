import re
def glasn(str):
    'количество_гласных_в_строке=en'
    return len(re.findall(r'[AEIOUYaeiouy]', str))
glasn('foobar')