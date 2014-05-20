from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.2'


setup(name='django-nested-formset',
      description='Nest Django formsets for multi-level hierarchical editing',
      author='Nathan Yergler',
      author_email='nathan@yergler.net',
      version=version,
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          'License :: OSI Approved :: BSD License',
          'Development Status :: 4 - Beta',
          'Framework :: Django',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
      ],
      keywords='',
      url='https://github.com/nyergler/nested-formset',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Django>=1.5',
      ],
      tests_require=[
          'django-discover-runner',
          'rebar',
      ],
      test_suite='nested_formset.tests.run_tests',
)
