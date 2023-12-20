CREATE TABLE wine_reviews (
    id SERIAL PRIMARY KEY,
    country VARCHAR(30),
    description TEXT,
    designation VARCHAR(100),
    points INTEGER,
    price FLOAT,
    province VARCHAR(50),
    region_1 VARCHAR(100),
    region_2 VARCHAR(100),
    taster_name VARCHAR(30),
    title VARCHAR(150),
    variety VARCHAR(50),
    winery VARCHAR(60),
    year INTEGER
);