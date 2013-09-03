from unittest import TestCase

from django.forms.models import BaseInlineFormSet
from nested_formset.tests import models as test_models
from nested_formset.tests.util import get_form_data

from nested_formset import nested_formset_factory


class EditTests(TestCase):

    def setUp(self):

        self.formset_class = nested_formset_factory(
            test_models.Block,
            test_models.Building,
            test_models.Tenant,
        )

        self.block = test_models.Block.objects.create()

    def test_edit_block(self):

        building = test_models.Building.objects.create(
            block=self.block,
            address='829 S Mulberry St.',
        )

        unbound_form = self.formset_class(instance=self.block)
        form_data = get_form_data(unbound_form)

        form_data.update({
            'building_set-0-address': '405 S. Wayne St.',
        })

        form = self.formset_class(
            instance=self.block,
            data=form_data,
        )

        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(
            test_models.Building.objects.get(id=building.id).address,
            '405 S. Wayne St.',
        )
