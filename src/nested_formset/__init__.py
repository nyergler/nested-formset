from django.forms.models import inlineformset_factory


def nested_formset_factory(parent_model, child_model, grandchild_model):

    return inlineformset_factory(
        parent_model,
        child_model,
    )
