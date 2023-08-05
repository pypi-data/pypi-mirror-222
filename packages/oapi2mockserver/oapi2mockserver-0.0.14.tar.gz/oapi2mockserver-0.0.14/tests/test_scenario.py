import unittest

from unittest_data_provider import data_provider

from oapi2mockserver.scenario import Scenario


class SchemaTest(unittest.TestCase):
    def test_it_can_be_created(self):
        scenario = Scenario('/v1/path', 'get', 200, '{"foo": "bar"}', 'application/json')

        self.assertIsInstance(scenario, Scenario)

    def test_it_can_be_created_without_response_body(self):
        scenario = Scenario('/v1/path', 'get', 200, None, 'text/plain')

        self.assertIsInstance(scenario, Scenario)

    def test_it_can_be_created_without_content_type(self):
        scenario = Scenario('/v1/path', 'get', 200, '{"foo": "bar"}')

        self.assertIsInstance(scenario, Scenario)

    def test_it_can_be_created_with_plain_response_body(self):
        scenario = Scenario('/v1/path', 'get', 200, 'foo', 'text/plain')

        self.assertIsInstance(scenario, Scenario)

    def data_provider_scenario_matches():
        return (
            (
                'equal path and operation',
                Scenario('/v1/path', 'get', 200),
                {'path': '/v1/path', 'operation': 'get'},
                True,
            ),
            (
                'scenario path with additional slash',
                Scenario('/v1/path/', 'get', 200),
                {'path': '/v1/path', 'operation': 'get'},
                True,
            ),
            (
                'matching path with additional slash',
                Scenario('/v1/path', 'get', 200),
                {'path': '/v1/path/', 'operation': 'get'},
                True,
            ),
            (
                'scenario operation in uppercase',
                Scenario('/v1/path', 'GET', 200),
                {'path': '/v1/path/', 'operation': 'get'},
                True,
            ),
            (
                'matching operation in uppercase',
                Scenario('/v1/path', 'get', 200),
                {'path': '/v1/path/', 'operation': 'GET'},
                True,
            ),
            (
                'different path',
                Scenario('/v1/path', 'get', 200),
                {'path': '/v1/foo/', 'operation': 'GET'},
                False,
            ),
            (
                'different operation',
                Scenario('/v1/path', 'POST', 200),
                {'path': '/v1/path/', 'operation': 'GET'},
                False,
            ),
        )

    @data_provider(data_provider_scenario_matches)
    def test_it_tells_if_path_and_operation_matches(self, case, scenario, matching, assertion):
        self.assertEqual(assertion, scenario.matches(matching['path'], matching['operation']))

    def test_it_provides_the_expected_response_data(self):
        scenario = Scenario('/v1/path', 'get', 200, '{"foo": "bar"}', 'application/json')

        expected = {
            'statusCode': 200,
            'responseBody': '{"foo": "bar"}',
            'contentType': 'application/json'
        }

        self.assertEqual(expected, scenario.get_expected_response())


if __name__ == '__main__':
    unittest.main()
