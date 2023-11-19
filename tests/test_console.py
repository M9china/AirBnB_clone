import sys
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage
from models.basemodel import BaseModel


class TestConsole(unittest.TestCase):

    def setUp(self):
        self.stdout_patch = patch('sys.stdout', new_callable=StringIO)
        self.mock_stdout = self.stdout_patch.start()

    def tearDown(self):
        self.stdout_patch.stop()

    def test_create_command(self):
        with patch('builtins.input',
                   return_value="create BaseModel") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("create BaseModel")
            self.assertIn("{}".format(
                storage.new.call_args[0][0].id),
                self.mock_stdout.getvalue().strip())

    def test_show_command(self):
        with patch('builtins.input',
                   return_value="show BaseModel") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("show BaseModel")
            self.assertIn("** instance id missing **",
                          self.mock_stdout.getvalue().strip())

        with patch('builtins.input', return_value="show BaseModel {}".format(
                storage.new(BaseModel()).id)) as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("show BaseModel {}".format(
                storage.new.call_args[0][0].id))
            self.assertIn(str(
                storage.new.call_args[0][0]),
                self.mock_stdout.getvalue().strip())

    def test_destroy_command(self):
        with patch('builtins.input',
                   return_value="destroy BaseModel") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("destroy BaseModel")
            self.assertIn("** instance id missing **",
                          self.mock_stdout.getvalue().strip())

        instance_id = storage.new(BaseModel()).id
        with patch('builtins.input',
                   return_value="destroy BaseModel {}".format(
                instance_id)) as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("destroy BaseModel {}".format(
                instance_id))
            self.assertNotIn(instance_id, storage.all())

    def test_all_command(self):
        with patch('builtins.input', return_value="all") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("all")
            self.assertIn("BaseModel",
                          self.mock_stdout.getvalue().strip())

        with patch('builtins.input',
                   return_value="all BaseModel") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("all BaseModel")
            self.assertIn("BaseModel",
                          self.mock_stdout.getvalue().strip())

    def test_update_command(self):
        with patch('builtins.input',
                   return_value="update BaseModel") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("update BaseModel")
            self.assertIn("** instance id missing **",
                          self.mock_stdout.getvalue().strip())

        instance_id = storage.new(BaseModel()).id
        with patch('builtins.input',
                   return_value="update BaseModel {}".format(instance_id)) as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with(
                "update BaseModel {}".format(instance_id))
            self.assertIn("** attribute name missing **",
                          self.mock_stdout.getvalue().strip())

        with patch('builtins.input',
                   return_value="update BaseModel {} name".format(instance_id)) as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with(
                "update BaseModel {} name".format(instance_id))
            self.assertIn("** value missing **",
                          self.mock_stdout.getvalue().strip())

        with patch('builtins.input',
                   return_value="update BaseModel {} name 'NewName'".format(instance_id)) as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with(
                "update BaseModel {} name 'NewName'".format(instance_id))
            self.assertEqual(storage.new.call_args[0][0].name, "NewName")

    def test_count_command(self):
        with patch('builtins.input', return_value="count BaseModel") as mock_input:
            HBNBCommand().cmdloop()
            mock_input.assert_called_with("count BaseModel")
            self.assertIn("1", self.mock_stdout.getvalue().strip())

    def test_quit_command(self):
        with patch('builtins.input', return_value="quit") as mock_input:
            with self.assertRaises(SystemExit):
                HBNBCommand().cmdloop()

    def test_EOF_command(self):
        with patch('builtins.input', return_value="EOF") as mock_input:
            with self.assertRaises(SystemExit):
                HBNBCommand().cmdloop()


if __name__ == '__main__':
    unittest.main()
