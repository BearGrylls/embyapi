# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.editors_editor_root import EditorsEditorRoot

class TestEditorsEditorRoot(unittest.TestCase):
    """EditorsEditorRoot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> EditorsEditorRoot:
        """Test EditorsEditorRoot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `EditorsEditorRoot`
        """
        model = EditorsEditorRoot()
        if include_optional:
            return EditorsEditorRoot(
                property_conditions = [
                    embyapi.models.conditions/property_condition.Conditions.PropertyCondition(
                        affected_property_id = '', 
                        condition_type = 'Visible', 
                        target_property_id = '', 
                        simple_condition = 'IsTrue', 
                        value_condition = 'IsEqual', 
                        value = embyapi.models.value.Value(), )
                    ],
                postback_actions = [
                    embyapi.models.actions/postback_action.Actions.PostbackAction(
                        target_editor_id = '', 
                        postback_command_id = '', 
                        command_parameter_property_id = '', )
                    ],
                title_button = embyapi.models.editors/editor_button_item.Editors.EditorButtonItem(
                    editor_type = 'Group', 
                    name = '', 
                    id = '', 
                    allow_empty = True, 
                    is_read_only = True, 
                    is_advanced = True, 
                    display_name = '', 
                    description = '', 
                    feature_requires_premiere = True, 
                    parent_id = '', ),
                editor_items = [
                    embyapi.models.editors/editor_base.Editors.EditorBase(
                        editor_type = 'Group', 
                        name = '', 
                        id = '', 
                        allow_empty = True, 
                        is_read_only = True, 
                        is_advanced = True, 
                        display_name = '', 
                        description = '', 
                        feature_requires_premiere = True, 
                        parent_id = '', )
                    ],
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
            return EditorsEditorRoot(
        )
        """

    def testEditorsEditorRoot(self):
        """Test EditorsEditorRoot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
