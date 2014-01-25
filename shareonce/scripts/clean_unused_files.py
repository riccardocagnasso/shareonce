import sys
import os

from pyramid.paster import bootstrap


if __name__ == '__main__':
    env = bootstrap(sys.argv[1])

    from shareonce.models import *

    for f in File.find_unused().all():
        try:
            os.remove(f.get_file_path())
        except OSError:
            pass
