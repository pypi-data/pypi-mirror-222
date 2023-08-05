from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import Boolean

from typing import List

from whitegravel.constants.app import SYSTEM_USER

from ..base import Base


class UserTable(Base):
    __tablename__ = "user"

    username: Mapped[str] = mapped_column(String(128), primary_key=True, nullable=False)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    password: Mapped[str] = mapped_column(String(192), nullable=False)
    mfa: Mapped[str] = mapped_column(String(32), nullable=True)
    mfa_enabled: Mapped[bool] = mapped_column(Boolean(), default=False)
    email: Mapped[str] = mapped_column(String(512), nullable=False)
    created_by: Mapped[str] = mapped_column(
        String(128), nullable=False, default=SYSTEM_USER
    )
    updated_by: Mapped[str] = mapped_column(
        String(128), nullable=False, default=SYSTEM_USER
    )
    created_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    last_password_set_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now, nullable=False
    )
    enabled: Mapped[bool] = mapped_column(Boolean(), default=True)
    comment: Mapped[str] = mapped_column(String(2000), default="")
    tokens: Mapped[List["TokenTable"]] = relationship(back_populates="user")
