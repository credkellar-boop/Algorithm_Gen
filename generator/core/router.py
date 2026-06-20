def route_prompt(prompt: str) -> tuple[str, str]:
    """
    Analyzes the prompt to decide if it uses a standard template or the AI engine.
    Returns a tuple: (route_type, standard_name_if_applicable)
    """
    prompt_lower = prompt.lower()
    
    # Dictionary of standard algorithms we have blueprints for
    standards = {
        "sm4": "SM4_China",
        "sm3": "SM3_China",
        "gost": "GOST_Russia",
        "aes": "AES_International",
        "rsa": "RSA_International"
    }
    
    # If the user asks for a specific strict standard, route to templates
    for key, name in standards.items():
        if key in prompt_lower:
            return "national_standard", name
            
    # Otherwise, let the AI write it from scratch
    return "ai_engine", ""
  
