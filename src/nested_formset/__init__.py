from django.forms.models import (
    BaseInlineFormSet,
    inlineformset_factory,
)


class BaseNestedFormset(BaseInlineFormSet):

    def add_fields(self, form, index):

        # allow the super class to create the fields as usual
        super(BaseNestedFormset, self).add_fields(form, index)

        form.nested = self.nested_formset_class(
            instance=form.instance,
        )


def nested_formset_factory(parent_model, child_model, grandchild_model):

    parent_child = inlineformset_factory(
        parent_model,
        child_model,
        formset=BaseNestedFormset,
    )

    parent_child.nested_formset_class = inlineformset_factory(
        child_model,
        grandchild_model,
    )

    return parent_child
