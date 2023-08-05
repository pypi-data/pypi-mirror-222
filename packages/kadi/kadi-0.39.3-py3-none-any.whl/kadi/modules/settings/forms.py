# Copyright 2020 Karlsruhe Institute of Technology
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import re
from datetime import timedelta
from urllib.parse import urlparse

from flask import current_app
from flask_babel import gettext as _
from flask_babel import lazy_gettext as _l
from flask_login import current_user
from marshmallow import fields
from marshmallow import ValidationError
from marshmallow.validate import OneOf
from marshmallow.validate import Range
from wtforms.validators import DataRequired
from wtforms.validators import Email
from wtforms.validators import EqualTo
from wtforms.validators import Length
from wtforms.validators import Optional
from wtforms.validators import URL

import kadi.lib.constants as const
from kadi.lib.api.models import PersonalToken
from kadi.lib.api.utils import get_access_token_scopes
from kadi.lib.conversion import empty_str
from kadi.lib.conversion import normalize
from kadi.lib.conversion import strip
from kadi.lib.forms import BaseConfigForm
from kadi.lib.forms import BooleanField
from kadi.lib.forms import FileField
from kadi.lib.forms import JSONField
from kadi.lib.forms import KadiForm
from kadi.lib.forms import LFTextAreaField
from kadi.lib.forms import PasswordField
from kadi.lib.forms import StringField
from kadi.lib.forms import SubmitField
from kadi.lib.forms import UTCDateTimeField
from kadi.lib.schemas import KadiSchema
from kadi.lib.utils import utcnow
from kadi.modules.accounts.models import LocalIdentity
from kadi.modules.accounts.models import User


class OrcidField(StringField):
    """Custom field to process and validate ORCID iDs."""

    ORCID_REGEX = re.compile("^\\d{4}-\\d{4}-\\d{4}-\\d{3}[0-9X]$")

    def process_formdata(self, valuelist):
        super().process_formdata(valuelist)

        if valuelist:
            if self.data:
                orcid = self.data.strip()

                url_prefix = f"{const.URL_ORCID}/"
                error_msg = _("Not a valid ORCID iD.")

                if orcid.startswith(url_prefix):
                    orcid = orcid[len(url_prefix) :]

                if not self.ORCID_REGEX.search(orcid):
                    raise ValueError(error_msg)

                # Calculate and verify the checksum of the ORCID iD according to ISO
                # 7064 MOD 11,2.
                total = 0

                for char in orcid[:-1]:
                    if char == "-":
                        continue

                    total = (total + int(char)) * 2

                remainder = total % 11
                result = (12 - remainder) % 11

                checksum = "X" if result == 10 else str(result)

                if checksum != orcid[-1]:
                    raise ValueError(error_msg)

                self.data = orcid
            else:
                self.data = None


class EditProfileForm(KadiForm):
    """A form for use in editing a user's profile information.

    :param user: The user to prepopulate the fields with.
    """

    displayname = StringField(
        _l("Display name"), filters=[normalize], validators=[DataRequired()]
    )

    email = StringField(
        _l("Email"),
        filters=[strip],
        validators=[
            DataRequired(),
            Email(),
            Length(max=LocalIdentity.Meta.check_constraints["email"]["length"]["max"]),
        ],
    )

    show_email = BooleanField(_l("Show email address on profile"))

    orcid = OrcidField(
        "ORCID iD",
        description=_l(
            "The ORCID iD is publicly displayed in your profile and may be used when"
            " exporting or publishing resources."
        ),
    )

    about = LFTextAreaField(
        _l("About"),
        filters=[empty_str],
        validators=[Length(max=User.Meta.check_constraints["about"]["length"]["max"])],
    )

    image = FileField(_l("Profile picture"))

    remove_image = BooleanField(_l("Remove current profile picture"))

    submit = SubmitField(_l("Save changes"))

    def __init__(self, user, *args, **kwargs):
        data = {
            "displayname": user.identity.displayname,
            "email": user.identity.email,
            "show_email": not user.email_is_private,
            "orcid": user.orcid,
            "about": user.about,
        }

        super().__init__(*args, data=data, **kwargs)

        if user.identity.type != const.AUTH_PROVIDER_TYPE_LOCAL:
            self.email.description = _(
                "Automatically set based on your %(type)s account.",
                type=user.identity.Meta.identity_type["name"],
            )

        self.displayname.validators.append(
            Length(
                max=current_app.config["AUTH_PROVIDERS"][user.identity.type][
                    "identity_class"
                ].Meta.check_constraints["displayname"]["length"]["max"]
            )
        )


class ChangePasswordForm(KadiForm):
    """A form for use in changing a local user's password."""

    password = PasswordField(_l("Current password"), validators=[DataRequired()])

    new_password = PasswordField(
        _l("New password"), validators=[DataRequired(), Length(min=8)]
    )

    new_password2 = PasswordField(
        _l("Repeat new password"),
        validators=[
            DataRequired(),
            EqualTo("new_password", _l("Passwords do not match.")),
        ],
    )

    submit = SubmitField(_l("Save changes"))


class _HomeLayoutSchema(KadiSchema):
    resource = fields.String(required=True, validate=OneOf(list(const.RESOURCE_TYPES)))

    visibility = fields.String(
        required=True,
        validate=OneOf(
            ["all", const.MODEL_VISIBILITY_PRIVATE, const.MODEL_VISIBILITY_PUBLIC]
        ),
    )

    creator = fields.String(required=True, validate=OneOf(["any", "self"]))

    max_items = fields.Integer(required=True, validate=Range(min=0, max=10))


