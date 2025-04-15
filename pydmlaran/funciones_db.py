import sqlalchemy as db
from configparser import ConfigParser
from sqlalchemy import create_engine


def crear_motor_mssql(
    cred: ConfigParser, database: str, driver: str
) -> db.engine.base.Engine:
    """
    Crea un motor de conexión a la base de datos utilizando las credenciales proporcionadas.

    Parametros:
    ----------
    cred : ConfigParser
        Objeto ConfigParser que contiene las credenciales de conexión.
    database : str
        Nombre de la base de datos a la que se desea conectar.

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

    return create_engine(sting_conn)
