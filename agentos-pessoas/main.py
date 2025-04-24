
from fastapi import FastAPI
from agentos_pessoas.routes.users import router as user_router

app = FastAPI(title="AgentOS Pessoas v2")
app.include_router(user_router)
