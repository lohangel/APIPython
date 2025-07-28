# from fastapi import FastAPI  # Ferramenta para criar API
# from app.api.v1.auth import router as auth_router  # Rotas de autenticação
# from app.api.v1.users import router as users_router  # Rotas de usuários

# app = FastAPI(title="Library API", version="1.0.0", description="API for managing users in an online library")  # Cria API

# app.include_router(auth_router, prefix="/api/v1")  # Adiciona rotas de autenticação
# app.include_router(users_router, prefix="/api/v1")  # Adiciona rotas de usuários

# @app.get("/", summary="Welcome message", description="Returns a welcome message for the Library API.")
# async def root():  # Rota inicial
#     return {"message": "Welcome to the Library API"}

import os
import uvicorn
from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router

app = FastAPI(
    title="Library API",
    version="1.0.0",
    description="API for managing users in an online library"
)

app.include_router(auth_router, prefix="/api/v1")
app.include_router(users_router, prefix="/api/v1")

@app.get("/", summary="Welcome message", description="Returns a welcome message for the Library API.")
async def root():
    return {"message": "Welcome to the Library API"}

# 👇 Adicione isso no final
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))  # Pega porta do Render ou usa 8000 localmente
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)
