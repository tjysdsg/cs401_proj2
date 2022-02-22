import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from pydantic import BaseModel, constr

router = APIRouter()


class ResponseModel(BaseModel):
    is_american: int = 0


class InputModel(BaseModel):
    text: constr(min_length=1)


@router.post("/api/american", response_model=ResponseModel)
def text_clf_api(in_: InputModel):
    from train import load_model, inference

    model = load_model()
    res = inference(model, in_.text)
    return ResponseModel(is_american=res)


def download_model():
    import urllib.request
    urllib.request.urlretrieve("https://raw.githubusercontent.com/tjysdsg/cs401_proj2/master/model.pkl", "model.pkl")


def create_app():
    app = FastAPI()
    app.include_router(router)

    # allow same origin for testing
    origins = ["*"]
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    download_model()

    return app


if __name__ == '__main__':
    app = create_app()
    server_port = int(os.environ.get('SERVER_PORT'))
    if server_port is None:
        server_port = 8080

    host = "0.0.0.0"
    print(f'Running on {host}:{server_port}')
    uvicorn.run(app, host=host, port=server_port)
