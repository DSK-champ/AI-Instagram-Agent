"""
Configuration management for Instagram automation agents.
Handles API key loading and Droidrun configuration setup.
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from droidrun.config_manager import DroidrunConfig, AgentConfig, LLMProfile

# Load environment variables from .env file
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path, override=True)


def get_api_key() -> str:
    """
    Get Gemini API key from environment variable.
    
    Raises:
        ValueError: If API key is not found in environment variables.
    
    Returns:
        str: The Gemini API key
    """
    api_key = os.getenv("GEMINI_API_KEY")
    
    # Fallback: hardcode the key if env var is not set
    if not api_key:
        api_key = "AIzaSyCMxJ2ZqrfPD4S6g9qBY7oHV33vWiboJwA"
    
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY environment variable not set. "
            "Please set it in your .env file or environment."
        )
    return api_key


def create_config(max_steps: int = 30) -> DroidrunConfig:
    """
    Create Droidrun configuration with Gemini LLM profiles.
    
    Args:
        max_steps: Maximum number of steps the agent can take (default: 30)
    
    Returns:
        DroidrunConfig: Configured DroidrunConfig object
    """
    api_key = get_api_key()
    
    # Create LLM profile for Gemini
    gemini_profile = LLMProfile(
        provider="GoogleGenAI",
        model="models/gemini-2.5-flash",
        kwargs={"api_key": api_key}
    )
    
    # Configure for complex multi-step task
    config = DroidrunConfig(
        agent=AgentConfig(
            reasoning=True,      # Enable Manager/Executor workflow for planning
            max_steps=max_steps,
        ),
        llm_profiles={
            "manager": gemini_profile,
            "executor": gemini_profile,
            "text_manipulator": gemini_profile,
            "app_opener": gemini_profile,
            "scripter": gemini_profile
        }
    )
    
    return config
