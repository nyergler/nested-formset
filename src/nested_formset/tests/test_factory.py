from unittest import TestCase

from django.forms.models import BaseInlineFormSet, inlineformset_factory
from nested_formset.tests import models as test_models

from nested_formset import nestedformset_factory


class FactoryTests(TestCase):

    def test_factory_calls(self):

        child_formset = inlineformset_factory(test_models.Building, test_models.Tenant)
        nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
        )

    def test_factory_returns_formset(self):

        child_formset = inlineformset_factory(test_models.Building, test_models.Tenant)
        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
        )

        self.assertTrue(issubclass(nested_formset, BaseInlineFormSet))
