from django.core.urlresolvers import reverse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
)

from nested_formset import nested_formset_factory

from blocks import models


class ListBlocksView(ListView):

    model = models.Block


class CreateBlockView(CreateView):
    model = models.Block

    def get_success_url(self):

        return reverse('blocks-list')


class EditBuildingsView(UpdateView):
    model = models.Block

    def get_template_names(self):

        return ['blocks/building_form.html']

    def get_form_class(self):

        return nested_formset_factory(
            models.Block,
            models.Building,
            models.Tenant,
        )

    def get_success_url(self):

        return reverse('blocks-list')
