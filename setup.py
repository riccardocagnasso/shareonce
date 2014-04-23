import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

requires = [
    'pyramid',
    'SQLAlchemy',
    'transaction',
    'pyramid_tm',
    'pyramid_debugtoolbar',
    'zope.sqlalchemy',
    'waitress',
    'alembic',
    'assetgen',
    'pyramid_assetgen',
    'Pillow',
    'python-magic',
    'pyramid-mako'
    ]

setup(name='shareonce',
      version='0.0',
      description='shareonce',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Riccardo Cagnasso',
      author_email='riccardo@phascode.org',
      url='www.shareonce.net',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='shareonce',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = shareonce:main
      [console_scripts]
      initialize_shareonce_db = shareonce.scripts.initializedb:main
      """,
      )
