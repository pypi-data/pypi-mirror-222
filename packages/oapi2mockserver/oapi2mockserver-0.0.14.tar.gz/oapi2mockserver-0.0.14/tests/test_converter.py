import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest_data_provider import data_provider
import os
from io import StringIO
import warnings
import requests
import prance
import sys
from json.decoder import JSONDecodeError
from prance.util.formats import ParseError
from jsonschema import ValidationError

import json

from oapi2mockserver.scenario import Scenario
from oapi2mockserver import converter

# ignores warnings decorator
def ignore_warnings(test_func):
    def do_test(self, *args, **kwargs):
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            test_func(self, *args, **kwargs)
    return do_test

""" test for the converter class located in the main package """
class Test_Converter(unittest.TestCase):

	def setUp(self):
		self.convert = converter.Converter()

	""" test the setup of scenarios with manualy added content"""
	def test_scenarios_manually(self):
		# cannot set empty array as scenarios
		self.convert.set_scenarios([])
		self.assertEqual('', self.convert.scenarios)
		# cannot set None
		self.convert.set_scenarios(None)
		self.assertEqual('', self.convert.scenarios)

	""" data provider for test_convert_opai """
	def data_provider_convert_opai_cases():
		return (
			(
				'Test method convert_opai with a missing status code in the yml file', 
				'tests/yml/Contracts_Consuming_user_missing_status_code.yaml',
				ParseError,
				'',
				None
			),
			(
				'Test method convert_opai with correct content in the yml file and no scenarios', 
				'tests/yml/Contracts_Consuming_user.yaml',
				None,
				'',
				(200, 201, 204)
			),
			(
				'Test method convert_opai with correct content in the yml file and scenarios for failed requests', 
				'tests/yml/Contracts_Consuming_user.yaml',
				None,
				[Scenario('/v1/agents', 'post', 401), Scenario('/v1/users', 'put', 404)],
				(401, 404)
			),
			(
				'Test method convert_opai with invalid example',
				'tests/yml/Contracts_Consuming_user_invalid_example.yaml',
				None,
				'',
				None,
				ValidationError
			),
			(
				'Test method convert_opai with invalid scenario example',
				'tests/yml/Contracts_Consuming_user.yaml',
				None,
				[Scenario('/v1/agents', 'post', 401, '{"foo":"bar"}')],
				None,
				ValidationError
			),
		)

	""" test oapi converter method """
	@ignore_warnings
	@data_provider(data_provider_convert_opai_cases)
	def test_convert_opai(self, case, file_path, parse_error, scenario, status_codes, error=None):
		# empty check
		self.assertFalse(self.convert.swagger)
		# read dummy file and parse data
		if (parse_error is not None):
			# parsing error expected
			with self.assertRaises(parse_error):
				parser = prance.ResolvingParser(file_path)
			# nothing has been added
			self.assertFalse(self.convert.swagger)
			self.unset_all()
			return
		# no parsing error expected
		parser = prance.ResolvingParser(file_path)
		parse_data = parser.specification
		# trigger converter
		self.convert.set_scenarios(scenario)

		if error is not None:
			with self.assertRaises(error):
				self.convert.convert_opai(parse_data)
			self.unset_all()
			return

		self.convert.convert_opai(parse_data)
		# check that content has been added
		self.assertIn('consumes', self.convert.swagger)
		self.assertIn('produces', self.convert.swagger)
		self.assertNotIn('invalid_field', self.convert.swagger)
		self.assertIsNotNone(self.convert.currentPath)

		self.assertIsNotNone(self.convert.expectations)
		# check returned status codes
		for i in range(0, len(self.convert.expectations)):
			self.assertEqual(
				status_codes[i],
				self.convert.expectations[i].expectation['httpResponse']['statusCode']
			)
			# check if json validation is successful
			self.assertIsInstance(json.loads(json.dumps(self.convert.expectations[i].expectation)), dict)
		# reset converter for further iterations
		self.unset_all()

	""" Resets all content in the converter variable to its default state.
		This is not part of the tearDown() method, since its not being triggered by data providers """
	def unset_all(self):
		self.convert.scenarios = ''
		self.convert.spec = {}
		self.convert.swagger = {}
		self.convert.currentPath = None
		self.convert.currentOperation = {}
		self.convert.currentStatusCode = {}
		self.convert.expectations = []
