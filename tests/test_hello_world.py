from unittest import TestCase

from ci_cd.hello_world import HelloWorld


class TestHelloWorld(TestCase):
    def test_hello_world(self):
        self.assertEqual(HelloWorld(name="Joao").say_hello(), "Hello Joao!")

    def test_hello_world2(self):
        self.assertEqual(HelloWorld(name="Joao").say_hello(), "Hello Joao!")
