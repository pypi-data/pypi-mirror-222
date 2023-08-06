"""
This module allows psycopg to use Posgresql's special date values, 'infinity' and '-infinity'.

import psycopg_infdate
import psycopg

psycopg_infdate.register_inf_date_handler(psycopg)
dbh = psycopg.connect('...')
with dbh.cursor() as cur:
    cur.execute("SELECT 'infinity'::DATE")
    answer, = cur.fetchone()

The above example shows how to apply the adapter to all database connections. For more control, instead of registering
the module, you can register the database connection, or an individual cursor.
"""

import psycopg
from psycopg import postgres
from psycopg.types.datetime import DateLoader, DateBinaryLoader
from psycopg.types.datetime import TimestampLoader, TimestampBinaryLoader
from psycopg.types.datetime import TimestamptzLoader, TimestamptzBinaryLoader
from psycopg.pq import Format
from psycopg.adapt import Dumper, Loader
import datetime as dt
from typing import Tuple, Any, Union, Type
from types import ModuleType

"""
This module allows psycopg to use Posgresql's special date values, 'infinity' and '-infinity'.
"""

Connection = psycopg.Connection[Tuple[Any, ...]]
Cursor = psycopg.Cursor[Tuple[Any, ...]]

__all__ = ('register_inf_date_handler',
           'date_plus_infinity', 'PlusInfDate',
           'date_minus_infinity', 'MinusInfDate',
           'datetime_plus_infinity', 'PlusInfDatetimeNoTz',
           'datetime_minus_infinity', 'MinusInfDatetimeNoTz',
           'datetime_tz_plus_infinity', 'PlusInfDatetime',
           'datetime_tz_minus_infinity', 'MinusInfDatetime',
           'PGDate', 'PGDateTime')


class _BaseInfDate:
    _inf_str: str
    _inf_text: bytes
    _inf_binary: bytes
    _inf_oid: int
    __slots__ = ()

    def __init__(self):
        pass

    def __add__(self, other):
        if isinstance(other, dt.timedelta):
            return self
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, dt.timedelta):
            return self
        if isinstance(other, (PlusInfDate, MinusInfDate)):
            raise ValueError('Cannot subtract infinite dates')
        return NotImplemented

    def pg_dump_text(self):
        return self._inf_text

    def pg_dump_binary(self):
        return self._inf_binary

    def __repr__(self):
        return self.__class__.__name__

    def __str__(self):
        return self._inf_str

    @classmethod
    def register_dumper(cls, obj: Union[Connection, Cursor, ModuleType]):

        class InfDateTextDumper(Dumper):
            oid = cls._inf_oid
            format = Format.TEXT

            def dump(self, _):
                return cls._inf_text

        class InfDateBinaryDumper(Dumper):
            oid = cls._inf_oid
            format = Format.BINARY

            def dump(self, _):
                return cls._inf_binary

        obj.adapters.register_dumper(cls, InfDateTextDumper)
        obj.adapters.register_dumper(cls, InfDateBinaryDumper)


class _BasePlusInfDate(_BaseInfDate):
    _inf_str = 'infinity'
    _inf_text = b'infinity'
    __slots__ = ()

    def __gt__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BaseMinusInfDate)):
            return True
        if isinstance(other, _BasePlusInfDate):
            return False
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BaseMinusInfDate, _BasePlusInfDate)):
            return True
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BaseInfDate)):
            return False
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BaseInfDate)):
            return False
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, _BasePlusInfDate):
            return True
        if isinstance(other, (dt.date, dt.datetime, _BaseMinusInfDate)):
            return False
        if isinstance(other, str) and other == 'infinity':
            return True
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, _BasePlusInfDate):
            return False
        if isinstance(other, (dt.date, dt.datetime, _BaseMinusInfDate)):
            return True
        if isinstance(other, str) and other == 'infinity':
            return False
        return NotImplemented

    def __hash__(self):
        return hash('pginfinity')


