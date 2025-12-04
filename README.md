# Data Engineering Project 1 — CSV to SQLite Import Pipeline

As an introduction, this project was based on my desire to learn about Data Engineering and asked ChatGPT to provide a brief and also review after I finished it. And this project is designed as **Project 1** in my Data Engineering portfolio. This project demonstrates a clean and structured Data Engineering simple ETL pipeline that ingests CSV data into a SQLite database using Python and Pandas.

---

## Overview
![Data Pipeline Architecture](https://miro.medium.com/v2/resize:fit:1400/1*KSWpdE7DEaw9jGxC2zNBPw.png)
The goal of this project is to:

- Load a CSV dataset into Python using Pandas  
- Parse and clean selected fields (e.g., `date_added` to datetime format)  
- Create a SQLite database with a structured table based on CSV columns
- Insert the cleaned data into the database

This project uses a Netflix Movies & TV Shows dataset that you can find [here](https://www.kaggle.com/datasets/ariyoomotade/netflix-data-cleaning-analysis-and-visualization).

**Tools Used:** Python, Pandas, SQLite  

---

## Prerequisites

Before running this project, make sure you have:

- Python 3 installed  
- Pandas library (`pip install pandas`)
- SQLite3 (built-in with Python)  
- CSV file placed inside the `data/` folder

---

## How to Run This Project
1. Clone the repo
   ```sh
   git clone https://github.com/mrayhannur/de-project1-etl-csv-to-sqlite.git
   ```
2. Run the `main` file
   ```sh
   python main.py
   ```
3. To reset the process, there is `clean_up` file that you can run
   ```sh
   python clean_up.py
   ```
   _Running this file will delete the db files inside the db folder that was created after running the main file._

## Database Result
If everything goes well, there will be a db folder with a .db file containing the data resulting from the ETL process. You can view the contents of this file by uploading it to the [following](https://sqliteviewer.app/) website.

![Database result](https://github.com/mrayhannur/de-project1-etl-csv-to-sqlite/blob/main/img/db_result.png)


## Lesson Learned
- I learned how to structure a data engineering project using an organized and scalable folder layout that follows industry best practices.
- I gained experience building a simple ETL pipeline by extracting data from a CSV file, transforming it with Python, and loading it into a SQLite database.
- I learned how to write a clear and effective README by referencing well-documented examples from other repositories.

## Future Improvements
- Add unit tests for transformation logic
- Replace SQLite with PostgreSQL
- Add logging to cloud or file output
- Containerize the project with Docker
