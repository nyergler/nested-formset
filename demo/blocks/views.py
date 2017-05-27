from django.core.urlresolvers import reverse
from django.forms.models import inlineformset_factory
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from nested_formset import nestedformset_factory

from blocks import models


class ListBlocksView(ListView):

    model = models.Block
    fields = '__all__'


class CreateBlockView(CreateView):

    model = models.Block
    fields = '__all__'

    def get_success_url(self):

        return reverse('blocks-list')


class EditBuildingsView(UpdateView):

    model = models.Block
    fields = '__all__'

    def get_template_names(self):

        return ['blocks/building_form.html']

    def get_form_class(self):

        return nestedformset_factory(
            models.Block,
            models.Building,
            nested_formset=inlineformset_factory(
                models.Building,
                models.Tenant,
                fields = '__all__'
            )
        )

    def get_success_url(self):

        return reverse('blocks-list')
