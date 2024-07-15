import re

def camel_to_snake(name):
    # Insert underscores before capital letters
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    # Insert underscores between lower case and upper case letters
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1)
    # Convert the string to lower case
    return s2.lower()

class BaseClass:
    parser = None
    args = []

    def __init__(self, *args, **kwargs) -> None:

        self.set_args(*args, **kwargs)
        self.parse_args(*args, **kwargs)

        try:
            self.execute(self.parser.args, *args, **kwargs)

        except Exception as err:
            error_method_name = camel_to_snake(err.__class__.__name__) 

            if hasattr(self, error_method_name):
                return getattr(self, error_method_name)(err, args)
            else:
                return self.exception(err)


    def set_args(self, *args, **kwargs):
        for arg in self.args:
            self.parser._add_argument(arg)

    def parse_args(self, *args, **kwargs):
        self.parser._parse_args(*args, **kwargs)

    def execute(self, args, *_args, **kwargs):
        pass

    def exception(self, err):
        print("Error:", err)