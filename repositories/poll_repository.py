from database import get_db
from typing import Optional, List

from database.models import Poll


class PollRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Poll]:
        try:
            poll = self.database.execute(
                'SELECT * FROM Polls WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if poll:
                return Poll(*poll)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Poll]:
        try:
            poll = self.database.execute(
                'DELETE FROM Polls WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if poll:
                return Poll(*poll)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def update_by_id(self, entity_id: int, values: Poll) -> bool:
        try:
            self.database.execute(
                'UPDATE Polls SET title=?, image=?, event_datetime=?, description=?, ending=? WHERE id = ?',
                (values.title, values.image, values.event_datetime, values.description, values.ending, entity_id,)
            )
            self.database.commit()
            return True

        except Exception as e:
            # logging.error(e)
            return False

    def add(self, entity: Poll) -> Optional[Poll]:
        try:
            self.database.execute(
                'INSERT INTO Polls (title,image,event_datetime,description,ending,teacher_id,tab_id) VALUES (?,?,?,?,?,?,?)',
                (entity.title, entity.image, entity.event_datetime, entity.description, entity.ending, entity.teacher_id,entity.tab_id)
            )
            self.database.commit()
            return entity


        except Exception as e:
            # logging.error(e)
            return None

    def get_all(self) -> List[Poll]:
        try:
            poll = self.database.execute(
                'SELECT * FROM Polls').fetchall()
            poll = list(map(lambda x: Poll(*x), poll))
            return poll

        except Exception as e:
            # logging.error(e)
            return []