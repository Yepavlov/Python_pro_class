import unittest

from HW_20.formatted_name import formatted_name


class TestFormattedName(unittest.TestCase):

    def test_formatted_name_without_middle_name(self):
        self.assertEqual(formatted_name(first_name="Leonardo", last_name="Dicaprio"), "Leonardo Dicaprio")

    def test_formatted_name_with_middle_name(self):
        self.assertEqual(formatted_name(first_name="Roy",
                                        last_name="Jons",
                                        middle_name="Junior"), "Roy Junior Jons")

    def test_formatted_name_without_middle_name_lower_case(self):
        self.assertEqual(formatted_name(first_name="leonardo", last_name="dicaprio"), "Leonardo Dicaprio")

    def test_formatted_name_with_middle_name_lower_case(self):
        self.assertEqual(formatted_name(first_name="roy",
                                        last_name="jons",
                                        middle_name="junior"), "Roy Junior Jons")

    def test_formatted_name_with_spaces_from_both_sides(self):
        self.assertEqual(formatted_name(first_name="  Leonardo  ", last_name="  Dicaprio  "),
                         "  Leonardo     Dicaprio  ")

    def test_formatted_name_with_middle_name_with_spaces_from_both_sides(self):
        self.assertEqual(formatted_name(first_name=" Roy ",
                                        last_name=" Jons ",
                                        middle_name=" Junior "), " Roy   Junior   Jons ")

    def test_formatted_name_with_middle_name_with_spaces_from_both_sides_and_middle(self):
        self.assertEqual(formatted_name(first_name=" R o y ",
                                        last_name=" Jon s ",
                                        middle_name=" Ju ni or "), " R O Y   Ju Ni Or   Jon S ")

    def test_formatted_name_with_chars_in_str_in_the_beginning(self):
        self.assertEqual(formatted_name(first_name="///eonardo", last_name="///icaprio"), "///Eonardo ///Icaprio")

    def test_formatted_name_with_chars_in_str_from_both_sides(self):
        self.assertEqual(formatted_name(first_name="///eonardo@#",
                                        last_name="///icaprio$%",
                                        middle_name="///unior^&"), "///Eonardo@# ///Unior^& ///Icaprio$%")

    def test_formatted_name_with_chars_in_str_from_both_sides_and_middle(self):
        self.assertEqual(formatted_name(first_name="///eon-ardo@#",
                                        last_name="///ica-prio$%",
                                        middle_name="///un-ior^&"), "///Eon-Ardo@# ///Un-Ior^& ///Ica-Prio$%")

    def test_formatted_name_with_empty_string(self):
        self.assertEqual(formatted_name(first_name="",
                                        last_name="",
                                        middle_name=""), " ")

    def test_formatted_name_with_first_name_none(self):
        try:
            formatted_name(first_name=None, last_name="Jons", middle_name="Junior")
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_with_last_name_none(self):
        try:
            formatted_name(first_name="Roy", last_name=None, middle_name="Junior")
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_with_middle_name_none(self):
        try:
            formatted_name(first_name="Roy", last_name="Jons", middle_name=None)
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_without_first_name(self):
        try:
            formatted_name(last_name="Jons", middle_name="Junior")
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_without_last_name(self):
        try:
            formatted_name(first_name="Roy", middle_name="Junior")
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_with_first_name_integers(self):
        try:
            formatted_name(first_name=123, last_name="jons", middle_name="")
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_with_last_name_integers(self):
        try:
            formatted_name(first_name="roy", last_name=123, middle_name="")
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_with_middle_name_integers(self):
        try:
            formatted_name(first_name="roy", last_name="jons", middle_name=123)
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")

    def test_formatted_name_with_all_integers(self):
        try:
            formatted_name(first_name=123, last_name=456, middle_name=789)
        except TypeError:
            self.assertTrue(True)
        else:
            self.fail("Expected TypeError but no exception was raised")
