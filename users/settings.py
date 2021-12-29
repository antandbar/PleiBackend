from django.conf import settings

GENERAL = 'GEN'
GAMING = 'GAM'
SPONSOR = 'SPO'
INTERNAL = 'INT'

DEFAULT_T_USER = (
    (GENERAL, 'General'),
    (GAMING, 'Gaming'),
    (SPONSOR, 'Sponsor'),
    (INTERNAL, 'Internal'),

)

T_USER = getattr(settings, 'T_USER', DEFAULT_T_USER)


HEAD_EMAIL = "Bienvenido "
MESSAGE_EMAIL = "Debe completar el proceso introduciendo el número: "
MESSAGE_PHONE = "Debe completar el proceso introduciendo el número: "