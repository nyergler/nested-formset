from unittest import TestCase

from django.forms.models import BaseInlineFormSet, inlineformset_factory
from nested_formset.tests import models as test_models

from nested_formset import nestedformset_factory


class FactoryTests(TestCase):

    def setUp(self):

        self.child_formset = inlineformset_factory(
            test_models.Building,
            test_models.Tenant,
            fields=(
                'name',
                'unit',
            ),
        )

    def test_factory_returns_formset(self):

        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=self.child_formset,
        )

        self.assertTrue(issubclass(nested_formset, BaseInlineFormSet))

    def test_override_fields_for_factory(self):

        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=self.child_formset,
            fields=(
                'block',
            ),
        )

        self.assertEqual(
            tuple(nested_formset.form.base_fields.keys()),
            ('block',),
        )

    def test_exclude_fields_for_factory(self):

        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=self.child_formset,
            exclude=(
                'address',
            ),
        )

        self.assertEqual(
            tuple(nested_formset.form.base_fields.keys()),
            ('block',),
        )
