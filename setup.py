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
    'psycopg2',
    'alembic',
    'assetgen',
    'pyramid_assetgen',
    'PIL',
    'python-magic',
    'pyramid-mako'
    ]

setup(name='linkme',
      version='0.0',
      description='linkme',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
        ],
      author='Riccardo Cagnasso',
      author_email='riccardo@phascode.org',
      url='www.linkme.com',
      keywords='web wsgi bfg pylons pyramid',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='linkme',
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = linkme:main
      [console_scripts]
      initialize_linkme_db = linkme.scripts.initializedb:main
      """,
      )
