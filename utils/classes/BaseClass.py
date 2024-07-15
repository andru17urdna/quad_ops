class BaseClass:
    parser = None
    args = []

    def __init__(self, *args, **kwargs) -> None:

        self.set_args(*args, **kwargs)
        self.parse_args(*args, **kwargs)

        self.execute(self.parser.args, *args, **kwargs)

    def set_args(self, *args, **kwargs):
        for arg in self.args:
            self.parser._add_argument(arg)

    def parse_args(self, *args, **kwargs):
        self.parser._parse_args(*args, **kwargs)


    def execute(self, args, *_args, **kwargs):
        pass