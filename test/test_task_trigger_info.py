# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.task_trigger_info import TaskTriggerInfo

class TestTaskTriggerInfo(unittest.TestCase):
    """TaskTriggerInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TaskTriggerInfo:
        """Test TaskTriggerInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TaskTriggerInfo`
        """
        model = TaskTriggerInfo()
        if include_optional:
            return TaskTriggerInfo(
                type = '',
                time_of_day_ticks = 56,
                interval_ticks = 56,
                system_event = 'WakeFromSleep',
                day_of_week = 'Sunday',
                max_runtime_ticks = 56
            )
        else:
            return TaskTriggerInfo(
        )
        """

    def testTaskTriggerInfo(self):
        """Test TaskTriggerInfo"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
