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

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_show(self, mock_stdout):
        """
        Test for 'do_show' method with a valid class and ID input.
        Expected output: String representation of the instance.
        """
        with patch('models.storage.Storage.all') as mock_storage_all:
            mock_storage_all.return_value = {"BaseModel.123": "instance"}
            self.cmd.onecmd("show BaseModel 123")
            self.assertEqual(mock_stdout.getvalue().strip(), "instance")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_destroy(self, mock_stdout):
        """
        Test for 'do_destroy' method with a valid class and ID input.
        Expected output: No output (should print nothing).
        """
        with patch('models.storage.Storage.all') as mock_storage_all:
            mock_storage_all.return_value = {"BaseModel.123": "instance"}
            with patch('models.storage.Storage.save') as mock_storage_save:
                self.cmd.onecmd("destroy BaseModel 123")
                mock_storage_save.assert_called_once()
                self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_emptyline(self):
        """
        Test for 'emptyline' method.
        Expected output: False.
        """
        self.assertFalse(self.cmd.emptyline())


if __name__ == '__main__':

    unittest.main()
