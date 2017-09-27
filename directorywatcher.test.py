"""
Module
"""
import unittest
import os
from directorywatcher import DirectoryWatcher


class DirectoryWatcherTests(unittest.TestCase):
    def __init__(self, methodName='runTest'):
        super(DirectoryWatcherTests, self).__init__(methodName)
        self.dir_watcher = DirectoryWatcher(os.path.join(os.path.dirname(os.path.realpath(__file__)), "newsletters"))

    def test_html_data_return_null_if_no_data_is_sent(self):
        self.assertIsNone(self.dir_watcher.html_data(None))
        
    def test_html_data_return_null_if_empty_data_is_sent(self):
        self.assertIsNone(self.dir_watcher.html_data([]))
        
    def test_writing_to_file_when_file_exist(self):
        file_name = "testfile.txt"
        data = "I am a man"
        self.dir_watcher.write_file(data, file_name)
        data2 = ""
        with open(file_name, 'r') as x_file:
            data2 = x_file.read()
        self.assertEqual(data, data2)

    def test_writing_to_file_when_file_does_not_exist(self):
        file_name = "madison.txt"
        data = "I am a new man"
        self.dir_watcher.write_file(data, file_name)
        data2 = ""
        with open(file_name, 'r') as x_file:
            data2 = x_file.read()
        self.assertEqual(data, data2)

if __name__ == '__main__':
    unittest.main()
