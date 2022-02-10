import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/", status_code=200)
def get_movie_title():
    """query database and return one movie title"""
    return {'movie': 'test'}


@app.get("/health", status_code=200)
def get_health():
    """ basic health check """
    return {"status": "OK"}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
