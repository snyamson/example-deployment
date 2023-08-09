from fastapi import FastAPI, __version__

app = FastAPI()


@app.get('/')
async def root():
    return {'Fast Api': __version__}