
from fastapi import FastAPI
from agentos_sales.routes.orders import router as orders_router

app = FastAPI(title="AgentOS Sales v2")
app.include_router(orders_router)
