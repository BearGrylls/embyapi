# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.library_add_media_path import LibraryAddMediaPath

class TestLibraryAddMediaPath(unittest.TestCase):
    """LibraryAddMediaPath unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LibraryAddMediaPath:
        """Test LibraryAddMediaPath
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LibraryAddMediaPath`
        """
        model = LibraryAddMediaPath()
        if include_optional:
            return LibraryAddMediaPath(
                id = '',
                path = '',
                path_info = embyapi.models.media_path_info.MediaPathInfo(
                    path = '', 
                    network_path = '', 
                    username = '', 
                    password = '', ),
                refresh_library = True
            )
        else:
            return LibraryAddMediaPath(
        )
        """

    def testLibraryAddMediaPath(self):
        """Test LibraryAddMediaPath"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
