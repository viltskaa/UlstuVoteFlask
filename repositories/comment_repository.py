from database import get_db
from typing import Optional, List

from database.models import Comment


class CommentRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Comment]:
        try:
            comment = self.database.execute(
                'SELECT * FROM Comments WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if comment:
                return Comment(*comment)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Comment]:
        try:
            comment = self.database.execute(
                'DELETE FROM Comments WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if comment:
                return Comment(*comment)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def update_by_id(self, entity_id: int, values: Comment) -> bool:
        try:
            self.database.execute(
                'UPDATE Comments SET content=? WHERE id = ?',
                (values.content, values.poll_id, values.student_id, entity_id,)
            )
            self.database.commit()
            return True

        except Exception as e:
            # logging.error(e)
            return False

    def add(self, entity: Comment) -> Optional[Comment]:
        try:
            self.database.execute(
                'INSERT INTO Comments(content,poll_id, student_id) VALUES (?,?,?)',
                (
                    entity.content, entity.poll_id, entity.student_id)
            )
            self.database.commit()
            return entity


        except Exception as e:
            # logging.error(e)
            return None

    def get_all(self) -> List[Comment]:
        try:
            comment = self.database.execute(
                'SELECT * FROM Comments').fetchall()
            comment = list(map(lambda x: Comment(*x), comment))
            return comment

        except Exception as e:
            # logging.error(e)
            return []
