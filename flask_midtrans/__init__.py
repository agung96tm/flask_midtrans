from flask import Flask
from midtransclient import CoreApi, Snap


# Version
VERSION = (0, 0, '1a')
__version__ = ".".join(str(i) for i in VERSION)


# Environments
MIDTRANS_SETTINGS_AVAILABLE = {
    'is_production': 'MIDTRANS_IS_PRODUCTION',
    'server_key': 'MIDTRANS_SERVER_KEY',
    'client_key': 'MIDTRANS_CLIENT_KEY'
}
MIDTRANS_DOCS = "https://github.com/Midtrans/midtrans-python-client"


# Core
class Midtrans(object):
    def __init__(self, app=None):
        self._default_settings = {}
        self._core = None
        self._snap = None

        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask):
        self._default_settings = {
            key: app.config.get(value, '')
            for (key, value) in MIDTRANS_SETTINGS_AVAILABLE.items()
        }

    @property
    def core(self):
        if not self._core:
            settings = self.__check_default_settings(self._default_settings)
            self._core = CoreApi(**settings)
        return self._core

    @property
    def snap(self):
        if not self._snap:
            settings = self.__check_default_settings(self._default_settings)
            self._snap = Snap(**settings)
        return self._snap

    def __check_default_settings(self, default_settings):
        for key, value in default_settings.items():
            if value == '':
                raise RuntimeError(
                    "The '%s' is not available on your settings. Please refer to '%s' how to set it." % (
                        MIDTRANS_SETTINGS_AVAILABLE[key], MIDTRANS_DOCS)
                )
        return default_settings

    def update_settings(self, **kwargs):
        _updated_settings = {
            key: kwargs.get(key) if bool(kwargs.get(key)) else value
            for (key, value) in self._default_settings.items()
        }
        self._default_settings = _updated_settings
        self._core = None
        self._snap = None
