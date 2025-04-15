import sqlalchemy as db
from configparser import ConfigParser
from sqlalchemy import create_engine


def crear_motor_mssql(
    cred: ConfigParser, database: str, driver: str, fast_executemany: bool = True
) -> db.engine.base.Engine:
    """
    Crea un motor de conexión a la base de datos utilizando las credenciales proporcionadas.

    Parametros:
    ----------
    cred : ConfigParser
        Objeto ConfigParser que contiene las credenciales de conexión.
    database : str
        Nombre de la base de datos a la que se desea conectar.
    fast_executemany : bool, opcional
        Si se establece en True, habilita el modo de ejecución rápida para mejorar el rendimiento al insertar grandes volúmenes de datos. Por defecto es True.

    Retorna:
    -------
    engine : db.engine.base.Engine
        Motor de conexión a la base de datos.
    """

    if cred.get("username"):
        sting_conn = f"mssql+pyodbc://{cred['username']}:{cred['password']}@{cred['server']}:{cred['port']}/{database}?driver={driver}"
    else:
        sting_conn = (
            f"mssql+pyodbc://{cred['server']}:{cred['port']}/{database}?driver={driver}"
        )

    return create_engine(sting_conn, fast_executemany=fast_executemany)
