from django.forms.models import (
    BaseInlineFormSet,
    inlineformset_factory,
    ModelForm,
)


class BaseNestedFormset(BaseInlineFormSet):

    def add_fields(self, form, index):

        # allow the super class to create the fields as usual
        super(BaseNestedFormset, self).add_fields(form, index)

        form.nested = self.nested_formset_class(
            instance=form.instance,
            data=form.data if form.is_bound else None,
            files=form.files if form.is_bound else None,
            prefix='%s-%s' % (
                form.prefix,
                self.nested_formset_class.get_default_prefix(),
            ),
        )

    def is_valid(self):

        result = super(BaseNestedFormset, self).is_valid()

        if self.is_bound:
            # look at any nested formsets, as well
            for form in self.forms:
                if not self._should_delete_form(form):
                    result = result and form.nested.is_valid()

        return result

    def save(self, commit=True):

        result = super(BaseNestedFormset, self).save(commit=commit)

        for form in self.forms:
            if not self._should_delete_form(form):
                form.nested.save(commit=commit)

        return result

    @property
    def media(self):
        return self.empty_form.media + self.empty_form.nested.media


class BaseNestedModelForm(ModelForm):

    def has_changed(self):

        return (
            super(BaseNestedModelForm, self).has_changed() or
            self.nested.has_changed()
        )


def nestedformset_factory(parent_model, model, nested_formset,
                          form=BaseNestedModelForm,
                          formset=BaseNestedFormset, fk_name=None,
                          fields=None, exclude=None, extra=3,
                          can_order=False, can_delete=True,
                          max_num=None, formfield_callback=None,
                          widgets=None, validate_max=False,
                          localized_fields=None, labels=None,
                          help_texts=None, error_messages=None,
                          min_num=None, validate_min=None):
    kwargs = {
        'form': form,
        'formset': formset,
        'fk_name': fk_name,
        'fields': fields,
        'exclude': exclude,
        'extra': extra,
        'can_order': can_order,
        'can_delete': can_delete,
        'max_num': max_num,
        'formfield_callback': formfield_callback,
        'widgets': widgets,
        'validate_max': validate_max,
        'localized_fields': localized_fields,
        'labels': labels,
        'help_texts': help_texts,
        'error_messages': error_messages,
        'min_num': min_num,
        'validate_min': validate_min,
    }

    if kwargs['fields'] is None:
        kwargs['fields'] = [
            field.name
            for field in model._meta.local_fields
        ]

    NestedFormSet = inlineformset_factory(
        parent_model,
        model,
        **kwargs
    )
    NestedFormSet.nested_formset_class = nested_formset

    return NestedFormSet
