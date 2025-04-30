from typing import Annotated

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import get_db_session

DatabaseSession = Annotated[AsyncSession, Depends(get_db_session)]
"""FastAPI dependency to get the database session"""
