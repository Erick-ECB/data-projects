# CSV to Database

This project involves the creation of a PostgreSQL database to manage information about a catalog of books. The goal is to design a database schema, create the necessary tables, and import the data from a CSV file.
 
 ## Source of Dataset

The dataset used in this project was obtained from [Kaggle](https://www.kaggle.com/). It is essential to acknowledge and give credit to the contributors and providers of the dataset. For more details and to access the original dataset, please visit the Kaggle dataset page: [Books Dataset](https://www.kaggle.com/datasets/abdallahwagih/books-dataset).

## Dataset Overview

| Column Name     | Description                           |
|------------------|---------------------------------------|
| `isbn13`         | ISBN-13 code (Primary Key)            |
| `isbn10`         | ISBN-10 code                          |
| `title`          | Title of the book                     |
| `subtitle`       | Subtitle of the book                  |
| `authors`        | Array of authors                      |
| `categories`     | Array of categories                   |
| `thumbnail`      | URL of the book's thumbnail image     |
| `description`    | Description of the book               |
| `published_year` | Year of publication                   |
| `average_rating` | Average rating of the book            |
| `num_pages`      | Number of pages in the book           |
| `ratings_count`  | Count of ratings                      |
