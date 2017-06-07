from unittest import TestCase

import django
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

    def test_fk_name_for_factory(self):

        fk_name = 'block'
        # Should pass because fk_name is valid
        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=self.child_formset,
            fk_name='block'
        )()
        # Fails because address is not fk
        with self.assertRaises(ValueError):
            nested_formset = nestedformset_factory(
                test_models.Block,
                test_models.Building,
                nested_formset=self.child_formset,
                fk_name='address'
            )()

    def test_min_num_for_factory(self):

        num = 3
        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=self.child_formset,
            min_num=num
        )

        self.assertEqual(
            num,
            nested_formset.min_num
        )


    def test_validate_min_for_factory(self):
        # Default is False
        validate_min = True
        nested_formset = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=self.child_formset,
            validate_min=validate_min
        )

        self.assertEqual(
            validate_min,
            nested_formset.validate_min
        )
