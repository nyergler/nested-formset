from setuptools import setup, find_packages
import sys, os

here = os.path.abspath(os.path.dirname(__file__))
README = '' #open(os.path.join(here, 'README.rst')).read()
NEWS = '' #open(os.path.join(here, 'NEWS.txt')).read()


version = '0.1'


setup(name='nested_formset',
      version=version,
      description="",
      long_description=README + '\n\n' + NEWS,
      classifiers=[
          'License :: OSI Approved :: BSD License',
      ],
      keywords='',
      url='https://github.com/nyergler/nested-formset',
      license='BSD',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'Django==1.5.1',
          'django-discover-runner',
          'rebar',
      ],
)
