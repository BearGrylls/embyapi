# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.create_user_by_name import CreateUserByName

class TestCreateUserByName(unittest.TestCase):
    """CreateUserByName unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> CreateUserByName:
        """Test CreateUserByName
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `CreateUserByName`
        """
        model = CreateUserByName()
        if include_optional:
            return CreateUserByName(
                name = '',
                copy_from_user_id = '',
                user_copy_options = [
                    'UserPolicy'
                    ]
            )
        else:
            return CreateUserByName(
        )
        """

    def testCreateUserByName(self):
        """Test CreateUserByName"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
