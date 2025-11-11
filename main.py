from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

from external_api.get_ephemerides_data import get_ephemerides_data

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from the astrophysical server"}


@app.get("/ephemerides", operation_id="get_ephemerides")
async def get_ephemerides():
    """Gets ephemerides data"""
    ephemerides_data = await get_ephemerides_data()
    return {"ephemerides": ephemerides_data}


mcp = FastApiMCP(app, include_operations=["get_ephemerides"])
mcp.mount()
