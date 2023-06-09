from fastapi import APIRouter

from study.controllers import papeis_control as papeis

router = APIRouter()

router.include_router(papeis.router, prefix='/papeis')
