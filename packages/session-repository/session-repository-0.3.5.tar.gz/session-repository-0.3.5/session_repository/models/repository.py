# MODULES
from typing import Any, Callable, Dict, List, Optional, Tuple, Type, TypeVar, Union
from logging import Logger

# CONNTEXTLIB
from contextlib import AbstractContextManager

# SQLALCHEMY
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, InstrumentedAttribute, Query

# UTILS
from session_repository.utils import (
    _FilterType,
    apply_no_load,
    apply_filters,
    apply_order_by,
    apply_limit,
    apply_pagination,
)


def with_session(func):
    def wrapper(self, *args, **kwargs):
        if kwargs.get("current_session") is not None:
            return func(self, *args, **kwargs)

        with self.session_manager() as session:
            kwargs["current_session"] = session

            return func(self, *args, **kwargs)

    return wrapper


T = TypeVar("T", bound=declarative_base())


class SessionRepository:
    def __init__(
        self,
        session_factory: Callable[..., AbstractContextManager[Session]],
        logger: Logger,
        literal_binds: bool = True,
    ) -> None:
        self._session_factory = session_factory
        self._logger = logger
        self._literal_binds = literal_binds

    @classmethod
    def _log_sql_query(
        cls,
        query: Query,
        logger: Logger,
        literal_binds: bool = False,
    ):
        if logger is None:
            return

        query_compiled = query.statement.compile(
            compile_kwargs={
                "literal_binds": literal_binds,
            }
        )
        logger.info(query_compiled.string)

    def session_manager(self):
        return self._session_factory()

    @with_session
    def _select(
        self,
        model: Type[T],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        disabled_relationships: Optional[Dict[InstrumentedAttribute, Any]] = None,
        current_session: Optional[Session] = None,
    ) -> Optional[T]:
        query = current_session.query(model)

        return self._select_query(
            query=query,
            filters=filters,
            optional_filters=optional_filters,
            disabled_relationships=disabled_relationships,
        )

    def _select_query(
        self,
        query: Query,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        disabled_relationships: Optional[Dict[InstrumentedAttribute, Any]] = None,
    ) -> Optional[Any]:
        query = apply_no_load(
            query=query,
            relationship_dict=disabled_relationships,
        )
        query = apply_filters(
            query=query,
            filter_dict=filters,
        )
        query = apply_filters(
            query=query,
            filter_dict=optional_filters,
            with_optional=True,
        )
        result = query.first()

        self._log_sql_query(
            query=query,
            logger=self._logger,
            literal_binds=self._literal_binds,
        )

        return result

    @with_session
    def _select_all(
        self,
        model: Type[T],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        disabled_relationships: Optional[Dict[InstrumentedAttribute, Any]] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        current_session: Optional[Session] = None,
    ) -> List[T]:
        query = current_session.query(model)

        return self._select_all_query(
            query=query,
            model=model,
            filters=filters,
            optional_filters=optional_filters,
            disabled_relationships=disabled_relationships,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

    def _select_all_query(
        self,
        query: Query,
        model: Type[T],
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        disabled_relationships: Optional[Dict[InstrumentedAttribute, Any]] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
    ) -> List[T]:
        query = apply_no_load(
            query=query,
            relationship_dict=disabled_relationships,
        )
        query = apply_filters(
            query=query,
            filter_dict=filters,
        )
        query = apply_filters(
            query=query,
            filter_dict=optional_filters,
            with_optional=True,
        )
        query = apply_order_by(
            query=query,
            model=model,
            order_by=order_by,
            direction=direction,
        )
        query = apply_limit(
            query=query,
            limit=limit,
        )

        results = query.all()

        self._log_sql_query(
            query=query,
            logger=self._logger,
            literal_binds=self._literal_binds,
        )

        return results

    @with_session
    def _select_paginate(
        self,
        model: Type[T],
        page: int,
        per_page: int,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        disabled_relationships: Optional[Dict[InstrumentedAttribute, Any]] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
        current_session: Optional[Session] = None,
    ) -> Tuple[List[T], str]:
        query = current_session.query(model)

        return self._select_paginate_query(
            query=query,
            model=model,
            page=page,
            per_page=per_page,
            filters=filters,
            optional_filters=optional_filters,
            disabled_relationships=disabled_relationships,
            order_by=order_by,
            direction=direction,
            limit=limit,
        )

    def _select_paginate_query(
        self,
        query: Query,
        model: Type[T],
        page: int,
        per_page: int,
        filters: Optional[_FilterType] = None,
        optional_filters: Optional[_FilterType] = None,
        disabled_relationships: Optional[Dict[InstrumentedAttribute, Any]] = None,
        order_by: Optional[Union[List[str], str]] = None,
        direction: Optional[str] = None,
        limit: int = None,
    ) -> Tuple[List[T], str]:
        query = apply_no_load(
            query=query,
            relationship_dict=disabled_relationships,
        )
        query = apply_filters(
            query=query,
            filter_dict=filters,
        )
        query = apply_filters(
            query=query,
            filter_dict=optional_filters,
            with_optional=True,
        )
        query = apply_order_by(
            query=query,
            model=model,
            order_by=order_by,
            direction=direction,
        )
        query = apply_limit(
            query=query,
            limit=limit,
        )
        query, pagination = apply_pagination(
            query=query,
            page=page,
            per_page=per_page,
        )

        results = query.all()

        self._log_sql_query(
            query=query,
            logger=self._logger,
            literal_binds=self._literal_binds,
        )

        return results, pagination

    @with_session
    def _update(
        self,
        model: Type[T],
        values: Dict,
        filters: Optional[_FilterType] = None,
        flush: bool = False,
        commit: bool = False,
        current_session: Optional[Session] = None,
    ) -> List[T]:
        rows = self._select_all(
            model=model,
            filters=filters,
            current_session=current_session,
        )

        if len(rows) == 0:
            return rows

        for row in rows:
            for key, value in values.items():
                setattr(row, key, value)

        if flush:
            current_session.flush()
        if commit:
            current_session.commit()

        [current_session.refresh(row) for row in rows]

        return rows

    @with_session
    def _add(
        self,
        data: Union[List[T], T],
        flush: bool = False,
        commit: bool = False,
        current_session: Optional[Session] = None,
    ) -> Union[List[T], T]:
        current_session.add_all(data) if isinstance(
            data, list
        ) else current_session.add(data)
        if flush:
            current_session.flush()
        if commit:
            current_session.commit()

        if flush or commit:
            current_session.refresh(data)

        return data

    @with_session
    def _delete(
        self,
        model: T,
        filters: Optional[_FilterType] = None,
        flush: bool = True,
        commit: bool = False,
        current_session: Optional[Session] = None,
    ) -> bool:
        rows: List = self._select_all(
            model=model,
            filters=filters,
            current_session=current_session,
        )

        if len(rows) == 0:
            return False

        for row in rows:
            current_session.delete(row)

        if flush:
            current_session.flush()
        if commit:
            current_session.commit()

        return True
