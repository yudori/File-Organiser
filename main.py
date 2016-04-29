import argparse
import os

from config import *


class Organizer:

    def __init__(self, directory):
        self.set_dir(directory)

    def set_dir(self, directory):
        self.directory = directory

    def sort(self):
        files = [os.path.join(self.directory, f) for f in os.listdir(self.directory)
                 if os.path.isfile(os.path.join(self.directory, f))]
        for file in files:
            name, ext = os.path.splitext(file)
            folder = self.assign_folder(ext)
            new_dir = os.path.join(self.directory, folder)
            if not os.path.exists(new_dir):
                os.makedirs(new_dir)
            os.rename(file, os.path.join(new_dir, os.path.basename(file)))

    def assign_folder(self, extension):
        for key, value in mappings.iteritems():
            if extension[1:] in value:
                return key
        return "Other"


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Organizes files in a directory by grouping them into folders based on filetype')
    parser.add_argument("directory", help="The directory to be organized")
    args = parser.parse_args()
    print "Organizing files in %s ..."%args.directory
    st = Organizer(args.directory)
    st.sort()
    print "Done."
