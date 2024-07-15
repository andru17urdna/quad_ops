import os
import sys

class Files:

    def __init__(self, file_path) -> None:
        self._file_path = file_path
        self._folder_files = self.list_files_in_folder()

    def list_files_in_folder(self):
        # Get the list of all files and directories in the specified directory
        files = os.listdir(self._file_path)
        
        # Filter out directories, keeping only files
        file_names = [f for f in files if os.path.isfile(os.path.join(self._file_path, f))]
        
        return file_names


    def _set_file(self, file_name: str):
        self._validate_file(file_name)

        scored_file_name = file_name.replace(".", "_")
        setattr(self, scored_file_name, f"{self._file_path}{file_name}")

    def _validate_file(self, file_name):

        def validate_file_exists():
            return file_name in self._folder_files

        def validate_file_is_file():
            return os.path.isfile(f"{self._file_path}{file_name}")

        validations = [
            validate_file_exists,
            validate_file_is_file,
        ]

        for validation in validations:
            if not validation():
                sys.exit("Exiting due to validation failure.")
    



def fetch_files( *files, **kwargs):
    return_kwargs = {}

    def decorator(func):
        corrected_file_path = sys.argv[0].replace("::","")
        file_path = f"{corrected_file_path}files/{func.__module__}/" 
        files_klass = Files(file_path)

        for file_name in files:
            files_klass._set_file(file_name)
            return_kwargs.update({"files": files_klass})

        def wrapper(*args, **kwargs):
            return func(*args, **{**kwargs, **return_kwargs})
        
        return wrapper
    return decorator