# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.notification_category_info import NotificationCategoryInfo

class TestNotificationCategoryInfo(unittest.TestCase):
    """NotificationCategoryInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NotificationCategoryInfo:
        """Test NotificationCategoryInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NotificationCategoryInfo`
        """
        model = NotificationCategoryInfo()
        if include_optional:
            return NotificationCategoryInfo(
                name = '',
                id = '',
                events = [
                    embyapi.models.notification_type_info.NotificationTypeInfo(
                        name = '', 
                        id = '', 
                        category_name = '', 
                        category_id = '', )
                    ]
            )
        else:
            return NotificationCategoryInfo(
        )
        """

    def testNotificationCategoryInfo(self):
        """Test NotificationCategoryInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
