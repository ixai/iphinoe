import random
from typing import Dict

from fastapi import FastAPI

app = FastAPI()


@app.get("/rest/health")
async def health_check() -> str:
    return "ok"


@app.post("/rest/v1/invoices/pay")
async def pay_invoice() -> Dict[str, bool]:
    return {"result": bool(random.randint(0, 1))}
