from database import get_db
from typing import Optional, List

from database.models import Answer


class AnswerRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Answer]:
        try:
            answer = self.database.execute(
                'SELECT * FROM Answers WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if answer:
                return Answer(*answer)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Answer]:
        try:
            answer = self.database.execute(
                'DELETE FROM Answers WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if answer:
                return Answer(*answer)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def add(self, entity: Answer) -> Optional[Answer]:
        try:
            self.database.execute(
                'INSERT INTO Answers(option_id, student_id) VALUES (?,?)',
                (
                    entity.option_id, entity.student_id)
            )
            self.database.commit()
            return entity


        except Exception as e:
            # logging.error(e)
            return None

    def get_all(self) -> List[Answer]:
        try:
            answer = self.database.execute(
                'SELECT * FROM Answers').fetchall()
            answer = list(map(lambda x: Answer(*x), answer))
            return answer

        except Exception as e:
            # logging.error(e)
            return []