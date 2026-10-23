from flask_babel import gettext as _
from markupsafe import Markup
from wtforms.widgets import html_params
from wtforms_htmx_components import ChipsWidget
from wtforms_htmx_components import ComboboxWidget


class DsfrChipsWidget(ChipsWidget):
    """Render each picked value as a dismissible DSFR tag."""

    def render_chip(self, field, value, label, remove):
        button = (
            Markup('<span class="fr-tag">{}</span>').format(label)
            if remove is None
            else remove(
                value=value,
                label=label,
                id=False,
                class_="fr-tag fr-tag--dismiss",
                aria_label=_("Retirer %(label)s", label=label),
            )
        )
        hidden = html_params(type="hidden", name=field.name, value=value)
        return f"<span>{button}<input {hidden}></span>"


class DsfrComboboxWidget(ComboboxWidget):
    """Lay the combobox out with the DSFR classes.

    The picked tags come first, then the query input with its search
    button, then the suggestions.
    """

    def __call__(self, field, **kwargs):
        attrs = {"class": "combobox-wrap", **kwargs}
        search = (
            field.search(class_="fr-btn fr-btn--secondary")
            if "search" in field.form
            else ""
        )
        return Markup(
            f"<div {html_params(**attrs)}>"
            f"{field.value()}"
            f'<div class="combobox-search">{field.query()}{search}</div>'
            f"{field.suggestions()}"
            f"</div>"
        )
