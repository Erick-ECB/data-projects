CREATE DATABASE book_catalog;


CREATE TABLE books (
    isbn13 CHAR(13) PRIMARY KEY,
    isbn10 CHAR(10),
    title TEXT,
    subtitle VARCHAR(255),
    authors TEXT [],
    categories TEXT [],
    thumbnail VARCHAR(150),
    description TEXT,
    published_year INTEGER,
    average_rating NUMERIC,
    num_pages INTEGER,
    ratings_count INTEGER
);