class _BaseMinusInfDate(_BaseInfDate):
    _inf_str = '-infinity'
    _inf_text = b'-infinity'
    __slots__ = ()

    def __lt__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BasePlusInfDate)):
            return True
        if isinstance(other, _BaseMinusInfDate):
            return False
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BasePlusInfDate, _BaseMinusInfDate)):
            return True
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BasePlusInfDate, _BaseMinusInfDate)):
            return False
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, (dt.date, dt.datetime, _BasePlusInfDate, _BaseMinusInfDate)):
            return False
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, _BasePlusInfDate):
            return True
        if isinstance(other, (dt.date, dt.datetime, _BaseMinusInfDate)):
            return False
        if isinstance(other, str) and other == '-infinity':
            return True
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, _BasePlusInfDate):
            return False
        if isinstance(other, (dt.date, dt.datetime, _BaseMinusInfDate)):
            return True
        if isinstance(other, str) and other == '-infinity':
            return False
        return NotImplemented

    def __hash__(self):
        return hash('-pginfinity')


class PlusInfDate(_BasePlusInfDate):
    """
    This class represents the infinite date, that is, a date that sorts after all other dates.
    You can use the instance has been created, date_plus_infinity.
    """
    _inf_binary = b'\x7f\xff\xff\xff'
    _inf_oid = postgres.types["date"].oid
    __slots__ = ()


class MinusInfDate(_BaseMinusInfDate):
    """
    This class represents the -infinite date, that is, a date that sorts before all other dates.
    You can use the instance has been created, date_minus_infinity.
    """
    _inf_binary = b'\x80\x00\x00\x00'
    _inf_oid = postgres.types["date"].oid
    __slots__ = ()


class PlusInfDatetimeNoTz(_BasePlusInfDate):
    """
    This class represents the infinite datetime, that is, a datetime that sorts after all other datetimes.
    You can use the instance has been created, datetime_plus_infinity.
    """
    _inf_binary = b'\x7f\xff\xff\xff\xff\xff\xff\xff'
    _inf_oid = postgres.types["timestamp"].oid
    __slots__ = ()


class MinusInfDatetimeNoTz(_BaseMinusInfDate):
    """
    This class represents the -infinite datetime, that is, a datetime that sorts before all other datetimes.
    You can use the instance has been created, datetime_minus_infinity.
    """
    _inf_binary = b'\x80\x00\x00\x00\x00\x00\x00\x00'
    _inf_oid = postgres.types["timestamp"].oid
    __slots__ = ()


class PlusInfDatetime(_BasePlusInfDate):
    """
    This class represents the infinite datetime, that is, a datetime that sorts before all other datetimes.
    This variant is for the Postgres timestamp with timezone and exists for type compatibility.
    It is otherwise identical to PlusInfDatetimeNoTz.
    You can use the instance has been created, datetime_tz_plus_infinity.
    """
    _inf_binary = b'\x7f\xff\xff\xff\xff\xff\xff\xff'
    _inf_oid = postgres.types["timestamptz"].oid
    __slots__ = ()


class MinusInfDatetime(_BaseMinusInfDate):
    """
    This class represents the -infinite datetime, that is, a datetime that sorts before all other datetimes.
    This variant is for the Postgres timestamp with timezone and exists for type compatibility.
    It is otherwise identical to MinusInfDatetimeNoTz.
    You can use the instance has been created, datetime_tz_minus_infinity.
    """
    _inf_binary = b'\x80\x00\x00\x00\x00\x00\x00\x00'
    _inf_oid = postgres.types["timestamptz"].oid
    __slots__ = ()


date_plus_infinity = PlusInfDate()
date_minus_infinity = MinusInfDate()
datetime_plus_infinity = PlusInfDatetimeNoTz()
datetime_minus_infinity = MinusInfDatetimeNoTz()
datetime_tz_plus_infinity = PlusInfDatetime()
datetime_tz_minus_infinity = MinusInfDatetime()


