from dataclasses import dataclass, asdict


@dataclass
class Teacher:
    id: int | None = 0
    email: str = ""
    classroom: str = ""
    fio: str = ""
    password: str = ""
    school: str = ""
    image: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Student:
    id: int | None = 0
    login: str = ""
    classroom: str = ""
    fio: str = ""
    password: str = ""
    school: str = ""
    image: str = ""
    teacher_id: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Answer:
    id: int | None = 0
    student_id: int = 0
    option_id: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Comment:
    id: int | None = 0
    content: str = ""
    student_id: int = 0
    poll_id: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Option:
    id: int | None = 0
    name: str = ""
    poll_id: int = 0

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Poll:
    id: int | None = 0
    title: str = ""
    image: str = ""
    event_datetime: str = ""
    description: str = ""
    tab_id: int = 0
    teacher_id: int = 0
    ending: str = ""

    def to_dict(self) -> dict:
        return asdict(self)


@dataclass
class Tab:
    id: int | None = 0
    name: str = ""
    teacher_id: int = 0

    def to_dict(self) -> dict:
        return asdict(self)
