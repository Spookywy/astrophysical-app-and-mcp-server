from fastapi import FastAPI

from external_api.get_ephemerides_data import get_ephemerides_data

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello from the astrophysical server"}


@app.get("/ephemerides")
async def get_ephemerides():
    ephemerides_data = await get_ephemerides_data()
    return {"ephemerides": ephemerides_data}
