import os
from openai import OpenAI

def generate_ai_algorithm(prompt: str) -> str:
    """Sends the standardized English prompt to the LLM to generate code."""
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: OPENAI_API_KEY not found. Please add it to your .env file."
        
    client = OpenAI(api_key=api_key)
    
    system_prompt = (
        "You are an expert AI Algorithm Generator. You write highly efficient Python algorithms. "
        "CRITICAL REQUIREMENT: Always output the final code, variable names, and documentation "
        "strictly in English, regardless of the cultural context of the original request."
    )
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo", # You can upgrade to gpt-4 if you prefer
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"AI Engine Error: {e}"
      
