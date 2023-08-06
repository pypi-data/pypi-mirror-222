#!/usr/bin/env python3

import pymssql
import singer

LOGGER = singer.get_logger('macrometa_source_mssql')


# TODO: @backoff.on_exception(backoff.expo, pymssql.Error, max_tries=5, factor=2)
def connect_with_backoff(connection):
    warnings = []
    with connection.cursor():
        if warnings:
            LOGGER.info(
                (
                    "Encountered non-fatal errors when configuring session that could "
                    "impact performance:"
                )
            )
        for w in warnings:
            LOGGER.warning(w)

    return connection


class MSSQLConnection(pymssql.Connection):
    def __init__(self, config, require_database=True):
        args = {
            "user": config.get("user"),
            "password": config.get("password"),
            "server": config["host"],
            "charset": config.get("characterset", "utf8"),
            "port": config.get("port", "1433"),
            "tds_version": config.get("tds_version", "7.3"),
        }
        if require_database:
            args["database"] = config["database"]
        conn = pymssql._mssql.connect(**args)
        super().__init__(conn, False, True)

    def __enter__(self):
        return self

    def __exit__(self, *exc_info):
        del exc_info
        self.close()


def make_connection_wrapper(config):
    class ConnectionWrapper(MSSQLConnection):
        def __init__(self, *args, **kwargs):
            super().__init__(config)

            connect_with_backoff(self)

    return ConnectionWrapper
