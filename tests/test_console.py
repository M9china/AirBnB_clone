import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """
    Test cases for the HBNBCommand class methods.
    """

    def setUp(self):
        """
        Set up a new HBNBCommand instance for each test method.
        """
        self.cmd = HBNBCommand()

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_create(self, mock_stdout):
        """
        Test for 'do_create' method with valid class input.
        Expected output: ID of the created instance
        """
        with patch('models.storage.Storage.new') as mock_storage_new:
            self.cmd.onecmd("create BaseModel")
            mock_storage_new.assert_called_once()
            self.assertTrue(len(mock_stdout.getvalue().strip()) > 0)

    def test_do_create_nonexistent_class(self):
        """
        Test for 'do_create' method with a non-existent class input.
        Expected output: '** class doesn't exist **'.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create NonExistentClass")
            self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    "** class doesn't exist **"
                    )

    def test_do_create_valid_class(self):
        """
        Test for 'do_create' method with a valid class input.
        Expected output: ID of the created instance.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("create BaseModel")
            output = mock_stdout.getvalue().strip()
            self.assertTrue(len(output) > 0)

    def test_do_quit(self):
        """
        Test for 'do_quit' method.
        Expected output: 'Left the HBNBCommand Shell'.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.cmd.do_quit(''))
            self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    "Left the HBNBCommand Shell"
                    )

    def test_do_EOF(self):
        """
        Test for 'do_EOF' method.
        Expected output: 'Left the HBNBCommand Shell'.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.assertTrue(self.cmd.do_EOF(''))
            self.assertEqual(
                    mock_stdout.getvalue().strip(),
                    "Left the HBNBCommand Shell"
                    )

    def test_emptyline(self):
        """
        Test for 'emptyline' method.
        Expected output: False.
        """
        self.assertFalse(self.cmd.emptyline())


if __name__ == '__main__':

    unittest.main()
