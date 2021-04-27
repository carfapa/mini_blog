import sqlite3
from logger_base import logger


class Connection:
    __connect = None
    __cursor = None
    
    
    @classmethod
    def get_connection(cls):
        try:
           cls.__connect = sqlite3.connect("datablog.db")
           logger.debug(f"Conexion obtenida exitosamente: {cls.__connect}")
           return cls.__connect
        except Exception as e:
            logger.error(f'Error al obtener la conexion: {cls.__connect}')
            
    @classmethod
    def get_cursor(cls):
        try:
            cls.__cursor = cls.__connect.cursor()
            logger.debug(f"cursor obtneido exitosamente:{cls.__cursor}")
            return cls.__cursor
        except Exception as e:
            logger.error(f'Error al obtner cursor:{cls.__cursor}')
    
    @classmethod
    def close(cls):
        try:
            cls.__cursor.close()
            logger.debug(f"cursor cerrado exitosamente:{cls.__cursor}")
        except Exception as e:
            logger.error(f'Error al cerrar cursor:{cls.__cursor}')
        try:
            cls.__connect.close()
            logger.debug(f"conexion cerrada exitosamente:{cls.__cursor}")
        except Exception as e:
            logger.debug(f"Error al cerrar conexion:{cls.__cursor}")
    
    


if __name__ == '__main__':
    pass
    