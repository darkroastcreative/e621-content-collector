CREATE TABLE downloaded_posts (
    id   INTEGER PRIMARY KEY ASC
                 UNIQUE
                 NOT NULL,
    url  TEXT    NOT NULL,
    tags TEXT    NOT NULL
);