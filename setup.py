from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()


version = '0.1'


setup(name='django-nested-formset',
      description='Nest Django formsets for multi-level hierarchical editing',
      author='Nathan Yergler',
      author_email='nathan@yergler.net',
      version=version,
      long_description=README,
      classifiers=[
          'License :: OSI Approved :: BSD License',
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
          'django-discover-runner',
          'rebar',
      ],
)
