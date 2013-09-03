from unittest import TestCase

from django.forms.models import BaseInlineFormSet
from nested_formset.tests import models as test_models
from rebar.testing import flatten_to_dict

from nested_formset import nested_formset_factory


class ValidationTests(TestCase):

    def setUp(self):

        self.formset_class = nested_formset_factory(
            test_models.Block,
            test_models.Building,
            test_models.Tenant,
        )

    def test_is_valid_calls_is_valid_on_nested(self):

        block = test_models.Block.objects.create()

        form_data = flatten_to_dict(self.formset_class(instance=block))
        form_data.update({
            'building_set-0-address': '123 Main St',
            'building_set-0-tenant_set-0-name': 'John Doe',
        })

        form = self.formset_class(
            instance=block,
            data=form_data,
        )

        # this is not valid -- unit is a required field for Tenants
        self.assertFalse(form.is_valid())
