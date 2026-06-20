import unittest
from generator.utils.translator import translate_to_english
from generator.core.router import route_prompt
from generator.utils.optimizer import clean_generated_code

class TestAlgorithmGenCore(unittest.TestCase):

    def test_translation_layer(self):
        text, lang = translate_to_english("Hola Mundo")
        self.assertIsNotNone(text)
        self.assertIsNotNone(lang)

    def test_routing_logic(self):
        route, target = route_prompt("Generate an implementation of SM4 encryption")
        self.assertEqual(route, "national_standard")
        self.assertEqual(target, "SM4_China")

    def test_code_optimizer(self):
        # We use a single-line string with newline characters (\n) 
        # to avoid all indentation/triple-quote issues.

        
        raw_markdown = "Here is your code:\nhttp://googleusercontent.com/immersive_entry_chip/0"

