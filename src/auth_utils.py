"""
AWS Bedrock Authentication Utilities

This module provides reusable authentication functions for Strands notebooks,
supporting both the new AWS Bedrock API keys and traditional AWS authentication methods.
"""

import boto3
import os
from typing import Dict, Any, Optional


class AuthStatus:
    """
    Authentication status class that provides clean access to authentication details.
    
    This class replaces the previous dictionary-based approach with a more Pythonic
    object-oriented interface while maintaining backward compatibility.
    """
    
    def __init__(self, method: str, detail: str, success: bool, 
                 region: str, profile: Optional[str] = None, message: str = ""):
        self.method = method
        self.detail = detail
        self.success = success
        self.region = region
        self.profile = profile
        self.message = message
    
    def __str__(self) -> str:
        """Human-readable string representation."""
        return f"AuthStatus(method={self.method}, region={self.region}, success={self.success})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return (f"AuthStatus(method='{self.method}', detail='{self.detail}', "
                f"success={self.success}, region='{self.region}', "
                f"profile={self.profile}, message='{self.message}')")
    
    def __getitem__(self, key: str):
        """Dictionary-style access for backward compatibility."""
        return getattr(self, key)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for backward compatibility."""
        return {
            'method': self.method,
            'detail': self.detail,
            'success': self.success,
            'region': self.region,
            'profile': self.profile,
            'message': self.message
        }
    
    @property
    def is_api_key(self) -> bool:
        """Convenience property to check if using API key authentication."""
        return self.method == "API Key"
    
    @property
    def is_aws_profile(self) -> bool:
        """Convenience property to check if using AWS profile authentication."""
        return self.method == "AWS Profile"
    
    @property
    def is_successful(self) -> bool:
        """Convenience property to check authentication success."""
        return self.success


def setup_bedrock_auth(
    api_key: str = "",
    region_name: str = "us-west-2",
    aws_profile: str = "default"
) -> AuthStatus:
    """
    Set up AWS Bedrock authentication using API keys or traditional AWS credentials.
    
    Args:
        api_key: AWS Bedrock API key (optional)
        region_name: AWS region to use
        aws_profile: AWS profile name for traditional authentication
        
    Returns:
        AuthStatus object with authentication details and methods for easy access
    """
    
    # Smart authentication detection
    if api_key and api_key.strip():
        return _setup_api_key_auth(api_key.strip(), region_name)
    else:
        return _setup_aws_profile_auth(region_name, aws_profile)


def _setup_api_key_auth(api_key: str, region_name: str) -> AuthStatus:
    """Set up API key authentication."""
    
    # Set the environment variable for API key authentication
    os.environ['AWS_BEARER_TOKEN_BEDROCK'] = api_key
    
    print("🔑 Using AWS Bedrock API Key authentication")
    print("   ✨ This is the easiest way to get started!")
    
    # Basic API key validation
    if len(api_key) < 20:
        print("⚠️  Warning: Your API key seems too short. Please verify it's correct.")
        print("   API keys are typically much longer than 20 characters.")
        
    return AuthStatus(
        method='API Key',
        detail='API Key authentication',
        success=True,
        region=region_name,
        profile=None,
        message='API Key authentication configured successfully'
    )


def _setup_aws_profile_auth(region_name: str, aws_profile: str) -> AuthStatus:
    """Set up traditional AWS profile authentication."""
    
    print("🔄 No API key provided, using traditional AWS authentication")
    print("   Checking for AWS credentials...")
    
    try:
        # Try to create a boto3 session
        session = boto3.Session(region_name=region_name, profile_name=aws_profile)
        credentials = session.get_credentials()
        
        if credentials:
            print("✅ AWS credentials found!")
            
            # Check which credential method is being used
            if os.environ.get('AWS_ACCESS_KEY_ID'):
                auth_detail = "Environment variables"
            elif os.path.exists(os.path.expanduser('~/.aws/credentials')):
                auth_detail = "AWS credentials file"
            else:
                auth_detail = "IAM role or other method"
                
            return AuthStatus(
                method='AWS Profile',
                detail=auth_detail,
                success=True,
                region=region_name,
                profile=aws_profile,
                message='AWS Profile authentication configured successfully'
            )
        else:
            print("❌ No AWS credentials found!")
            print("")
            print("📋 To fix this, choose one of these options:")
            print("   1. 🔑 Get an API key from AWS Console and paste it above (EASIEST)")
            print("   2. 🖥️  Run 'aws configure' in your terminal")
            print("   3. 🌍 Set AWS environment variables")
            
            return AuthStatus(
                method='AWS Profile',
                detail='No credentials found',
                success=False,
                region=region_name,
                profile=aws_profile,
                message='No AWS credentials found'
            )
            
    except Exception as e:
        print(f"❌ Error checking credentials: {e}")
        print("   Please ensure boto3 is installed and AWS credentials are configured.")
        
        return AuthStatus(
            method='AWS Profile',
            detail='Error checking credentials',
            success=False,
            region=region_name,
            profile=aws_profile,
            message=f'Error checking credentials: {e}'
        )


def display_auth_status(auth_status: AuthStatus) -> None:
    """
    Display formatted authentication status information.
    
    Args:
        auth_status: AuthStatus object from setup_bedrock_auth()
    """
    
    print("")
    print("=" * 60)
    print(f"✅ Authentication Method: {auth_status.method}")
    
    if auth_status.is_aws_profile:
        print(f"   Using: {auth_status.detail}")
        print(f"   Region: {auth_status.region} (Profile: {auth_status.profile})")
    else:
        print(f"   Region: {auth_status.region}")
        
    if auth_status.success:
        print("💡 Ready to create agents!")
    else:
        print("⚠️  Authentication setup needed - see messages above")
        
    print("=" * 60)


def get_auth_troubleshooting(auth_status: AuthStatus) -> None:
    """
    Display authentication troubleshooting information.
    
    Args:
        auth_status: AuthStatus object from setup_bedrock_auth()
    """
    
    print("🔧 Authentication Troubleshooting:")
    print(f"   Current method: {auth_status.method}")
    
    if auth_status.is_api_key:
        print("   ✅ Using API Key authentication")
        print("   💡 If you get authentication errors:")
        print("      - Check if your API key is valid and not expired")
        print("      - Ensure model access is enabled in AWS Console")
    else:
        print("   ✅ Using traditional AWS authentication")
        print("   💡 If you get authentication errors:")
        print("      - Try generating an API key for easier setup")
        print("      - Check your AWS credentials configuration")


def display_auth_help() -> None:
    """Display comprehensive authentication help and setup instructions."""
    
    print("🔑 AWS Bedrock Authentication Help")
    print("=" * 50)
    print()
    print("📖 How to get an API key (EASIEST method):")
    print("   1. Sign in to the AWS Bedrock Console: https://console.aws.amazon.com/bedrock/")
    print("   2. Click 'API keys' in the left navigation panel")
    print("   3. Choose 'Generate long-term API key' (lasts 30 days)")
    print("   4. Copy your API key and paste it in the notebook cell")
    print()
    print("🔧 Alternative authentication methods:")
    print("   • AWS CLI: Run 'aws configure' in your terminal")
    print("   • Environment variables: Set AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY")
    print("   • IAM roles: For production deployments on AWS services")
    print()
    print("🔒 Security best practices:")
    print("   • Use long-term keys (30 days) for learning and exploration")
    print("   • Use short-term keys (12 hours) for production applications")
    print("   • Never share your API keys or commit them to code repositories")
    print("   • Regenerate keys regularly for production use")
    print()
    print("📚 More information:")
    print("   • AWS Bedrock API Keys: https://docs.aws.amazon.com/bedrock/latest/userguide/api-keys.html")
    print("   • AWS Blog Post: https://aws.amazon.com/blogs/machine-learning/accelerate-ai-development-with-amazon-bedrock-api-keys/")
