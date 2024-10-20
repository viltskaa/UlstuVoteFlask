create table if not exists Teachers (
    id        integer primary key,
    email     text not null,
    classroom text not null,
    fio       text not null,
    password  text not null,
    school    text not null,
    image     text
);