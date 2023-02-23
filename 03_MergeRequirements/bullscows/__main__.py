import sys
import urllib
import urllib.request

from bullscows.bullscows import ask
from bullscows.bullscows import inform
from bullscows.bullscows import bullscows
from bullscows.bullscows import gameplay

if len(sys.argv) in (2, 3):
    try:
        with open(sys.argv[1], 'r') as f:
            dictionary = f.read().split()
    except:
        try:
            f = urllib.request.urlopen(sys.argv[1])
        except:
            raise RuntimeError('not correct dictionary')
        dictionary = f.read().decode().split()
    if len(sys.argv) == 3:
        length = sys.argv[2]
    else:
        length = 5
    print(gameplay(ask, inform, dictionary))
else:
    raise RuntimeError('python -m bullscows словарь [длина]')
