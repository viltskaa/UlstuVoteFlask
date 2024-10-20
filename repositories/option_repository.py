from database import get_db
from typing import Optional, List

from database.models import Option


class OptionRepository:
    def __init__(self):
        self.database = get_db()

    def get_by_id(self, entity_id: int) -> Optional[Option]:
        try:
            option = self.database.execute(
                'SELECT * FROM Options WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if option:
                return Option(*option)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def delete_by_id(self, entity_id: int) -> Optional[Option]:
        try:
            option = self.database.execute(
                'DELETE FROM Options WHERE id = ?',
                (entity_id,)
            ).fetchone()
            if option:
                return Option(*option)
            return None

        except Exception as e:
            # logging.error(e)
            return None

    def update_by_id(self, entity_id: int, values: Option) -> bool:
        try:
            self.database.execute(
                'UPDATE Options SET name=? WHERE id = ?',
                (values.name, values.poll_id, entity_id, )
            )
            self.database.commit()
            return True

        except Exception as e:
            # logging.error(e)
            return False

    def add(self, entity: Option) -> Optional[Option]:
        try:
            self.database.execute(
                'INSERT INTO Options(name,poll_id) VALUES (?,?)',
                (
                    entity.name, entity.poll_id)
            )
            self.database.commit()
            return entity


        except Exception as e:
            # logging.error(e)
            return None

    def get_all(self) -> List[Option]:
        try:
            option = self.database.execute(
                'SELECT * FROM Options').fetchall()
            option = list(map(lambda x: Option(*x), option))
            return option

        except Exception as e:
            # logging.error(e)
            return []
