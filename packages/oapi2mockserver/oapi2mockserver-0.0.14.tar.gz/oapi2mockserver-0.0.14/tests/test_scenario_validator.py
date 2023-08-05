import unittest

from unittest_data_provider import data_provider

from oapi2mockserver.scenario import Validator
from oapi2mockserver.scenario import Scenario
from oapi2mockserver.scenario import EndpointNotDefinedException
from oapi2mockserver.scenario import InvalidResponseBodySchemaException
from oapi2mockserver.scenario import InvalidResponseContentTypeException


class ScenarioValidatorTest(unittest.TestCase):
    def test_it_can_be_created(self):
        validator = Validator({'paths': {'/v1/foo': {'get': {'responses': {'200': {''}}}}}})
        self.assertIsInstance(validator, Validator)

    def test_it_does_not_fail_when_all_scenarios_are_defined_in_contract(self):
        validator = Validator({'paths': {'/v1/foo/': {'get': {'responses': {'200': {''}}}}}})
        passingScenario = Scenario('/v1/foo', 'get', '200')

        self.assertTrue(validator.validate([passingScenario]))

    def data_provider_failing_scenarios():
        return (
            (
                'undefined path',
                {'paths': {'/v1/foo': {'get': {'responses': {'200': {''}}}}}},
                Scenario('/v1/bar', 'get', '200'),
            ),
            (
                'undefined operation',
                {'paths': {'/v1/foo': {'get': {'responses': {'200': {''}}}}}},
                Scenario('/v1/foo', 'post', '200'),
            ),
            (
                'undefined status code',
                {'paths': {'/v1/foo': {'get': {'responses': {'200': {''}}}}}},
                Scenario('/v1/foo', 'get', '404'),
            ),
        )

    @data_provider(data_provider_failing_scenarios)
    def test_it_fails_when_scenario_endpoint_is_not_defined_in_contract(self, case, paths, failingScenario):
        validator = Validator(paths)

        with self.assertRaises(EndpointNotDefinedException):
            validator.validate([failingScenario])

    def test_it_does_not_fail_when_scenarios_provide_responses_validating_against_schema_in_contract(self):
        validator = Validator({
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'responses': {
                            '200': {
                                'schema': {
                                    'type': 'object',
                                    'required': ['foo'],
                                    'additionalProperties': False,
                                    'properties': {
                                        'foo': {
                                            'type': 'string',
                                            'example': 'bar'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        })
        passingScenario = Scenario('/v1/foo', 'get', '200', '{"foo":"bar"}')

        self.assertTrue(validator.validate([passingScenario]))

    def test_it_does_fail_when_scenario_provide_responses_violating_the_schema_in_contract(self):
        validator = Validator({
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'responses': {
                            '200': {
                                'schema': {
                                    'type': 'object',
                                    'required': ['foo'],
                                    'additionalProperties': False,
                                    'properties': {
                                        'foo': {
                                            'type': 'string',
                                            'example': 'bar'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        })
        failingScenario = Scenario('/v1/foo', 'get', '200', '{"buz":"bar"}')

        with self.assertRaises(InvalidResponseBodySchemaException):
            self.assertTrue(validator.validate([failingScenario]))

    def test_it_does_not_fail_when_scenarios_provide_response_content_types_defined_in_method(self):
        validator = Validator({
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'produces': ['text/html', 'application/json'],
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        passingScenario = Scenario('/v1/foo', 'get', '200', None, 'text/html')

        self.assertTrue(validator.validate([passingScenario]))

    def test_it_does_not_fail_when_scenarios_provide_response_content_types_defined_global(self):
        validator = Validator({
            'produces': ['application/json', 'text/html'],
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        passingScenario = Scenario('/v1/foo', 'get', '200', None, 'text/html')

        self.assertTrue(validator.validate([passingScenario]))

    def test_it_does_fail_when_scenario_provide_response_content_type_not_defined_in_method(self):
        validator = Validator({
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'produces': ['text/html', 'application/json'],
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        failingScenario = Scenario('/v1/foo', 'get', '200', None, 'image/png')

        with self.assertRaises(InvalidResponseContentTypeException):
            self.assertTrue(validator.validate([failingScenario]))

    def test_it_does_fail_when_scenario_provide_response_content_types_not_defined_global(self):
        validator = Validator({
            'produces': ['application/json', 'text/html'],
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        failingScenario = Scenario('/v1/foo', 'get', '200', None, 'image/png')

        with self.assertRaises(InvalidResponseContentTypeException):
            self.assertTrue(validator.validate([failingScenario]))

    def test_it_ignores_global_content_types_and_fails_when_content_types_are_defined_for_operation_and_invalid_content_type_is_set_in_scenario(self):
        validator = Validator({
            'produces': ['image/png'],
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'produces': ['text/html', 'application/json'],
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        failingScenario = Scenario('/v1/foo', 'get', '200', None, 'image/png')

        with self.assertRaises(InvalidResponseContentTypeException):
            self.assertTrue(validator.validate([failingScenario]))

    def test_it_ignores_global_content_types_and_passes_when_content_types_are_defined_for_operation_and_valid_content_type_is_set_in_scenario(self):
        validator = Validator({
            'produces': ['image/png'],
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'produces': ['text/html', 'application/json'],
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        passingScenario = Scenario('/v1/foo', 'get', '200', None, 'text/html')

        self.assertTrue(validator.validate([passingScenario]))

    def test_it_does_not_fail_when_no_content_types_are_defined_at_all(self):
        validator = Validator({
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'responses': {
                            '200': {}
                        }
                    }
                }
            }
        })
        passingScenario = Scenario('/v1/foo', 'get', '200', None, 'text/html')

        self.assertTrue(validator.validate([passingScenario]))

    def test_it_does_not_fail_when_no_json_is_set_as_response_body_and_content_type_is_not_application_json(self):
        validator = Validator({
            'paths': {
                '/v1/foo/': {
                    'get': {
                        'produces': ['application/json', 'text/plain'],
                        'responses': {
                            '200': {
                                'schema': {
                                    'type': 'object',
                                    'required': ['foo'],
                                    'additionalProperties': False,
                                    'properties': {
                                        'foo': {
                                            'type': 'string',
                                            'example': 'bar'
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        })
        passingScenario = Scenario('/v1/foo', 'get', '200', None, 'text/plain')

        self.assertTrue(validator.validate([passingScenario]))

if __name__ == '__main__':
    unittest.main()
