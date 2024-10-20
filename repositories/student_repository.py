from database import get_db
from typing import Optional, List

from database.models import Student


class StudentRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Student]:
        try:
            student = self.database.execute(
                'SELECT * FROM Students WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if student:
                return Student(*student)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Student]:
        try:
            student = self.database.execute(
                'DELETE FROM Students WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if student:
                return Student(*student)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def update_by_id(self, entity_id: int, values: Student) -> bool:
        try:
            self.database.execute(
                'UPDATE Students SET login=?, password=?, fio=?, image=? WHERE id = ?',
                (values.login, values.password, values.fio, values.image, entity_id,)
            )
            self.database.commit()
            return True

        except Exception as e:
            # logging.error(e)
            return False

    def add(self, entity: Student) -> Optional[Student]:
        try:
            self.database.execute(
                'INSERT INTO Students (login,password,fio,image, teacher_id) VALUES (?, ?)',
                (entity.login, entity.password, entity.fio, entity.image, entity.teacher_id,)
            )
            self.database.commit()
            return entity


        except Exception as e:
            # logging.error(e)
            return None

    def get_all(self) -> List[Student]:
        try:
            student = self.database.execute(
                'SELECT * FROM Students').fetchall()
            student = list(map(lambda x: Student(*x), student))
            return student

        except Exception as e:
            # logging.error(e)
            return []