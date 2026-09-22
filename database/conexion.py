import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

def conectar():
    """Establece la conexión a la base de datos."""
    return sqlite3.connect(BASE_DIR / "ventas.db")