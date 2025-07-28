from pydantic import BaseModel, EmailStr  # Ferramentas para validar dados
from datetime import datetime  # Para trabalhar com datas
from typing import Optional  # Para dizer que um campo pode ser vazio

class UserBase(BaseModel):  # Modelo base com campos comuns
    full_name: Optional[str] = None  # Nome completo (pode ser vazio)
    role: str = "member"  # Função na biblioteca (padrão é "member")

class UserCreate(BaseModel):  # Modelo para cadastrar usuário
    email: EmailStr  # Email (tem que ser válido, ex.: teste@email.com)
    password: str  # Senha
    full_name: Optional[str] = None  # Nome completo (opcional)
    role: str = "member"  # Função (padrão é "member")

class UserUpdate(BaseModel):  # Modelo para atualizar usuário
    full_name: Optional[str] = None  # Nome completo (opcional)
    role: Optional[str] = None  # Função (opcional)

class User(UserBase):  # Modelo completo do usuário
    id: str  # ID do usuário (vem do Supabase)
    email: EmailStr  # Email
    updated_at: Optional[datetime] = None  # Quando o perfil foi atualizado

    class Config:  # Configuração extra
        from_attributes = True  # Permite usar dados do banco
        