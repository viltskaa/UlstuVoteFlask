
from typing import Optional, List

from database import get_db
from database.models import Tab


class TabRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Tab]:
        try:
            tab = self.database.execute(
                'SELECT * FROM Tabs WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if tab:
                return Tab(*tab)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Tab]:
        try:
            tab = self.database.execute(
                'DELETE FROM Tabs WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if tab:
                return Tab(*tab)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def update_by_id(self, entity_id: int, values: Tab) -> bool:
        try:
            self.database.execute(
                'UPDATE Tabs SET name=? WHERE id = ?',
                (values.name, entity_id,)
            )
            self.database.commit()
            return True

        except Exception as e:
            # logging.error(e)
            return False

    def add(self, entity: Tab) -> Optional[Tab]:
        try:
            self.database.execute(
                'INSERT INTO Tabs (name, teacher_id) VALUES (?, ?)',
                (entity.name, entity.teacher_id,)
            )
            self.database.commit()
            return entity


        except Exception as e:
            # logging.error(e)
            return None

    def get_all(self) -> List[Tab]:
        try:
            tab = self.database.execute(
                'SELECT * FROM Tabs').fetchall()
            tab = list(map(lambda x: Tab(*x), tab))
            return tab

        except Exception as e:
            # logging.error(e)
            return []
