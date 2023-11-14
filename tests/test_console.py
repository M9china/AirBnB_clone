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

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_all(self, mock_stdout):
        """
        Test for 'do_all' method with a valid class input.
        Expected output: String representation of all instances of the class.
        """
        with patch('models.storage.Storage.all') as mock_storage_all:
            mock_storage_all.return_value = {"BaseModel.123": "instance"}
            self.cmd.onecmd("all BaseModel")
            self.assertEqual(mock_stdout.getvalue().strip(), "instance")

    @patch('sys.stdout', new_callable=StringIO)
    def test_do_update(self, mock_stdout):
        """
        Test for 'do_update' method with a valid class,
        ID, attribute, and value input.
        Expected output: No output (should print nothing).
        """
        with patch('models.storage.Storage.all') as mock_storage_all:
            mock_storage_all.return_value = {"BaseModel.123": "instance"}
            with patch('models.storage.Storage.new') as mock_storage_new:
                with patch('models.storage.Storage.save') as mock_storage_save:
                    self.cmd.onecmd("update BaseModel 123 name 'NewName'")
                    mock_storage_new.assert_called_once()
                    mock_storage_save.assert_called_once()
                    self.assertEqual(mock_stdout.getvalue().strip(), "")

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_command(self, mock_stdout):
        """
        Test for 'default' method with a valid command.
        Expected output: Custom output based on the command.
        """
        with patch('models.storage.Storage.all') as mock_storage_all:
            mock_storage_all.return_value = {"BaseModel.123": "instance"}
            self.cmd.onecmd("show BaseModel 123")
            self.assertEqual(mock_stdout.getvalue().strip(), "instance")

    @patch('sys.stdout', new_callable=StringIO)
    def test_default_command_invalid(self, mock_stdout):
        """
        Test for 'default' method with an invalid command.
        Expected output: Error message.
        """
        self.cmd.onecmd("invalid_command")
        expected_output = "** NO COMMAND FOR invalid_command**"
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_do_count(self):
        """
        Test for 'do_count' method with a valid class input.
        Expected output: Number of instances of the class.
        """
        with patch('models.storage.Storage.all') as mock_storage_all:
            mock_storage_all.return_value = {"BaseModel.123": "instance"}
            with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                self.cmd.onecmd("count BaseModel")
                self.assertEqual(mock_stdout.getvalue().strip(), "1")

    def test_do_count_missing_class(self):
        """
        Test for 'do_count' method with a missing class input.
        Expected output: Error message.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("count")
            expected_output = "** Class name missing **"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_do_count_nonexistent_class(self):
        """
        Test for 'do_count' method with a non-existent class input.
        Expected output: Error message.
        """
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.onecmd("count NonExistentClass")
            expected_output = "** class doesn't exist **"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output)

    def test_emptyline(self):
        """
        Test for 'emptyline' method.
        Expected output: False.
        """
        self.assertFalse(self.cmd.emptyline())


if __name__ == '__main__':

    unittest.main()
