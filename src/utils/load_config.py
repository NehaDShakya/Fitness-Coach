"""
Application configuration loader.

This module handles loading and managing application-wide settings including:
- Directory paths
- LLM configurations
- OpenAI model settings
"""

import os
import shutil

import yaml
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from openai import OpenAI

print("Environment variables are loaded:", load_dotenv())


class LoadConfig:
    """Loads and manages application-wide configuration settings."""

    def __init__(self) -> None:
        """Initialize configuration from YAML and set up components."""
        with open("configs/app_config.yml", encoding="utf-8") as cfg:
            app_config = yaml.load(cfg, Loader=yaml.FullLoader)

        self.load_directories(app_config=app_config)
        self.load_llm_configs(app_config=app_config)
        self.load_openai_models()

    def load_directories(self, app_config: dict) -> None:
        """
        Load directory configurations.
        
        Args:
            app_config: Application configuration dictionary
        """
        self.stored_csv_xlsx_directory = app_config["directories"]["stored_csv_xlsx_directory"]
        self.stored_csv_xlsx_sqldb_directory = app_config["directories"]["stored_csv_xlsx_sqldb_directory"]

    def load_llm_configs(self, app_config: dict) -> None:
        """
        Load LLM-specific configurations.
        
        Args:
            app_config: Application configuration dictionary
        """
        self.model_name = os.getenv("gpt_deployment_name", "gpt-4-mini")
        self.agent_llm_system_role = app_config["llm_config"]["agent_llm_system_role"]
        self.rag_llm_system_role = app_config["llm_config"]["rag_llm_system_role"]
        self.temperature = app_config["llm_config"]["temperature"]
        self.embedding_model_name = os.getenv(
            "embed_deployment_name", "text-embedding-3-small"
        )

    def load_openai_models(self) -> None:
        """Initialize OpenAI clients and models."""
        openai_api_key = os.environ["OPENAI_API_KEY"]
        
        self.openai_client = OpenAI(api_key=openai_api_key)
        self.langchain_llm = ChatOpenAI(
            model_name=self.model_name,
            temperature=self.temperature,
        )

    def remove_directory(self, directory_path: str) -> None:
        """
        Safely remove a directory and its contents.
        
        Args:
            directory_path: Path to directory to remove
        """
        if os.path.exists(directory_path):
            try:
                shutil.rmtree(directory_path)
                print(f"Directory '{directory_path}' successfully removed.")
            except OSError as e:
                print(f"Error removing directory: {e}")
        else:
            print(f"Directory '{directory_path}' does not exist.")
