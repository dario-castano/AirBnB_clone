import unittest
import os
import uuid
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand
from models.engine.file_storage import FileStorage


class TestConsole(unittest.TestCase):
    """
    Test cases for the console
    """
    jsfile_test = 'consoletest.json'
    err = {'CLS_MISS': "** class name missing **",
           'CLS_NOEX': "** class doesn't exist **",
           'ID_MISS': "** instance id missing **",
           'ID_NOEX': "** no instance found **",
           'NO_ATTR': "** attribute name missing **",
           'NO_VAL': "** value missing **"}
    cls_list = ['BaseModel',
                'Amenity',
                'City',
                'Place',
                'Review',
                'State',
                'User']

    @classmethod
    def setUpClass(cls):
        FileStorage._FileStorage__file_path = TestConsole.jsfile_test

    def tearDown(self):
        if os.path.isfile(TestConsole.jsfile_test):
            os.remove(TestConsole.jsfile_test)

    def test_help_works(self):
        """
        Create should show the right info
        """
        h_title = "Documented commands (type help <topic>):"
        h_sep = "========================================"
        h_menu = "EOF  all  count  create  destroy  help  quit  show  update"
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("help")
        outstr = f.getvalue()
        self.assertIn(h_title, outstr)
        self.assertIn(h_sep, outstr)
        self.assertIn(h_menu, outstr)

    def test_create_missing_class(self):
        """
        Create should fail if no class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_MISS'] + '\n')

    def test_create_wrong_class(self):
        """
        Create should fail if the wrong class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("create YoMAMA")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("YoMAMA.create()")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

    def test_create_saves_json(self):
        """
        Create makes a JSON file if doesnt exists
        """
        pass

    def test_create_ok_params(self):
        """
        Create works with correct parameters
        """
        pass

    def test_create_has_help(self):
        """
        Create has documented help
        """
        pass

    def test_show_missing_class(self):
        """
        Show should fail if no class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_MISS'] + '\n')

    def test_show_missing_id(self):
        """
        Show should fail if no id are typed
        """
        for cls_elem in TestConsole.cls_list:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {}".format(cls_elem))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_MISS'] + '\n')

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.show()".format(cls_elem))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_MISS'] + '\n')

    def test_show_wrong_class(self):
        """
        Show should fail if the wrong class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("show YoMAMA")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("YoMAMA.show()")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

    def test_show_wrong_id(self):
        """
        Show should fail if the wrong id are typed
        """
        for cls_elem in TestConsole.cls_list:
            fake_id = uuid.uuid4()
            HBNBCommand().onecmd("create {}".format(cls_elem))

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("show {} {}".format(cls_elem, fake_id))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_NOEX'] + '\n')

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.show({})".format(cls_elem, fake_id))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_NOEX'] + '\n')

    def test_show_ok_params(self):
        """
        Show works with correct parameters
        """
        pass

    def test_show_has_help(self):
        """
        Show has documented help
        """
        pass

    def test_destroy_missing_class(self):
        """
        destroy should fail if no class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_MISS'] + '\n')

    def test_destroy_missing_id(self):
        """
        destroy should fail if no id are typed
        """
        for cls_elem in TestConsole.cls_list:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {}".format(cls_elem))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_MISS'] + '\n')

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.destroy()".format(cls_elem))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_MISS'] + '\n')

    def test_destroy_wrong_class(self):
        """
        destroy should fail if the wrong class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("destroy YoMAMA")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("YoMAMA.destroy()")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

    def test_destroy_wrong_id(self):
        """
        destroy should fail if the wrong id are typed
        """
        for cls_elem in TestConsole.cls_list:
            fake_id = uuid.uuid4()
            HBNBCommand().onecmd("create {}".format(cls_elem))

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("destroy {} {}".format(cls_elem, fake_id))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_NOEX'] + '\n')

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.destroy({})".format(cls_elem, fake_id))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_NOEX'] + '\n')

    def test_destroy_ok_params(self):
        """
        destroy works with correct parameters
        """
        pass

    def test_destroy_has_help(self):
        """
        destroy has documented help
        """
        pass

    def test_all_wrong_class(self):
        """
        all should fail if the wrong class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("all YoMAMA")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("YoMAMA.all()")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

    def test_all_ok_params(self):
        """
        all works with correct parameters
        """
        pass

    def test_all_has_help(self):
        """
        all has documented help
        """
        pass

    def test_update_missing_class(self):
        """
        update should fail if no class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_MISS'] + '\n')

    def test_update_missing_id(self):
        """
        update should fail if no id are typed
        """
        for cls_elem in TestConsole.cls_list:
            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {}".format(cls_elem))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_MISS'] + '\n')

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.update()".format(cls_elem))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_MISS'] + '\n')

    def test_update_wrong_class(self):
        """
        update should fail if the wrong class are typed
        """
        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("update YoMAMA")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

        with patch('sys.stdout', new=StringIO()) as f:
            HBNBCommand().onecmd("YoMAMA.update()")
        outstr = f.getvalue()
        self.assertEqual(outstr, TestConsole.err['CLS_NOEX'] + '\n')

    def test_update_wrong_id(self):
        """
        update should fail if the wrong id are typed
        """
        for cls_elem in TestConsole.cls_list:
            fake_id = uuid.uuid4()
            HBNBCommand().onecmd("create {}".format(cls_elem))

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("update {} {}".format(cls_elem, fake_id))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_NOEX'] + '\n')

            with patch('sys.stdout', new=StringIO()) as f:
                HBNBCommand().onecmd("{}.update({})".format(cls_elem, fake_id))
            outstr = f.getvalue()
            self.assertEqual(outstr, TestConsole.err['ID_NOEX'] + '\n')

    def test_update_ok_params(self):
        """
        update works with correct parameters
        """
        pass

    def test_update_has_help(self):
        """
        update has documented help
        """
        pass
