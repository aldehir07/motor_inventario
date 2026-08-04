from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI


def configure_cors(app: FastAPI) -> None:
    """
    Configura la política CORS de la API.
    """

    app.add_middleware(
        CORSMiddleware,

        allow_origins=[
            "http://localhost:3000",   # React
            "http://localhost:5173",   # Vite
            "http://127.0.0.1:5173",
        ],

        allow_credentials=True,

        allow_methods=["*"],

        allow_headers=["*"],
    )