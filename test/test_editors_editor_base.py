# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.editors_editor_base import EditorsEditorBase

class TestEditorsEditorBase(unittest.TestCase):
    """EditorsEditorBase unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditorsEditorBase:
        """Test EditorsEditorBase
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditorsEditorBase`
        """
        model = EditorsEditorBase()
        if include_optional:
            return EditorsEditorBase(
                editor_type = 'Group',
                name = '',
                id = '',
                allow_empty = True,
                is_read_only = True,
                is_advanced = True,
                display_name = '',
                description = '',
                feature_requires_premiere = True,
                parent_id = ''
            )
        else:
            return EditorsEditorBase(
        )
        """

    def testEditorsEditorBase(self):
        """Test EditorsEditorBase"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
