from datetime import datetime

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Boolean

from ..base import Base
from .user import UserTable


class TokenTable(Base):
    __tablename__ = "token"

    id: Mapped[str] = mapped_column(String(32), primary_key=True, nullable=False)
    type: Mapped[str] = mapped_column(String(64), nullable=False)
    username: Mapped[str] = mapped_column(ForeignKey("user.username"), nullable=False)
    user: Mapped[UserTable] = relationship(back_populates="tokens")
    revoked: Mapped[bool] = mapped_column(Boolean(), default=False, nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now, nullable=False
    )
    expiration: Mapped[datetime] = mapped_column(DateTime(), nullable=False)
    last_ipaddress: Mapped[str] = mapped_column(String(40), nullable=False)
    last_user_agent: Mapped[str] = mapped_column(String(2000), nullable=False)
    last_timestamp: Mapped[datetime] = mapped_column(
        DateTime(), default=datetime.now, nullable=False
    )
