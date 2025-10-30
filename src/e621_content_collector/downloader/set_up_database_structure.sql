/* Create posts table to store information about downloaded posts. */
CREATE TABLE IF NOT EXISTS posts (
    id            INTEGER PRIMARY KEY ASC
                          UNIQUE
                          NOT NULL,
    url           TEXT    NOT NULL,
    description   TEXT,
    rating        TEXT    NOT NULL,
    width         INTEGER NOT NULL,
    height        INTEGER NOT NULL,
    extension     TEXT    NOT NULL,
    size          INTEGER NOT NULL,
    created_at    TEXT    NOT NULL,
    updated_at    TEXT    NOT NULL,
    downloaded_at TEXT    NOT NULL
);

/* Create tags table to store tags associated with downloaded posts. */
CREATE TABLE IF NOT EXISTS tags (
    id TEXT NOT NULL
          UNIQUE
          PRIMARY KEY ASC
);

/* Create a bridge table to easily associate posts with the tags they're assigned. */
CREATE TABLE IF NOT EXISTS posts_tags_bridge (
    post_id INTEGER REFERENCES posts (id) 
                    NOT NULL,
    tag_id  TEXT    REFERENCES tags (id) 
                    NOT NULL
);