#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Andy Sayler
# Summer 2014
# CSCI 3308
# Univerity of Colorado
# Text Processing Module

'''
Add the following tests to the textproc_test.py file:

    x Write a test to verify the constructor raises an error if passed something other than a string
    x Write one or more unit tests to test the count() method
    x Write one or more unit tests to test the count_alpha() method
    x Write one or more unit tests to test the count_numeric() method
    x Write one or more unit tests to test the count_vowels() method
    x Write one or more unit tests to test the is_phonenumber() method
    x Find and correct any bugs the tests turn up

Credit: turn in a zip file with your code.
'''

import unittest
import textproc

class TextprocTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_init(self):
        text = "tesing123"
        p = textproc.Processor(text)
        self.assertEqual(p.text, text, "'text' does not match input")

    def test_Processor_constructor(self):
        number = 50130
        with self.assertRaises(textproc.TextProcError) as cm:
            textproc.Processor(number)
        the_exception = cm.exception
        self.assertEqual(the_exception.error_message, 'Processors require strings')

    def test_count(self):
        text = "Aardvark"
        text_obj = textproc.Processor(text)
        length = textproc.Processor.count(text_obj)
        self.assertEqual(length, 8, "Count failed") # Aardvark is eight long

        text = "Count number of characters in text. :return: Length"
        text_obj = textproc.Processor(text)
        length = textproc.Processor.count(text_obj)
        self.assertEqual(length, len(text))

    def test_count_alpha(self):
        text = "aardvarks"
        text_obj = textproc.Processor(text)
        num_a = textproc.Processor.count_alpha(text_obj)
        self.assertEqual(num_a, 9)

        text = "Aardvarks Kill."
        text_obj = textproc.Processor(text)
        num_a = textproc.Processor.count_alpha(text_obj)
        self.assertEqual(num_a, len("Aardvarks")+len("Kill"), "'Aardvarks Kill' has 9+4=13 alpha characters")

        # no alpha case
        text = "3210987678"
        text_obj = textproc.Processor(text)
        num_a = textproc.Processor.count_alpha(text_obj)
        self.assertEqual(num_a, 0)   

    def test_count_numeric(self):
        # no numeric case
        text = "Aardvarks Love."
        text_obj = textproc.Processor(text)
        num_a = textproc.Processor.count_numeric(text_obj)
        self.assertEqual(num_a, 0)

        # all numeric case
        text = "3210987678" # count_numeric does not count 0!
        text_obj = textproc.Processor(text)
        num_nums = textproc.Processor.count_numeric(text_obj)
        self.assertEqual(num_nums, len(text))

        # part numeric case
        text = "Aardvarks Want 50130." # 5 0 1 3 0 = five numbers
        text_obj = textproc.Processor(text)
        num_nums = textproc.Processor.count_numeric(text_obj)
        self.assertEqual(num_nums, 5)

    def test_count_vowels(self):
        # no vowels case
        text = "rdvrks 50130."
        text_obj = textproc.Processor(text)
        num_a = textproc.Processor.count_vowels(text_obj)
        self.assertEqual(num_a, 0)

        # Mixed vowel case
        text = "Aardvarks Like You." # should have 7 vowels
        text_obj = textproc.Processor(text)
        num_a = textproc.Processor.count_vowels(text_obj)
        # manual count of vowels
        vowels = "AaEeIiOoUu"
        num_vowels = 0
        for char in text:
            if char in vowels:
                num_vowels+=1
        # fails by not counting i
        self.assertEqual(num_a, num_vowels)

    def test_is_phonenumber(self):
        # no phonenumber case
        text = "Aardvarks Love."
        text_obj = textproc.Processor(text)
        is_num = textproc.Processor.is_phonenumber(text_obj)
        self.assertFalse(is_num)

        # phonenumber case
        text = "987-456-3212"
        text_obj = textproc.Processor(text)
        is_num = textproc.Processor.is_phonenumber(text_obj)
        self.assertTrue(is_num)

        # phonenumber with zeros and . case
        text = "900.450.3012"
        text_obj = textproc.Processor(text)
        is_num = textproc.Processor.is_phonenumber(text_obj)
        self.assertTrue(is_num)

        # phonenumber no dashes or dots
        text = "9991118888"
        text_obj = textproc.Processor(text)
        is_num = textproc.Processor.is_phonenumber(text_obj)
        self.assertTrue(is_num)

        # phonenumber not long enough
        text = "999111888"
        text_obj = textproc.Processor(text)
        is_num = textproc.Processor.is_phonenumber(text_obj)
        self.assertFalse(is_num)
        


# Main: Run Test Cases
if __name__ == '__main__':
    unittest.main()
