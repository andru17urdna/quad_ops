import subprocess

from utils.classes import BaseClass, Parser, Arg
from utils.wrappers import fetch_files

class run_file(BaseClass):
    
    @fetch_files("simple_file.txt", "second_file.txt")
    def execute(self, args, *_args, files, **kwargs):
        file_name = args.filename

        file = getattr(files, file_name)

        result = subprocess.run(["cat", file], capture_output=True, text=True)
        print(result.stdout)


    def attribute_error(self, err, args):
        print("funky error:", err, args)

    parser = Parser(description="A simple example script.")
    args=[
        Arg('filename', type=lambda file_name: file_name.replace(".","_"), help='The name of the file to process'),
        Arg('-v', '--verbose', action='store_true', help='Increase output verbosity'),
        Arg('-c', '--count', type=int, default=1, help='Number of times to process the file')
    ]