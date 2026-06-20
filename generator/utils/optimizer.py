import re

def clean_generated_code(raw_ai_output: str) -> str:
    """
    Extracts raw Python code blocks from AI markdown responses 
    and sanitizes formatting.
    """
    # Regex to find text between ```python and ```
    code_block_match = re.search(r"```python\s*(.*?)\s*```", raw_ai_output, re.DOTALL | re.IGNORECASE)
    
    if code_block_match:
        extracted_code = code_block_match.group(1)
    else:
        # Fallback if AI didn't use markdown blocks but just returned text
        extracted_code = raw_ai_output.strip()
        
    # Remove any stray leading/trailing whitespace or empty lines
    cleaned_code = "\n".join([line for line in extracted_code.splitlines() if line.strip() != ""])
    
    return cleaned_code
  
