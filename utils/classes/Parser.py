import argparse

class Parser:
    def __init__(self, *args, **kwargs) -> None:
        self.argument_parser = argparse.ArgumentParser(*args, **kwargs)

    def _add_argument(self, argument, *args, **kwargs):        
        self.argument_parser.add_argument(*argument._args, **argument._kwargs)

    def _parse_args(self, *args, **kwargs):
        self.args = self.argument_parser.parse_args(*args)