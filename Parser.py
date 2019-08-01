import re

class Parser:
    """A class representing a parser for cedict

    Attributes:
    file_dir (string): Directory of the cedict data file.
    entries (dict): A dictonary containing key value pairs for every word.

    """
    def __init__(self, file_dir):
        """Initialiser

        Parameters:
        file_dir (string): Directory of the cedict data file.
        """
        self.file_dir = file_dir
        self.entries = {}

    def add_entry(self, entry):
        """Adds an entry to the dictonary, with the simplified character(s) as the key

        Parameters:
        entry (dict): The entry as a dictonary, containing key value pairs for:
            Simplified character(s)
            Traditional character(s)
            Pinyin character(s)
            Entry definition
        """
        self.entries[entry['simplified']] = entry

    def parse(self):
        """Reads the cedict and processes its contents, formatting and stroing each entry

        Returns:
        entries: A dictonary containing all of the cedict entires.
        """
        with open(self.file_dir, 'r', encoding='utf8') as cedict:
            lines = cedict.readlines()
            for line in lines:
                # Discard any file meta data
                if line.strip()[0] == '#':
                    continue

                entry = self.process_line(line)
                self.add_entry(entry)
                
        return self.entries
    
    def process_line(self, line):
        """Processes the cedict line by line

        Parameters:
        line (string): A line entry
        """
        # Lines should be in format: Traditional Simplified [pin1 yin1] /English equivalent 1/equivalent 2/
        # E.g. 中國 中国 [Zhong1 guo2] /China/Middle Kingdom/
        filtered_line = line.strip().strip('\t').strip('\n').strip('\r')    
        elements = re.split(r'(.+) (.+) \[(.+)\] /(.*)/', filtered_line)
        elements = list(filter(None, elements))

        # There should be 4 parts to each entry (see above)
        if len(elements) < 4:
            return

        # Separates multiple definitions into a list
        elements[-1] = elements[-1].split('/')

        return dict(zip(['traditional', 'simplified', 'pinyin', 'def'], elements))