import unittest
from generator.utils.translator import translate_to_english
from generator.core.router import route_prompt
from generator.utils.optimizer import clean_generated_code

class TestAlgorithmGenCore(unittest.TestCase):

    def test_translation_layer(self):
        # Basic validation that processing string returns expected tuple format
        text, lang = translate_to_english("Hola Mundo")
        self.assertIsNotNone(text)
        self.assertIsNotNone(lang)

    def test_routing_logic(self):
        # Confirm that keyword tracking accurately intercepts structural ciphers
        route, target = route_prompt("Generate an implementation of SM4 encryption")
        self.assertEqual(route, "national_standard")
        self.assertEqual(target, "SM4_China")

    def test_code_optimizer(self):
        # Confirm that markdown delimiters are stripped correctly
        raw_markdown = "Here is your code:\n
http://googleusercontent.com/immersive_entry_chip/0
