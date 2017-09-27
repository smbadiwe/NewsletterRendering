"""
Module
"""
import os
import time
from datetime import datetime


class DirectoryWatcher:
    """
    Watching for additions or removal of files from the directory, dirToWatch
    """

    def __init__(self, dirToWatch, wait_time_in_secs=10):
        self.wait_time = wait_time_in_secs
        if not dirToWatch:
            dirToWatch = os.path.dirname(os.path.realpath(__file__))
        self.path_to_watch = dirToWatch  # the folder being watched
        print("Initializing...")
        print("path_to_watch = " + dirToWatch)
        print("wait_time_in_secs = %d" % wait_time_in_secs)

    def html_data(self, list_of_files):
        """
        this function return html string to be saved to file.
        """
        if list_of_files:
            html = '<!DOCTYPE html>\n<html lang="en-US">\n<title>CEC - Newsletter Archive</title>\n'
            html += '<!--#include virtual="/etc/start_of_file.shtml" -->\n'
            html += '<!--#include virtual="/etc/trees_splash.shtml" -->\n'
            html += '<h1>Newsletter Archive</h1>\n'
            for file in list_of_files:
                date_str = file[:8]
                # for formatting, see http://strftime.org
                date_format = datetime.strptime(date_str, '%Y%m%d').strftime('%A, %B %d, %Y')
                print("file = " + file + " date_str = " + date_str + " date_format = " + date_format)
                html += '<p><a href="/newsletter/archive/' + file + '">' + date_format + '</a></p>\n'

            html += '<!--#include virtual="/etc/end_of_file.shtml" -->'
            return html
        return None

    def write_file(self, data, file_name):
        """
        this function write data to file
        """
        with open(file_name, 'w+') as x_file:
            x_file.write(data)

    def watch(self):
        """
        this function watches the specified folder
        """
        file_name = "newsletters.html"
        before = [f for f in os.listdir(self.path_to_watch) if f.endswith(".pdf")]
        while 1:
            time.sleep(self.wait_time)
            print(str(datetime.now()) + ": Checking directory for additions or removals...")
            after = [f for f in os.listdir(self.path_to_watch) if f.endswith(".pdf")]
            added = [f for f in after if not f in before and f.endswith(".pdf")]
            removed = [f for f in before if not f in after and f.endswith(".pdf")]
            if added or removed:
                data = self.html_data(after)
                self.write_file(data, file_name)
                before = after


if __name__ == '__main__':
    watcher = DirectoryWatcher(os.path.join(os.path.dirname(os.path.realpath(__file__)), "newsletters"))
    watcher.watch()
