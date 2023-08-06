from lobsang.directives.base import Directive


class JSONDirective(Directive):
    def embed(self, message: str) -> (str, dict):
        # TODO: add original message to the dict
        raise NotImplementedError("JSONDirective is not implemented yet.")

    def parse(self, response: str) -> (str, dict):
        """
         e.g. a JSONDirective would try to parse the response to a JSON object (returned in the info dict)
        while the response remains unchanged.
        """
        raise NotImplementedError("JSONDirective is not implemented yet.")


# import json
# from jsonschema.validators import validator_for
#
#
# class Parser:
#     """
#     A parser to extract data from messages based on a JSON schema.
#
#
#     # TODO: Reafactor and explain retry / aut-fixing capabilities.
#     # This parser provides a simple interface for parsing data from messages.
#     # The schema is defined as a JSON schema, and the parser will validate the messages against the schema.
#     # It is based on a JSON schema that defines the structure of the data to be parsed.
#     # This parser provides the ability to load a JSON schema from a file, and to parse
#     # messages into the schema.
#     """
#
#     def __init__(self, schema: dict):
#         """
#         Initializes the parser with the provided schema.
#
#         :param schema: The schema used to parse the data. It should be a valid JSON schema.
#         """
#         self.schema = schema
#         self.validator = validator_for(schema)
#
#         # Validate schema
#         self.validator.check_schema(schema)
#
#     def parse(self, message: str):
#         """
#         Parses the message into the data schema.
#
#         :param message: The message to parse.
#         :return: The parsed data.
#         """
#         # TODO: Implement this.
#         pass
#
#     @classmethod
#     def from_file(cls, schema_path):
#         """
#         Create a new parser from a JSON schema file.
#
#         :param schema_path: The path to the JSON schema file.
#         :return: A new instance of the parser.
#         :raises: FileNotFoundError if the schema file does not exist.
#         :raises: jsonschema.exceptions.SchemaError if the schema is invalid.
#         """
#         with open(schema_path) as schema_file:
#             schema = json.load(schema_file)
#
#         return cls(schema=schema)
#
#
# if __name__ == '__main__':
#     schema = {
#         "type": "object",
#         "properties": {
#             "name": {"type": "string"},
#             "age": {"type": "integer", "minimum": 0},
#             "height": {"type": "number"},
#         }
#     }
#
#     parser = Parser(schema=schema)
#     parser.parse(message={"name": "John", "age": 30, "height": 1.8})
