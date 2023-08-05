import unittest

from jsonschema import ValidationError

from oapi2mockserver.open_api_schema import OpenAPISchema


class ValidateJsonAgainstSchemaTest(unittest.TestCase):
    def test_throw_error_on_invalid_data(self):
        schema = OpenAPISchema()

        provided_schema = '{"type": "string", "example": "foo"}'
        provided_json = '3'

        with self.assertRaises(ValidationError):
            schema.validate_json(provided_schema, provided_json)

    def test_return_true_on_valid_json(self):
        schema = OpenAPISchema()

        provided_schema = '{"type": "string","example": "foo"}'
        provided_json = '"foo"'

        self.assertTrue(schema.validate_json(provided_schema, provided_json))


if __name__ == '__main__':
    unittest.main()
