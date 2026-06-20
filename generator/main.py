from generator.utils.translator import translate_to_english
from generator.core.router import route_prompt
from generator.core.ai_engine import generate_ai_algorithm
from generator.templates.national_standards import get_standard_blueprint

def process_prompt(user_prompt: str) -> str:
    # 1. Translate input to English
    english_prompt, source_lang = translate_to_english(user_prompt)
    print(f"[System] Detected language: {source_lang}. Translated prompt: {english_prompt}")
    
    # 2. Decide if it's a strict standard or needs AI generation
    route_type, standard_name = route_prompt(english_prompt)
    
    # 3. Fetch template or generate via AI
    if route_type == "national_standard" and standard_name:
        print(f"[System] Routing to deterministic template: {standard_name}")
        return get_standard_blueprint(standard_name)
    else:
        print("[System] Routing to AI Engine...")
        return generate_ai_algorithm(english_prompt)
      
