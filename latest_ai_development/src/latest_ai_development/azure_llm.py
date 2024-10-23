import os
from crewai import LLM

os.environ["AZURE_API_KEY"] = os.environ.get("AZURE_OPENAI_KEY_GPT4O") # AZURE_OPENAI_KEY_GPT4O is an environment variable with a secret I expose to the GitHub Codespace
os.environ["AZURE_API_BASE"] = "https://sc-main-openai-eastus.openai.azure.com/"
os.environ["AZURE_API_VERSION"] = "2024-02-01"
DEPLOYMENT_NAME = "simon-gpt-4o-mini"

azureopenai_llm = LLM(
    model=f"azure/{DEPLOYMENT_NAME}",
    temperature=0.7
)
