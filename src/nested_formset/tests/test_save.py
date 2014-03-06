from django.test import TestCase

from django.forms.models import inlineformset_factory
from nested_formset.tests import models as test_models
from nested_formset.tests.util import get_form_data

from nested_formset import nestedformset_factory


class EditTests(TestCase):

    def setUp(self):

        child_formset = inlineformset_factory(test_models.Building, test_models.Tenant)
        self.formset_class = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
        )

        self.block = test_models.Block.objects.create()

    def test_edit_building(self):

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

    def test_edit_tenant(self):

        building = test_models.Building.objects.create(
            block=self.block,
            address='829 S Mulberry St.',
        )
        tenant = test_models.Tenant.objects.create(
            building=building,
            name='John Doe',
            unit='42',
        )

        form_data = get_form_data(
            self.formset_class(instance=self.block)
        )

        form_data.update({
            'building_set-0-address': '405 S. Wayne St.',
            'building_set-0-tenant_set-0-unit': '42A',
        })

        form = self.formset_class(
            instance=self.block,
            data=form_data,
        )

        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(
            test_models.Tenant.objects.get(id=tenant.id).unit,
            '42A',
        )
        self.assertEqual(
            test_models.Tenant.objects.get(id=tenant.id).building,
            building,
        )


class CreationTests(TestCase):

    def setUp(self):

        child_formset = inlineformset_factory(test_models.Building, test_models.Tenant)
        self.formset_class = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
        )

        self.block = test_models.Block.objects.create()

    def test_create_building(self):

        unbound_form = self.formset_class(instance=self.block)
        self.assertEqual(unbound_form.initial_forms, [])

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

        self.assertEqual(self.block.building_set.count(), 1)

    def test_create_tenant(self):

        building = test_models.Building.objects.create(
            block=self.block,
            address='829 S Mulberry St.',
        )
        self.assertEqual(building.tenant_set.count(), 0)

        form_data = get_form_data(
            self.formset_class(instance=self.block)
        )

        form_data.update({
            'building_set-0-tenant_set-0-name': 'John Doe',
            'building_set-0-tenant_set-0-unit': '42A',
        })

        form = self.formset_class(
            instance=self.block,
            data=form_data,
        )

        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(building.tenant_set.all().count(), 1)
        self.assertEqual(
            building.tenant_set.all()[0].name,
            'John Doe',
        )

    def test_create_building_tenant(self):

        self.assertEqual(self.block.building_set.count(), 0)

        form_data = get_form_data(
            self.formset_class(instance=self.block)
        )
        form_data.update({
            'building_set-0-address': '829 S Mulberry St.',
            'building_set-0-tenant_set-0-name': 'John Doe',
            'building_set-0-tenant_set-0-unit': '42A',
        })

        form = self.formset_class(
            instance=self.block,
            data=form_data,
        )

        self.assertTrue(form.is_valid())
        form.save()

        # the building was created and linked to the block
        self.assertEqual(self.block.building_set.count(), 1)
        building = self.block.building_set.all()[0]
        self.assertEqual(
            building.address,
            '829 S Mulberry St.',
        )

        # the tenant was also created and linked to the new building
        self.assertEqual(building.tenant_set.count(), 1)
        self.assertEqual(
            building.tenant_set.all()[0].name,
            'John Doe',
        )


class DeleteTests(TestCase):

    def setUp(self):

        child_formset = inlineformset_factory(test_models.Building, test_models.Tenant)
        self.formset_class = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
        )

        self.block = test_models.Block.objects.create()
        self.building = test_models.Building.objects.create(
            block=self.block,
            address='829 S Mulberry St.',
        )
        self.tenant = test_models.Tenant.objects.create(
            building=self.building,
            name='John Doe',
            unit='42',
        )

    def test_delete_tenant(self):

        self.assertEqual(self.building.tenant_set.count(), 1)

        unbound_form = self.formset_class(instance=self.block)
        form_data = get_form_data(unbound_form)

        form_data.update({
            'building_set-0-tenant_set-0-DELETE': True,
        })

        form = self.formset_class(
            instance=self.block,
            data=form_data,
        )

        self.assertTrue(form.is_valid())
        form.save()

        # the building is intact...
        self.assertEqual(
            test_models.Block.objects.get(id=self.block.id).building_set.count(),
            1)

        # ... and the tenant is deleted
        self.assertEqual(self.building.tenant_set.count(), 0)

    def test_delete_building(self):

        self.assertEqual(test_models.Tenant.objects.all().count(), 1)
        self.assertEqual(self.block.building_set.count(), 1)
        self.assertEqual(self.building.tenant_set.count(), 1)

        unbound_form = self.formset_class(instance=self.block)
        form_data = get_form_data(unbound_form)

        form_data.update({
            'building_set-0-DELETE': True,
        })

        form = self.formset_class(
            instance=self.block,
            data=form_data,
        )

        self.assertTrue(form.is_valid())
        form.save()

        self.assertEqual(self.block.building_set.count(), 0)

        self.assertEqual(test_models.Tenant.objects.all().count(), 0)
