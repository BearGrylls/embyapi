# coding: utf-8

"""
    Emby Server REST API

    Explore the Emby Server API

    The version of the OpenAPI document: 4.8.7.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from embyapi.models.process_run_metrics_process_metric_point import ProcessRunMetricsProcessMetricPoint

class TestProcessRunMetricsProcessMetricPoint(unittest.TestCase):
    """ProcessRunMetricsProcessMetricPoint unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ProcessRunMetricsProcessMetricPoint:
        """Test ProcessRunMetricsProcessMetricPoint
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ProcessRunMetricsProcessMetricPoint`
        """
        model = ProcessRunMetricsProcessMetricPoint()
        if include_optional:
            return ProcessRunMetricsProcessMetricPoint(
                time = '',
                cpu_percent = 1.337,
                virtual_memory = 1.337,
                working_set = 1.337
            )
        else:
            return ProcessRunMetricsProcessMetricPoint(
        )
        """

    def testProcessRunMetricsProcessMetricPoint(self):
        """Test ProcessRunMetricsProcessMetricPoint"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
