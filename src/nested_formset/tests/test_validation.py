from unittest import TestCase

from django.forms.models import inlineformset_factory
from nested_formset.tests import models as test_models
from nested_formset.tests.util import get_form_data

from nested_formset import nestedformset_factory


class ValidationTests(TestCase):

    def setUp(self):

        child_formset = inlineformset_factory(test_models.Building, test_models.Tenant)
        self.formset_class = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
        )

    def test_is_valid_calls_is_valid_on_nested(self):

        block = test_models.Block.objects.create()

        form_data = get_form_data(self.formset_class(instance=block))
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
