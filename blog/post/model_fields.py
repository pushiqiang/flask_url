# -*- coding: utf-8 -*-


import time
from datetime import datetime
import sqlalchemy.types as types


class TimeStamp(types.TypeDecorator):
    """
    自定义时间戳类型,数据库保存bigint类型,默认渲染为datetime类型
    """

    impl = types.BigInteger

    def process_bind_param(self, value, dialect):
        """
        适配时间戳和datetime类型
        """
        if value is None:
            return value

        if isinstance(value, datetime):
            value = int(time.mktime(value.timetuple()))

        return value


    def process_result_value(self, value, dialect):
        """
        默认渲染为datetime类型
        """
        return datetime.fromtimestamp(value)
