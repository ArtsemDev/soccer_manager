from typing import Type, Any, Sequence
from inspect import iscoroutine

from sqlalchemy import Column, INT, create_engine, Row, RowMapping, select
from sqlalchemy.orm import DeclarativeBase, declared_attr, sessionmaker, Session
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True, autoincrement=True)

    engine = create_engine('sqlite:///db.sqlite3')
    session = sessionmaker(bind=engine)

    async_engine = create_async_engine('sqlite+aiosqlite:///db.sqlite3')
    async_session = async_sessionmaker(bind=async_engine)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')

    @staticmethod
    def create_session(func):
        async def async_wrapper(*args, **kwargs):
            async with Base.async_session() as session:
                return await func(*args, **kwargs, session=session)

        def wrapper(*args, **kwargs):
            with Base.session() as session:
                return func(*args, **kwargs, session=session)

        return async_wrapper if iscoroutine(func) else wrapper

    @create_session
    def save(self, session: Session = None) -> None:
        session.add(self)
        session.commit()
        session.refresh(self)

    @classmethod
    @create_session
    def get(cls, pk: int, session: Session = None) -> Type["Base"]:
        return session.get(cls, pk)

    @create_session
    def delete(self, session: Session = None) -> None:
        session.delete(self)
        session.commit()

    @classmethod
    @create_session
    def select(
            cls,
            *args,
            order_by: Any = 'id',
            limit: int = None,
            offset: int = None,
            session: Session = None
    ) -> Sequence[Row | RowMapping | Any]:
        return session.scalars(
            select(cls)
            .order_by(order_by)
            .limit(limit)
            .offset(offset)
            .filter(*args)
        ).all()

    @classmethod
    @create_session
    def join(
            cls,
            right: Type["Base"],
            *args,
            limit: int = None,
            offset: int = None,
            session: Session = None
    ) -> Sequence[Row | RowMapping | Any]:
        return session.execute(
            select(cls, right)
            .limit(limit)
            .offset(offset)
            .filter(*args)
            .join(right)
        ).all()
