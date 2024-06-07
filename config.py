import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Configurações de limite de requisição
AGENT_MAX_RPM = 3
AGENT_MAX_ITER = 3
CREW_MAX_RPM = 10
