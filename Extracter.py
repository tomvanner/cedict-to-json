import os
from urllib.request import urlopen
from zipfile import ZipFile
from shutil import rmtree

class Extracter:
    """A class representing a file extracter

    Attributes:
    download_url (string): The url containing the source zip file
    extract_dir (string): The directory to extract the file contents to
    file_names (list): A list containing names of all the files extracted
    tmp_dir (string): The directory where the downloaded zip file will be stored
    tmp_file_name (string): The name of the temporary zip file

    """
    def __init__(self, download_url, extract_dir='data'):
        """Initialiser

        Parameters:
        download_url (string): The url containing the source zip file

        """
        self.download_url = download_url
        self.extract_dir = extract_dir
        self.file_names = None
        self.tmp_dir = os.path.join(os.path.dirname(__file__), 'temp')
        self.tmp_file_name = 'data.zip'

    def run(self):
        """Runs the extracter

        """
        # Get zip file from source
        zip_file = urlopen(self.download_url)

        # Create the zip file and extract it
        self.make_tmp_file(zip_file)       
        self.extract()
        self.remove_tmp()

        if len(self.file_names) != 1:
            return None

        return os.path.join(self.extract_dir, self.file_names[0])

    def extract(self):
        """Extract the contents of the downloaded zip file

        """
        with ZipFile(os.path.join(self.tmp_dir, self.tmp_file_name), 'r') as tmp_zip:
            tmp_zip.extractall(self.extract_dir)
            self.file_names = tmp_zip.namelist()

    def make_tmp_file(self, contents):
        """Makes a temporary zip.

        Parameters:
        contents : The contents to put into the temporary zip file.

        """
        # Make the temporary directory
        os.makedirs(self.tmp_dir, exist_ok=True)
        tmp_file = os.path.join(self.tmp_dir, self.tmp_file_name)

        # Create the file with the contents
        with open(tmp_file, "wb") as tmp:
            tmp.write(contents.read())

    def remove_tmp(self):
        """Removes the temporary directory, if it exists.

        """
        rmtree(self.tmp_dir)




