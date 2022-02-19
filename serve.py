from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter
from pydantic import BaseModel, constr

router = APIRouter()


class ResponseModel(BaseModel):
    is_american: int = 0


class InputModel(BaseModel):
    text: constr(min_length=1)


@router.post("/", response_model=ResponseModel)
def text_clf_api(in_: InputModel):
    from train import load_model, inference

    model = load_model()
    res = inference(model, in_.text)
    return ResponseModel(is_american=res)


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

    return app
