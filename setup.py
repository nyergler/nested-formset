from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()
NEWS = open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1.4'


setup(name='django-nested-formset',
      description='Nest Django formsets for multi-level hierarchical editing',
      author='Nathan Yergler',
      author_email='nathan@yergler.net',
      version=version,
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          'Framework :: Django',
          'Framework :: Django :: 1.11',
          'License :: OSI Approved :: BSD License',
          'Development Status :: 5 - Production/Stable',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
      ],
      keywords='',
      url='https://github.com/nyergler/nested-formset',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'Django<2.0',
      ],
      tests_require=[
          'rebar',
      ],
      test_suite='nested_formset.tests.run_tests',
)
