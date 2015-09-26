======================
Django Nested Formsets
======================

.. image:: https://travis-ci.org/nyergler/nested-formset.png?branch=master
   :target: https://travis-ci.org/nyergler/nested-formset

Formsets_ are a Django abstraction that make it easier to manage
multiple instances of a single Form_ on a page. In 2009 I wrote a
`blog post`_ about using nesting formsets using Django 1.1. This is a
generic implementation of the technique described there, targeting
Django 1.6 and later. A `follow-up blog post`_ provides additional
context.

Note that I **do not** advocate the use of nested Formsets: in every case
I've considered them, they've led to usability issues and overly
complex view code. This repository was created as an exercise in test
driven development and abstraction.

Your mileage may vary.

Installing
==========

You can install Django Nested Formsets using your favorite package
management tool. For example::

  $ pip install django-nested-formset

You can also install the latest development version::

  $ pip install git+https://github.com/nyergler/nested-formset#egg=django-nested-formset

After installing the package, you can use the
``nestedformset_factory`` function to create your formset class.

Developing
==========

If you'd like to work on the source, I suggest cloning the repository
and creating a virtualenv.

::

   $ cd nested-formset
   $ virtualenv .
   $ source bin/activate
   $ python setup.py develop

The last line will install the installation and test dependencies.

To run the unit test suite, run the following::

   $ python setup.py test

See Also
========

* `Django Formset documentation`_
* `jquery.django-formset`_ Dynamic creation of formsets from the empty
  formset.

License
=======

This package is released under a BSD style license. See LICENSE for details.

.. _Formsets: https://docs.djangoproject.com/en/1.5/topics/forms/formsets/
.. _`Django Formset documentation`: Formsets_
.. _Form: https://docs.djangoproject.com/en/1.5/topics/forms/
.. _`blog post`: http://yergler.net/blog/2009/09/27/nested-formsets-with-django/
.. _`follow-up blog post`: http://yergler.net/blog/2013/09/03/nested-formsets-redux/
.. _`jquery.django-formset`: https://github.com/mbertheau/jquery.django-formset
