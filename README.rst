======================
Django Nested Formsets
======================

.. image:: https://travis-ci.org/nyergler/nested-formset.png?branch=master
   :target: https://travis-ci.org/nyergler/nested-formset

Formsets_ are a Django abstraction that make it easier to manage
multiple instances of a single Form_ on a page. In 2009 I wrote a
`blog post`_ about using nesting formsets using Django 1.1. This is a
generic implementation of the technique described there, targeting
Django 1.5 and later. A `follow-up blog post`_ provides additional
context.

Installing
==========

You can install Django Nested Formsets using your favorite package
management tool. For example::

  $ pip install django-nested-formset

You can also install the `latest development version`_\ ::

  $ pip install django-nested-formset==dev

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

To run the unit test suite, run the following from within the
virtualenv::

   $ python ./bin/django-admin.py test --settings=nested_formset.test_settings nested_formset

License
=======

This package is released under a BSD style license. See LICENSE for details.

.. _`latest development version`: https://github.com/nyergler/nested-formset/tarball/master#egg=django_nested_formset-dev
.. _Formsets: https://docs.djangoproject.com/en/1.5/topics/forms/formsets/
.. _Form: https://docs.djangoproject.com/en/1.5/topics/forms/
.. _`blog post`: http://yergler.net/blog/2009/09/27/nested-formsets-with-django/
.. _`follow-up blog post`: http://yergler.net/blog/2013/09/03/nested-formsets-redux/
