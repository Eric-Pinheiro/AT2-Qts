from fastapi import FastAPI, Request, HTTPException
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

app = FastAPI(title="IT Provisioning")
templates = Jinja2Templates(directory="templates")

class Workstation(BaseModel):
    hostname: str
    os_version: str

def notify_inventory_system(hostname: str) -> bool:
    """Simula uma dependência externa (ex: API de CMDB/Inventário)"""
    return True # Será mockado nos testes

@app.get("/")
async def get_portal(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/api/provision", status_code=201)
async def provision_workstation(workstation: Workstation):
    success = notify_inventory_system(workstation.hostname)
    if not success:
        raise HTTPException(status_code=503, detail="Falha ao sincronizar com sistema de inventário")
    return {"status": "success", "hostname": workstation.hostname, "message": "Provisionamento iniciado"}