# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.api.user_service_api import UserServiceApi


class TestUserServiceApi(unittest.TestCase):
    """UserServiceApi unit test stubs"""

    def setUp(self) -> None:
        self.api = UserServiceApi()

    def tearDown(self) -> None:
        pass

    def test_delete_users_by_id(self) -> None:
        """Test case for delete_users_by_id

        Deletes a user
        """
        pass

    def test_delete_users_by_id_trackselections_by_tracktype(self) -> None:
        """Test case for delete_users_by_id_trackselections_by_tracktype

        Clears audio or subtitle track selections for a user
        """
        pass

    def test_get_users_by_id(self) -> None:
        """Test case for get_users_by_id

        Gets a user by Id
        """
        pass

    def test_get_users_by_userid_typedsettings_by_key(self) -> None:
        """Test case for get_users_by_userid_typedsettings_by_key

        Gets a typed user setting
        """
        pass

    def test_get_users_itemaccess(self) -> None:
        """Test case for get_users_itemaccess

        Gets a list of users
        """
        pass

    def test_get_users_prefixes(self) -> None:
        """Test case for get_users_prefixes

        Gets a list of users
        """
        pass

    def test_get_users_public(self) -> None:
        """Test case for get_users_public

        Gets a list of publicly visible users for display on a login screen.
        """
        pass

    def test_get_users_query(self) -> None:
        """Test case for get_users_query

        Gets a list of users
        """
        pass

    def test_post_users_authenticatebyname(self) -> None:
        """Test case for post_users_authenticatebyname

        Authenticates a user
        """
        pass

    def test_post_users_by_id(self) -> None:
        """Test case for post_users_by_id

        Updates a user
        """
        pass

    def test_post_users_by_id_authenticate(self) -> None:
        """Test case for post_users_by_id_authenticate

        Authenticates a user
        """
        pass

    def test_post_users_by_id_configuration(self) -> None:
        """Test case for post_users_by_id_configuration

        Updates a user configuration
        """
        pass

    def test_post_users_by_id_configuration_partial(self) -> None:
        """Test case for post_users_by_id_configuration_partial

        Updates a user configuration
        """
        pass

    def test_post_users_by_id_delete(self) -> None:
        """Test case for post_users_by_id_delete

        Deletes a user
        """
        pass

    def test_post_users_by_id_password(self) -> None:
        """Test case for post_users_by_id_password

        Updates a user's password
        """
        pass

    def test_post_users_by_id_policy(self) -> None:
        """Test case for post_users_by_id_policy

        Updates a user policy
        """
        pass

    def test_post_users_by_id_trackselections_by_tracktype_delete(self) -> None:
        """Test case for post_users_by_id_trackselections_by_tracktype_delete

        Clears audio or subtitle track selections for a user
        """
        pass

    def test_post_users_by_userid_typedsettings_by_key(self) -> None:
        """Test case for post_users_by_userid_typedsettings_by_key

        Updates a typed user setting
        """
        pass

    def test_post_users_forgotpassword(self) -> None:
        """Test case for post_users_forgotpassword

        Initiates the forgot password process for a local user
        """
        pass

    def test_post_users_forgotpassword_pin(self) -> None:
        """Test case for post_users_forgotpassword_pin

        Redeems a forgot password pin
        """
        pass

    def test_post_users_new(self) -> None:
        """Test case for post_users_new

        Creates a user
        """
        pass


if __name__ == '__main__':
    unittest.main()
