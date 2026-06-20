from generator.utils.translator import translate_to_english
from generator.core.router import route_prompt

def handle_request(user_prompt: str):
    # Step 1: Standardize input language to English
    english_prompt, original_lang = translate_to_english(user_prompt)
    
    # Step 2: Route the standardized English prompt
    decision = route_prompt(english_prompt)
    
    # Step 3: Proceed with generation or template execution...
  
# Snippet to add to the end of your generator/main.py

from generator.cloud.sovereignty import get_compliant_cloud_region

# ... after the algorithm string is generated ...

if route_type == "national_standard":
    compliance_info = get_compliant_cloud_region(standard_name)
    print(f"\n[Compliance Notice] Sovereignty Level: {compliance_info['sovereignty_level']}")
    print(f"Recommended AWS Region: {compliance_info['aws_region']}")
    print(f"Recommended GCP Region: {compliance_info['gcp_region']}")
