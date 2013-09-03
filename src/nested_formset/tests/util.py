from rebar.testing import flatten_to_dict


def get_form_data(formset):
    """Return the form data for formset as a dict."""

    form_data = flatten_to_dict(formset)

    for form in formset:
        form_data.update(
            flatten_to_dict(form.nested)
        )

    return form_data
