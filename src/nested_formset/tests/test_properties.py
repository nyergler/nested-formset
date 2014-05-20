from unittest import TestCase

from django import forms
from django.forms.models import inlineformset_factory
from nested_formset.tests import models as test_models

from nested_formset import nestedformset_factory


class StyledTextInput(forms.TextInput):

    class Media:
        css = {
            'all': ('widget.css',),
        }


class TenantForm(forms.ModelForm):

    name = forms.CharField(
        max_length=50,
        widget=StyledTextInput,
    )

    class Meta:
        model = test_models.Tenant
        fields = ('name', 'unit')

    class Media:
        css = {
            'all': ('layout.css',),
        }


class BuildingForm(forms.ModelForm):

    class Meta:
        model = test_models.Building
        exclude = ()

    class Media:
        css = {
            'print': ('building.css',),
        }


class PropertyTests(TestCase):

    def setUp(self):

        child_formset = inlineformset_factory(
            test_models.Building,
            test_models.Tenant,
            fields=(
                'name',
                'unit',
            ),
            form=TenantForm,
        )
        self.formset_class = nestedformset_factory(
            test_models.Block,
            test_models.Building,
            nested_formset=child_formset,
            form=BuildingForm,
        )

    def test_media_rolls_up_child_media(self):

        block = test_models.Block.objects.create()
        form = self.formset_class(
            instance=block,
        )

        self.assertIn('building.css', form.media._css['print'])

    def test_media_rolls_up_grandchild_media(self):

        block = test_models.Block.objects.create()
        form = self.formset_class(
            instance=block,
        )

        self.assertIn('layout.css', form.media._css['all'])

    def test_widget_media_rolls_up(self):

        block = test_models.Block.objects.create()
        form = self.formset_class(
            instance=block,
        )

        self.assertIn('widget.css', form.media._css['all'])