class HomeLayoutField(JSONField):
    """Custom field to process and validate preferences for the home page layout."""

    def __init__(self, *args, **kwargs):
        kwargs["default"] = const.USER_CONFIG_HOME_LAYOUT_DEFAULT
        super().__init__(*args, **kwargs)

    def process_formdata(self, valuelist):
        super().process_formdata(valuelist)

        if valuelist:
            try:
                schema = _HomeLayoutSchema(many=True)
                self.data = schema.load(self.data)

            except ValidationError as e:
                self.data = self.default
                raise ValueError("Invalid data structure.") from e


class CustomizationPreferencesForm(BaseConfigForm):
    """A form for use in setting user-specific config items related to customization.

    :param user: (optional) The user to pass to :class:`.BaseConfigForm`. Defaults to
        the current user.
    """

    hide_introduction = BooleanField(
        _l("Hide introduction"),
        description=_l('Hide the "Get started" section on the home page.'),
    )

    home_layout = HomeLayoutField(
        _l("Home page layout"),
        description=_l(
            'Resource types to be shown on the home page in the "Latest Updates"'
            " section with corresponding filters. Note that only groups with membership"
            " are shown."
        ),
    )

    def __init__(self, *args, user=None, **kwargs):
        user = user if user is not None else current_user
        super().__init__(*args, user=user, **kwargs)


class ScopesField(StringField):
    """Custom field to process and validate access token scopes."""

    def process_formdata(self, valuelist):
        super().process_formdata(valuelist)

        if valuelist:
            scopes = []

            error_msg = _("One or more scopes are invalid.")
            access_token_scopes = get_access_token_scopes()

            for scope in self.data.split():
                parts = scope.split(".", 1)

                if len(parts) != 2:
                    raise ValueError(error_msg)

                object_name, action = parts

                if action not in access_token_scopes.get(object_name, []):
                    raise ValueError(error_msg)

                if scope not in scopes:
                    scopes.append(scope)

            if scopes:
                self.data = " ".join(sorted(scopes))
            else:
                self.data = None


class NewPersonalTokenForm(KadiForm):
    """A form for use in creating new personal tokens."""

    name = StringField(
        _l("Name"),
        filters=[normalize],
        validators=[
            DataRequired(),
            Length(max=PersonalToken.Meta.check_constraints["name"]["length"]["max"]),
        ],
    )

    expires_at = UTCDateTimeField(
        _l("Expires at"),
        validators=[Optional()],
        description=_l("The default expiration date is %(num)d weeks.", num=4),
        default=lambda: utcnow() + timedelta(days=28),
    )

    scope = ScopesField(
        _l("Scopes"),
        description=_l(
            "Scopes can restrict a token's access to specific resources or actions. If"
            " no scopes are selected, full access is granted to the token."
        ),
    )

    submit = SubmitField(_l("Create token"))

    def clear(self):
        """Reset all relevant field data of this form to their default values."""
        self.name.data = self.scope.data = ""
        self.expires_at.data = self.expires_at.default()
        self.expires_at.raw_data = None


class RedirectURIsField(LFTextAreaField):
    """Custom field to process and validate OAuth2 redirect URIs.

    :param max_len: (optional) The maximum length of each invidiual URI.
    """

    def __init__(self, *args, max_len=2048, **kwargs):
        self.max_len = max_len

        kwargs["default"] = []
        super().__init__(*args, **kwargs)

    def process_formdata(self, valuelist):
        super().process_formdata(valuelist)

        if valuelist:
            uris = []
            error_msg = _("One or more redirect URIs are invalid.")

            for uri in self.data.split("\n"):
                uri = uri.strip()

                if not uri:
                    continue

                if len(uri) > self.max_len:
                    raise ValueError(error_msg)

                result = urlparse(uri)

                if not result.scheme or not result.netloc:
                    raise ValueError(error_msg)

                if result.scheme != "https":
                    netloc = result.netloc.split(":", 1)[0]

                    # Allow HTTP in combination with localhost as well.
                    if netloc != "localhost" or result.scheme != "http":
                        raise ValueError(error_msg)

                if uri not in uris:
                    uris.append(uri)

            self.data = uris

    def to_dict(self):
        data = super().to_dict()

        if isinstance(self.data, list):
            data["data"] = "\n".join(self.data)

        return data


class BaseApplicationForm(KadiForm):
    """Base form class for use in creating or updating OAuth2 applications."""

    client_name = StringField(
        _l("Name"),
        filters=[normalize],
        validators=[DataRequired(), Length(max=150)],
        description=_l("The name of the application (displayed to users)."),
    )

    client_uri = StringField(
        _l("Website URL"),
        filters=[strip],
        validators=[DataRequired(), Length(max=2048), URL()],
        description=_l("The URL of the application (displayed to users)."),
    )

    redirect_uris = RedirectURIsField(
        _l("Redirect URIs"),
        validators=[DataRequired()],
        description=_l(
            "One or multiple redirect URIs (one per line) that can be used for the"
            " authorization callback. All URIs must use HTTPS (except for localhost)."
        ),
    )

    scope = ScopesField(
        _l("Scopes"),
        description=_l(
            "Scopes can restrict an application's access to specific resources or"
            " actions. If no scopes are selected, full access is granted to the"
            " application."
        ),
    )


class NewApplicationForm(BaseApplicationForm):
    """A form for use in creating new OAuth2 applications."""

    submit = SubmitField(_l("Register application"))

    def clear(self):
        """Reset all relevant field data of this form to their default values."""
        self.client_name.data = self.client_uri.data = self.scope.data = ""
        self.redirect_uris.data = self.redirect_uris.default


class EditApplicationForm(BaseApplicationForm):
    """A form for use in editing existing OAuth2 application.

    :param application: The application to edit, used for prefilling the form.
    """

    submit = SubmitField(_l("Save changes"))

    def __init__(self, application, *args, **kwargs):
        super().__init__(*args, obj=application, **kwargs)
