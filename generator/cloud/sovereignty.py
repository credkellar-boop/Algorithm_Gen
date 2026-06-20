def get_compliant_cloud_region(algorithm_standard: str) -> dict:
    """
    Maps national algorithm standards to legally compliant Sovereign Cloud regions.
    """
    localization_rules = {
        "SM4_China": {
            "aws_region": "cn-northwest-1", # AWS Ningxia (operated by NWCD)
            "gcp_region": "asia-east2",     # GCP (Hong Kong/Taiwan local partners)
            "sovereignty_level": "Strict Data Localization"
        },
        "GOST_Russia": {
            "aws_region": "restricted_use_local_provider", # Foreign hyperscalers are restricted
            "gcp_region": "restricted_use_local_provider",
            "sovereignty_level": "Strict National Isolation"
        },
        "AES_International": {
            "aws_region": "us-east-1",      # Global Standard Public Cloud
            "gcp_region": "us-central1",
            "sovereignty_level": "International Public Cloud"
        }
    }
    
    return localization_rules.get(
        algorithm_standard, 
        {"aws_region": "eu-central-1", "sovereignty_level": "Default / GDPR Compliant"}
    )
  
