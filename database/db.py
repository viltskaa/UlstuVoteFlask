import sqlite3
from pathlib import Path

from flask import g

_root = Path(__file__).parent.parent


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            _root / 'database.db',
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
