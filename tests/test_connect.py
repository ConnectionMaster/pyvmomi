# VMware vSphere Python SDK tests
#
# Copyright (c) 2008-2025 Broadcom. All Rights Reserved.
# The term "Broadcom" refers to Broadcom Inc. and/or its subsidiaries.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tests
import unittest
import sys

from pyVim import connect
from pyVim.connect import TOKEN_TYPE_SSPI
from pyVmomi import vim

if sys.version_info >= (3, 3):
    from unittest.mock import patch, MagicMock
else:
    from mock import patch, MagicMock


class ConnectionTests(tests.VCRTestBase):

    @tests.VCRTestBase.my_vcr.use_cassette('basic_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once', decode_compressed_response=True)
    def test_basic_connection(self):
        # see: http://python3porting.com/noconv.html
        si = connect.Connect(host='vcsa',
                             user='my_user',
                             pwd='my_password')
        cookie = si._stub.cookie
        session_id = si.content.sessionManager.currentSession.key
        # NOTE (hartsock): The cookie value should never change during
        # a connected session. That should be verifiable in these tests.
        self.assertEqual(cookie, si._stub.cookie)
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(session_id is not None)
        self.assertEqual('5220f274-9ba1-a663-b51f-9b16fca182f1', session_id)

    @tests.VCRTestBase.my_vcr.use_cassette('sspi_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once')
    def test_sspi_connection(self):
        # see: http://python3porting.com/noconv.html
        si = connect.Connect(host='vcsa',
                             tokenType=TOKEN_TYPE_SSPI,
                             token='my_base64token')
        cookie = si._stub.cookie
        session_id = si.content.sessionManager.currentSession.key
        # NOTE (hartsock): The cookie value should never change during
        # a connected session. That should be verifiable in these tests.
        self.assertEqual(cookie, si._stub.cookie)
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(session_id is not None)
        self.assertEqual('5220f274-9ba1-a663-b51f-9b16fca182f1', session_id)

    @tests.VCRTestBase.my_vcr.use_cassette('basic_connection_bad_password.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_basic_connection_bad_password(self):
        def should_fail():
            connect.Connect(host='vcsa',
                            user='my_user',
                            pwd='bad_password')

        self.assertRaises(vim.fault.InvalidLogin, should_fail)

    @tests.VCRTestBase.my_vcr.use_cassette('smart_connection.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once', decode_compressed_response=True)
    def test_smart_connection(self):
        # see: http://python3porting.com/noconv.html
        si = connect.SmartConnect(host='vcsa',
                                  user='my_user',
                                  pwd='my_password')
        session_id = si.content.sessionManager.currentSession.key
        # NOTE (hartsock): assertIsNotNone does not work in Python 2.6
        self.assertTrue(session_id is not None)
        self.assertEqual('52a67ed8-0f0b-1714-4534-86a177fc5158', session_id)

    def test_disconnect_on_no_connection(self):
        connect.Disconnect(None)

    @tests.VCRTestBase.my_vcr.use_cassette('ssl_tunnel.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_ssl_tunnel(self):
        connect.SoapStubAdapter('sdkTunnel', 8089, httpProxyHost='vcsa').GetConnection()

    def test_ssl_tunnel_http_failure(self):
        import socket
        def should_fail():
            conn = connect.SoapStubAdapter('vcsa', 80, httpProxyHost='unreachable').GetConnection()
            conn.request('GET', '/')
            conn.getresponse()
        self.assertRaises((OSError, socket.gaierror), should_fail)

    @tests.VCRTestBase.my_vcr.use_cassette('ssl_tunnel.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='none')
    def test_http_proxy(self):
        connect.SoapStubAdapter('sdkTunnel', 8089, httpProxyHost='vcsa').GetConnection()


    @patch('ssl.SSLContext.load_cert_chain')
    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_http_proxy_with_cert_file(self, https_conn, ssl_ctx):
        certFile = 'my_cert_file'
        certKeyFile = 'my_key_file'
        conn = connect.SoapStubAdapter(
            'sdkTunnel',
            8089,
            httpProxyHost='vcsa',
            certKeyFile=certKeyFile,
            certFile=certFile
        ).GetConnection()
        conn.request('GET', '/')
        https_conn.assert_called_once_with(host='vcsa', port=80, context=unittest.mock.ANY)
        conn.set_tunnel.assert_called_once_with('sdkTunnel', 8089, {})
        ssl_ctx.assert_called_once_with(certFile, certKeyFile)

    @tests.VCRTestBase.my_vcr.use_cassette('http_proxy.yaml',
                      cassette_library_dir=tests.fixtures_path,
                      record_mode='once')
    def test_http_proxy(self):
        conn = connect.SoapStubAdapter(
            'vcenter.test',
            httpProxyHost='my-http-proxy',
            httpProxyPort=8080
        ).GetConnection()
        self.assertEqual(conn._tunnel_host, 'vcenter.test')
        self.assertEqual(conn._tunnel_port, 443)
        conn.request('GET', '/')
        conn.getresponse()

    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_host_attr_ipv4(self, https_conn):
        connect.SoapStubAdapter(
            host="123.123.123.123"
        ).GetConnection()
        https_conn.assert_called_with(host='123.123.123.123', port=443)

        connect.SoapStubAdapter(host="123.123.123.123", port=1234).GetConnection()
        https_conn.assert_called_with(host='123.123.123.123', port=1234)

    @patch('pyVmomi.SoapAdapter.HTTPConnection')
    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_url_attr_ipv4(self, https_conn, http_conn):
        connect.SoapStubAdapter(url="http://123.123.123.123/testpath").GetConnection()
        http_conn.assert_called_with(host='123.123.123.123', port=http_conn.default_port)

        connect.SoapStubAdapter(url="https://123.123.123.123:1234/testpath").GetConnection()
        https_conn.assert_called_with(host='123.123.123.123', port=1234)

    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_host_attr_ipv6(self, https_conn):
        connect.SoapStubAdapter(host="fd00:0:0:0:0:0:7:3001").GetConnection()
        https_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=443)

        connect.SoapStubAdapter(host="fd00:0:0:0:0:0:7:3001", port=1234).GetConnection()
        https_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=1234)

        connect.SoapStubAdapter(host="[fd00:0:0:0:0:0:7:3001]").GetConnection()
        https_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=443)

        connect.SoapStubAdapter(host="[fd00:0:0:0:0:0:7:3001]", port=1234).GetConnection()
        https_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=1234)

        connect.SoapStubAdapter(host="[fd00:0:0:0:0:0:7:3001", port=1234).GetConnection()
        https_conn.assert_called_with(host='[fd00:0:0:0:0:0:7:3001', port=1234)

    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_url_attr_ipv6(self, https_conn):
        connect.SoapStubAdapter(url="https://[fd00:0:0:0:0:0:7:3001]/testpath").GetConnection()
        https_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=https_conn.default_port)

        connect.SoapStubAdapter(url="https://[fd00:0:0:0:0:0:7:3001]:1234/testpath").GetConnection()
        https_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=1234)

    @patch('pyVmomi.SoapAdapter.HTTPConnection')
    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_negative_port(self, https_conn, http_conn):
        connect.SoapStubAdapter(host='fd00:0:0:0:0:0:7:3001', port=-1234).GetConnection()
        https_conn.assert_not_called()
        http_conn.assert_called_with(host='fd00:0:0:0:0:0:7:3001', port=1234)

    @patch('pyVmomi.SoapAdapter.HTTPSConnection')
    def test_url_priority(self, https_conn):
        connect.SoapStubAdapter(
            host='fd00:0:0:0:0:0:7:3001',
            port=-1234,
            url="https://123.123.123.123/testpath"
        ).GetConnection()
        https_conn.assert_called_with(host='123.123.123.123', port=https_conn.default_port)


if __name__ == '__main__':
    unittest.main()
