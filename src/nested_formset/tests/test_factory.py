from unittest import TestCase

from django.forms.models import BaseInlineFormSet
from nested_formset.tests import models as test_models

from nested_formset import nested_formset_factory


class FactoryTests(TestCase):

    def test_factory_calls(self):

        nested_formset = nested_formset_factory(
            test_models.Block,
            test_models.Building,
            test_models.Tenant,
        )

    def test_factory_returns_formset(self):

        nested_formset = nested_formset_factory(
            test_models.Block,
            test_models.Building,
            test_models.Tenant,
        )

        self.assertTrue(issubclass(nested_formset, BaseInlineFormSet))
