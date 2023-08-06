# -*- coding: utf-8 -*-
import os

import pytest
from pip_services4_components.config import ConfigParams

from test.clients.DummyClientFixture import DummyClientFixture
from test.clients.DummyAzureFunctionClient import DummyAzureFunctionClient

app_name = os.environ.get('AZURE_FUNCTION_APP_NAME')
function_name = os.environ.get('AZURE_FUNCTION_NAME')
protocol = os.environ.get('AZURE_FUNCTION_PROTOCOL')
auth_code = os.environ.get('AZURE_FUNCTION_AUTH_CODE')
uri = os.environ.get('AZURE_FUNCTION_URI')

config = ConfigParams.from_tuples(
    'connection.uri', uri,
    'connection.protocol', protocol,
    'connection.app_name', app_name,
    'connection.function_name', function_name,
    'credential.auth_code', auth_code,
)


@pytest.mark.skipif(not uri and (not app_name or not function_name or not protocol or not auth_code),
                    reason='No Azure credentials')
class TestDummyAzureFunctionClient:
    client: DummyAzureFunctionClient
    fixture: DummyClientFixture

    def setup_method(self):
        self.client = DummyAzureFunctionClient()
        self.client.configure(config)

        self.fixture = DummyClientFixture(self.client)

        self.client.open(None)

    def teardown(self):
        self.client.close(None)

    def test_crud_operations(self):
        self.fixture.test_crud_operations()
