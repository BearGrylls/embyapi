# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.system_service_api import SystemServiceApi


class TestSystemServiceApi(unittest.TestCase):
    """SystemServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = SystemServiceApi()

    def tearDown(self) -> None:
        pass

    def test_get_system_endpoint(self) -> None:
        """Test case for get_system_endpoint

        Gets information about the request endpoint
        """
        pass

    def test_get_system_info(self) -> None:
        """Test case for get_system_info

        Gets information about the server
        """
        pass

    def test_get_system_info_public(self) -> None:
        """Test case for get_system_info_public

        Gets public information about the server
        """
        pass

    def test_get_system_logs_by_name(self) -> None:
        """Test case for get_system_logs_by_name

        Gets a log file
        """
        pass

    def test_get_system_logs_by_name_lines(self) -> None:
        """Test case for get_system_logs_by_name_lines

        Gets a log file
        """
        pass

    def test_get_system_logs_query(self) -> None:
        """Test case for get_system_logs_query

        Gets a list of available server log files
        """
        pass

    def test_get_system_ping(self) -> None:
        """Test case for get_system_ping

        """
        pass

    def test_get_system_releasenotes(self) -> None:
        """Test case for get_system_releasenotes

        Gets release notes
        """
        pass

    def test_get_system_releasenotes_versions(self) -> None:
        """Test case for get_system_releasenotes_versions

        Gets release notes
        """
        pass

    def test_get_system_wakeonlaninfo(self) -> None:
        """Test case for get_system_wakeonlaninfo

        Gets wake on lan information
        """
        pass

    def test_post_system_ping(self) -> None:
        """Test case for post_system_ping

        """
        pass

    def test_post_system_restart(self) -> None:
        """Test case for post_system_restart

        Restarts the application, if needed
        """
        pass

    def test_post_system_shutdown(self) -> None:
        """Test case for post_system_shutdown

        Shuts down the application
        """
        pass


if __name__ == '__main__':
    unittest.main()
