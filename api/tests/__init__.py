
from __future__ import unicode_literals

# add patch support to built-in django test client

from django.test.client import RequestFactory, Client


def construct_patch(self, path, data='',
                    content_type='application/octet-stream', **extra):
    """Construct a PATCH request."""
    return self.generic('PATCH', path, data, content_type, **extra)


def send_patch(self, path, data='', content_type='application/octet-stream',
               follow=False, **extra):
    """Send a resource to the server using PATCH."""
    # FIXME: figure out why we need to reimport Client (otherwise NoneType)
    from django.test.client import Client  # @Reimport
    response = super(Client, self).patch(
        path, data=data, content_type=content_type, **extra)
    if follow:
        response = self._handle_redirects(response, **extra)
    return response


RequestFactory.patch = construct_patch
Client.patch = send_patch

from .test_app import *  # noqa
from .test_auth import *  # noqa
from .test_build import *  # noqa
from .test_config import *  # noqa
from .test_container import *  # noqa
from .test_flavor import *  # noqa
from .test_formation import *  # noqa
from .test_key import *  # noqa
from .test_layer import *  # noqa
from .test_node import *  # noqa
from .test_perm import *  # noqa
from .test_provider import *  # noqa
from .test_release import *  # noqa
