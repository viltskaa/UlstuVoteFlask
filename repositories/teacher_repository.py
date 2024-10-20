from database import get_db
from typing import Optional, List

from database.models import Teacher
from utils import singleton


@singleton
class TeacherRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Teacher]:
        try:
            teacher = self.database.execute(
                'SELECT * FROM Teachers WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if teacher:
                return Teacher(*teacher)
            return None

        except Exception as e:
            print(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Teacher]:
        try:
            teacher = self.database.execute(
                'DELETE FROM Teachers WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if teacher:
                return Teacher(*teacher)
            return None

        except Exception as e:
            print(e)
            return None

    def update_by_id(self, entity_id: int, values: Teacher) -> bool:
        try:
            self.database.execute(
                'UPDATE Teachers SET email = ?, classroom = ?, fio = ?, password = ?, school = ?, image = ? WHERE id = ?',
                (values.email, values.classroom, values.fio, values.password, values.school, values.image, entity_id,)
            )
            self.database.commit()
            return True

        except Exception as e:
            print(e)
            return False

    def add(self, entity: Teacher) -> Optional[Teacher]:
        try:
            self.database.execute(
                'INSERT INTO Teachers (email, classroom, fio, password, school, image) VALUES (?, ?, ?, ?, ?, ?)',
                (entity.email, entity.classroom, entity.fio, entity.password, entity.school, entity.image)
            )
            self.database.commit()
            return entity


        except Exception as e:
            print(e)
            return None

    def get_all(self) -> List[Teacher]:
        try:
            teacher = self.database.execute(
                'SELECT * FROM Teachers'
            ).fetchall()
            teacher = list(map(lambda x: Teacher(*x), teacher))
            return teacher

        except Exception as e:
            # logging.error(e)
            return []
