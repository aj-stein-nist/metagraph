from xmlschema import XMLSchema

class MetaschemaXsdValidator:
    def __init__(self, schema, definition):
        self.schema = XMLSchema(schema)
        self.definition = definition
        self._errors = []

    def errors(self):
        """Return errors from last completed validation pass.
        """
        return self._errors

    def validate(self):
        """Use the schema initialized with the validator instance to perform
        XSD validation on the target Metaschema definition content, return any
        errors, if found.
        """
        # Purge the errors in the event schema rerun on the same file.
        self.reset()
        _errors = self.schema.iter_errors(self.definition)
        for idx, e in enumerate(_errors, start=1):
            self._errors.append(e.__str__())
        return self.errors()

    def is_valid(self):
        """Use the schema initialized with the validator instance to perform
        XSD validation on the target Metaschema definition content. This utility
        function will run validate and return a boolean value with result, true
        if the Metaschema definition is valid without any errors, false otherwise.
        """
        return len(self.errors()) == 0

    def reset(self):
        """Reset previously set errors in the error list from the class instance
        so they are not constantly re-added between validation cycles.
        """
        self._errors = []
