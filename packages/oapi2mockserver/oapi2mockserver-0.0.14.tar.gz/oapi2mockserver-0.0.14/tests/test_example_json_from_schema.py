import unittest

from jsonschema import ValidationError

from oapi2mockserver.open_api_schema import OpenAPISchema, ExampleNotFoundException


class ExampleJsonFromSchema(unittest.TestCase):
    def test_get_primitive_example(self):
        schema = OpenAPISchema()

        provided_schema = '{"type": "string", "example": "foo"}'
        expected_json = '"foo"'

        self.assertEqual(expected_json, schema.get_example_json(provided_schema))

    def test_get_object_example(self):
        schema = OpenAPISchema()

        provided_schema = """
        {
            "type": "object",
            "properties": {
                "foo": {
                    "type": "string",
                    "example": "bar"
                }
            }
        }
        """
        expected_json = '{"foo": "bar"}'

        self.assertEqual(expected_json, schema.get_example_json(provided_schema))

    def test_get_array_example(self):
        schema = OpenAPISchema()

        provided_schema = """
        {
            "type": "array",
            "items": {
                "type": "string",
                "example": "bar"
            }
        }
        """
        expected_json = '["bar"]'

        self.assertEqual(expected_json, schema.get_example_json(provided_schema))

    def test_deep_nested_schema(self):
        schema = OpenAPISchema()

        provided_schema = """
        {
            "type": "object",
            "properties": {
                "foos": {
                    "type": "array",
                    "items": {
                        "type": "integer",
                        "example": 2
                    }
                },
                "bars": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "some_property": {
                                "type": "string",
                                "example": "some_value"
                            }
                        }
                    }
                },
                "bar": {
                    "type": "object",
                    "properties": {
                        "some_property": {
                            "type": "string",
                            "example": "some_value"
                        }
                    }
                },
                "buz": {
                    "type": "string",
                    "example": "buz"
                }
            }
        }
        """
        expected_json = '{"foos": [2], "bars": [{"some_property": "some_value"}], "bar": {"some_property": "some_value"}, "buz": "buz"}'

        self.assertEqual(expected_json, schema.get_example_json(provided_schema))

    def test_raises_exception_when_no_example_was_found(self):
        schema = OpenAPISchema()

        provided_schema = """
        {"type": "string"}
        """

        with self.assertRaises(ExampleNotFoundException):
            schema.get_example_json(provided_schema)

    def test_raises_validation_error_when_example_does_not_validate_against_schema(self):
        schema = OpenAPISchema()

        provided_schema = """
        {
           "type": "object",
           "properties": {
               "foo": {
                   "type": "string",
                   "example": 12
               }
           }
        }
        """

        with self.assertRaises(ValidationError):
            schema.get_example_json(provided_schema)


if __name__ == '__main__':
    unittest.main()
