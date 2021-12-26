create table users(
    id INTEGER PRIMARY KEY NOT NULL,
    user_id INTEGER,
    date DATETIME
);

create table coins(
    id INTEGER PRIMARY KEY NOT NULL,
    name TEXT,
    quote TEXT,
    price TEXT,
    change1h TEXT,
    change24h TEXT
);

