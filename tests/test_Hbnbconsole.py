#this is the main the main test file for the console project By Jan Yaya Mutewera

#!/usr/bin/python3
""" Test Console for AirBnB """
import cmd
import sys
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(TestCase):
    """ Test class for the console """

    def setUp(self):
        """ Redirect stdout for testing"""
        self.console_out = StringIO()
        sys.stdout = self.console_out

    def tearDown(self):
        """ Reset redirect """
        sys.stdout = sys.__stdout__

    def test_create(self):
        """ Test create command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("create BaseModel")
            self.assertTrue(len(fake_out.getvalue()) > 0)

    def test_show(self):
        """ Test show command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("show BaseModel 1234-1234-1234")
            self.assertEqual(fake_out.getvalue(), "** no instance found **\n")

    def test_destroy(self):
        """ Test destroy command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("destroy BaseModel 1234-1234-1234")
            self.assertEqual(fake_out.getvalue(), "** no instance found **\n")

    def test_all(self):
        """ Test all command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("all")
            self.assertTrue(len(fake_out.getvalue()) > 0)

    def test_update(self):
        """ Test update command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("update BaseModel 1234-1234-1234")
            self.assertEqual(fake_out.getvalue(), "** no instance found **\n")

    def test_quit(self):
        """ Test quit command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("quit")
            self.assertEqual(fake_out.getvalue(), "")

    def test_EOF(self):
        """ Test EOF command """
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(fake_out.getvalue(), "")

