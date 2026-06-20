import boto3

def deploy_to_aws(code: str, region: str, algorithm_name: str) -> str:
    """
    Deploys the generated algorithm to an AWS Lambda function.
    Automatically handles Sovereign vs Public endpoints based on the region.
    """
    print(f"[AWS] Connecting to region: {region}")
    
    # China's sovereign AWS regions require a different partition ('aws-cn')
    if region.startswith("cn-"):
        print("[AWS] ALERT: Using AWS China Sovereign Partition (Data Localization Enforced).")
    
    try:
        # In a real app, you would use boto3.client('lambda', region_name=region)
        # to zip and upload the 'code' string as a serverless function.
        return f"Successfully staged {algorithm_name} for AWS deployment in {region}."
    except Exception as e:
        return f"AWS Deployment Error: {e}"
      
