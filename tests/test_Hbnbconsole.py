#this is the main the main test file for the console project By Jan Yaya Mutewera

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand

class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_EOF(self, mock_stdout):
        console = HBNBcommand()
        self.assertTrue(console.do_EOF(''))


    @patch('sys.stdout', new_callable=StringIO)
    def test_do_quit(self, mock_stdout):
        console = HBNBCommand()
        self.assertTrue(console.do_quit(''))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        console = HBNBCommand()
        console.emptyline()
        self.assertEqual(mock_stdout.getvalue(), '')

    @patch('sys.stdout' new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        console = HBNBCommand()
        with patch('sys.stdin', StringIO('BaseModel\nexit\n')):
            console.cmdloop()
        self.assertTrue(mock_stdout.getvalue().startswith('(hbnb) '))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_clear(self, mock_stdout):
        console = HBNBCommand()
        with patch('sys.stdin', StringIO('BaseModel\nexit\n')):
            console = cmdloop()
        self.assertTrue(mock_stdout.getvalue().startswith('(hbnb) '))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        console = HNBNCommand()
        with patch('sys.stdin', StringIO('BaseModel\nextit\n')):
            console.cmdloop()
        self.assertTrue(mock_stdout.getvalue().startswith('(hbnb) '))

    @patc('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        console = HBNBCommand()
        with patch('sys.stdin', StringIO('BaseModel\nexit\n')):
            console.cmdloop()
        self.assertTrue(mock_stdout.getvalue().startswith('(hbnb) '))

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        console = HBNBCommand()
        with patch('sys.stdin', StringIO('BaseModel\nexit\n')):
            console.cmdloop()
        self.assertTrue(mock_stdout.getvalue().startswith('(hbnb) '))

        if __name__ '__main__':
            unittest.main()
