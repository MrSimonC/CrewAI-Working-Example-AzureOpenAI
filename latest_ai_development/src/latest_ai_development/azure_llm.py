import os
from crewai import LLM

os.environ["AZURE_API_KEY"] = os.environ.get("AZURE_OPENAI_KEY_GPT4O")
os.environ["AZURE_API_BASE"] = "https://sc-main-openai-eastus.openai.azure.com/"
os.environ["AZURE_API_VERSION"] = "2024-02-01"
DEPLOYMENT_NAME = "simon-gpt-4o-mini"

azureopenai_llm = LLM(
    model=f"azure/{DEPLOYMENT_NAME}",
    temperature=0.7
)

# os.environ["AZURE_OPENAI_VERSION"] = "2024-02-01"
# os.environ["AZURE_OPENAI_DEPLOYMENT"] = "simon-gpt-4o"
# os.environ["AZURE_OPENAI_ENDPOINT"] = "https://sc-main-openai-eastus.openai.azure.com/"
# os.environ["OPENAI_API_KEY"] = os.environ.get("AZURE_OPENAI_KEY_GPT4O")

# AZURE_EMBEDDING_MODEL_NAME = 'text-embedding-ada-002'
# AZURE_EMBEDDING_DEPLOYMENT_NAME = 'simon-text-embedding-ada-002'

# AZURE_EMBEDDER_CONFIG = {
#     "provider": "azure_openai",
#     "config": {
#         "model": AZURE_EMBEDDING_MODEL_NAME,
#         "deployment_name": AZURE_EMBEDDING_DEPLOYMENT_NAME,
#     }
# }

# AZURE_LLM_AND_EMBEDDER_CONFIG = {
#     "llm": {
#         "provider": "azure_openai",
#         "config": {
#             "api_key": os.environ.get("AZURE_OPENAI_KEY"),
#             "model": os.environ.get("AZURE_OPENAI_DEPLOYMENT"),
#             "deployment_name": os.environ.get("AZURE_OPENAI_DEPLOYMENT")
#         }
#     },
#     "embedder": AZURE_EMBEDDER_CONFIG
# }

# azure_llm = AzureChatOpenAI(
#     azure_endpoint=os.environ.get("AZURE_OPENAI_ENDPOINT"),
#     api_key=os.environ.get("AZURE_OPENAI_KEY"),
#     api_version=os.environ.get("AZURE_OPENAI_VERSION"),
#     azure_deployment=os.environ.get("AZURE_OPENAI_DEPLOYMENT")
# )
