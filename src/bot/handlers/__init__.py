from aiogram import Router

from .admin import router as admin_router
from .common import router as common_router

router = Router()
router.include_routers(
    admin_router,
    common_router,
)
