
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UppercaseValidator(object):

    '''The password must contain at least 1 uppercase letter, A-Z.'''

    def validate(self, password, user=None):
        if not re.findall('[A-Z]', password):
            raise ValidationError(
                _("The password must contain at least 1 uppercase letter, A-Z."),
                code='password_no_upper',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 uppercase letter, A-Z."
        )


class LowercaseValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[a-z]', password):
            raise ValidationError(
                _("The password must contain at least 1 lowercase letter, a-z."),
                code='password_no_lower',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 lowercase letter, a-z."
        )


class SpecialCharValidator(object):

    ''' The password must contain at least 1 special character @#$%!^&* '''

    def validate(self, password, user=None):
        if not re.findall('[@#$%!^&*]', password):
            raise ValidationError(
                _("The password must contain at least 1 special character: " +
                  "@#$%!^&*"),
                code='password_no_symbol',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least 1 special character: " +
            "@#$%!^&*"
        )