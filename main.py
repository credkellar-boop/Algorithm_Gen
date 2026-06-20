from generator.utils.translator import translate_to_english
from generator.core.router import route_prompt

def handle_request(user_prompt: str):
    # Step 1: Standardize input language to English
    english_prompt, original_lang = translate_to_english(user_prompt)
    
    # Step 2: Route the standardized English prompt
    decision = route_prompt(english_prompt)
    
    # Step 3: Proceed with generation or template execution...
  
