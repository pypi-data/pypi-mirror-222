# override authentication backends at package level
AUTHENTICATION_BACKENDS = [
    'djangoldp_component.auth.backends.BasicAuthBackend',
    'djangoldp_account.auth.backends.EmailOrUsernameAuthBackend',
    'guardian.backends.ObjectPermissionBackend',
    'djangoldp_account.auth.backends.ExternalUserBackend'
]