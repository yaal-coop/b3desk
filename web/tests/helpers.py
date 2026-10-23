def form_with_action(response, action):
    """Return the form of the page whose action starts with ``action``."""
    return next(
        form for form in response.forms.values() if form.action.startswith(action)
    )


def add_group_members(client_app, group_id, user_ids, status=302):
    """Add users to a group with the admin form, as picked in the combobox."""
    return client_app.post(
        f"/admin/add-group-members/{group_id}",
        {"users-value": [str(user_id) for user_id in user_ids], "add_members": ""},
        status=status,
    )
