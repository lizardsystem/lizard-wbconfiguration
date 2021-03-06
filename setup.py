from setuptools import setup

version = '0.5.7.dev0'

long_description = '\n\n'.join([
    open('README.rst').read(),
    open('TODO.rst').read(),
    open('CREDITS.rst').read(),
    open('CHANGES.rst').read(),
    ])

install_requires = [
    'Django',
    'lizard-security',
    'django-celery',
    'django-extensions',
    'django-nose',
    'djangorestframework',
    'lizard-area',
    'lizard-geo',
    'lizard-fewsnorm',
    'lizard-esf',
    'lizard-portal',
    'lizard-task',
    'lizard-ui >= 3.0',
    'lizard-history >= 0.4.1',
    'pkginfo',
    'dbfpy',
    ],

tests_require = [
    ]

setup(name='lizard-wbconfiguration',
      version=version,
      description="TODO",
      long_description=long_description,
      # Get strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=['Programming Language :: Python',
                   'Framework :: Django',
                   ],
      keywords=[],
      author='TODO',
      author_email='TODO@nelen-schuurmans.nl',
      url='',
      license='GPL',
      packages=['lizard_wbconfiguration'],
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require = {'test': tests_require},
      entry_points={
          'console_scripts': [
          ]},
      )