def text_loader(text_loader_superclass: Type[Loader],
                plus_inf_type: Type[_BasePlusInfDate], minus_inf_type: Type[_BaseMinusInfDate],
                plus_inf: _BasePlusInfDate, minus_inf: _BaseMinusInfDate):
    """
    Create a loader that will be used for loading data from the database.
    This is for text-based cursors.

    :param text_loader_superclass: The superclass from which to derive a new class
    :param plus_inf_type: The class corresponding to infinity
    :param minus_inf_type: The class corresponding to -infinity
    :param plus_inf: An instance of plus_inf_type
    :param minus_inf: An instance of minus_inf_type
    :return: A loader class that can be used in register_loader
    """
    class InfDateTextLoader(text_loader_superclass):
        def load(self, data):
            # noinspection PyProtectedMember
            if data == plus_inf_type._inf_text:
                return plus_inf
            # noinspection PyProtectedMember
            if data == minus_inf_type._inf_text:
                return minus_inf
            return super().load(data)

    return InfDateTextLoader


def binary_loader(binary_loader_superclass: Type[Loader],
                  plus_inf_type: Type[_BasePlusInfDate], minus_inf_type: Type[_BaseMinusInfDate],
                  plus_inf: _BasePlusInfDate, minus_inf: _BaseMinusInfDate):
    """
    Create a loader that will be used for loading data from the database.
    This is for binary cursors.

    :param text_loader_superclass: The superclass from which to derive a new class
    :param plus_inf_type: The class corresponding to infinity
    :param minus_inf_type: The class corresponding to -infinity
    :param plus_inf: An instance of plus_inf_type
    :param minus_inf: An instance of minus_inf_type
    :return: A loader class that can be used in register_loader
    """

    class InfDateBinaryLoader(binary_loader_superclass):
        def load(self, data):
            # noinspection PyProtectedMember
            if data == plus_inf_type._inf_binary:
                return plus_inf
            # noinspection PyProtectedMember
            if data == minus_inf_type._inf_binary:
                return minus_inf
            return super().load(data)

    return InfDateBinaryLoader


def register_inf_date_handler(obj: Union[ModuleType, Connection, Cursor]) -> None:
    """
    Register this handler with psycopg so that infinite dates can be sent to/from the database

    :param obj: The psycopg module, or a psycopg connection or cursor
    """
    # Sending data to the database

    PlusInfDate.register_dumper(obj)
    MinusInfDate.register_dumper(obj)

    PlusInfDatetimeNoTz.register_dumper(obj)
    MinusInfDatetimeNoTz.register_dumper(obj)

    PlusInfDatetime.register_dumper(obj)
    MinusInfDatetime.register_dumper(obj)

    # Fetching data from the database

    obj.adapters.register_loader("date", text_loader(DateLoader,
                                                     PlusInfDate, MinusInfDate,
                                                     date_plus_infinity, date_minus_infinity))
    obj.adapters.register_loader("date", binary_loader(DateBinaryLoader,
                                                       PlusInfDate, MinusInfDate,
                                                       date_plus_infinity, date_minus_infinity))
    obj.adapters.register_loader("timestamp", text_loader(TimestampLoader,
                                                          PlusInfDatetimeNoTz, MinusInfDatetimeNoTz,
                                                          datetime_plus_infinity, datetime_minus_infinity))
    obj.adapters.register_loader("timestamp", binary_loader(TimestampBinaryLoader,
                                                            PlusInfDatetimeNoTz, MinusInfDatetimeNoTz,
                                                            datetime_plus_infinity, datetime_minus_infinity))
    obj.adapters.register_loader("timestamptz", text_loader(TimestamptzLoader,
                                                            PlusInfDatetime, MinusInfDatetime,
                                                            datetime_tz_plus_infinity, datetime_tz_minus_infinity))
    obj.adapters.register_loader("timestamptz", binary_loader(TimestamptzBinaryLoader,
                                                              PlusInfDatetime, MinusInfDatetime,
                                                              datetime_tz_plus_infinity, datetime_tz_minus_infinity))


PGDate = Union[dt.date, _BaseInfDate]
PGDateTime = Union[dt.datetime, _BaseInfDate]
