from unittest import TestCase

from src.ci_cd.hello_world import HelloWorld


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        self.assertEqual(HelloWorld(name="Joao").say_hello(), "Hello Joao!")

    def test_hello_world2(self):
        self.assertEqual(HelloWorld(name="José").say_hello(), "Hello José!")

    def test_hello_world3(self):
        self.assertNotEqual(HelloWorld(name="José").say_hello(), "Hello José..?")

    def test_hello_world4(self):
        self.assertEqual(HelloWorld(name="José").say_bye(from_who="Andreia"), "Andreia said by to José.")
