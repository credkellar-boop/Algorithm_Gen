def get_compliant_cloud_region(algorithm_standard: str) -> dict:
    """
    Maps national and international standards to corresponding cloud environments 
    to ensure local sovereignty compliance.
    """
    compliance_matrix = {
        "SM4_China": {
            "aws_region": "cn-northwest-1",
            "gcp_region": "asia-east2",
            "sovereignty_level": "Strict Sovereignty (China Cybersecurity Law Enforced)"
        },
        "GOST_Russia": {
            "aws_region": "restricted",
            "gcp_region": "restricted",
            "sovereignty_level": "Air-Gapped / Isolated National Infrastructure"
        },
        "AES_International": {
            "aws_region": "us-east-1",
            "gcp_region": "us-central1",
            "sovereignty_level": "Standard Global Public Cloud"
        }
    }
    
    return compliance_matrix.get(
        algorithm_standard, 
        {"aws_region": "us-east-1", "gcp_region": "us-central1", "sovereignty_level": "General"}
    )
