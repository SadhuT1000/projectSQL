from typing import Any

import psycopg2


def create_database(database_name, params):
    """Создание БД"""
    conn = psycopg2.connect(dbname="postgres", **params)
    conn.autocommit = True
    cur = conn.cursor()

    cur.execute(f"DROP TABLE IF EXISTS {database_name}")
    cur.execute(f"CREATE TABLE {database_name}")

    conn.close()

    with conn.cursor() as cur:
        cur.execute(
            """CREATE TABLE employers (
                employer_id INTEGER PRIMARY KEY,
                employer_name text not null,
                employer_area TEXT not null,
                url TEXT,
                open_vacancies INTEGER)"""
        )

    with conn.cursor() as cur:
        cur.execute(
            """CREATE TABLE vacancies (
                vacancy_id INTEGER,
                vacancy_name VARCHAR,
                vacancy_area VARCHAR,
                salary INTEGER,
                employer_id INTEGER REFERENCES employers(employer_id),
                vacancy_url VARCHAR)"""
        )

    conn.commit()
    conn.close()


def save_data_to_database(
    data_employer: list[dict[str, Any]],
    data_vacancies: list[dict[str, Any]],
    database_name: str,
    params: dict,
):
    """Сохранение данных в БД"""

    conn = psycopg2.connect(dbname="database_name", **params)

    with conn.cursor() as cur:
        for employer in data_employer:
            cur.execute(
                """INSERT INTO employers (employer_id, employer_name, employer_area, url, open_vacancies) VAlUES (%, %, %, % ,%)""",
                (
                    employer["id"],
                    employer["name"],
                    employer["area"]["name"],
                    employer["alternate_url"],
                    employer["open_vacancies"],
                ),
            )

    with conn.cursor() as cur:
        for vacancy in data_vacancies:
            salary_from = (
                vacancy["salary"]["from"]
                if vacancy["salary"] and vacancy["salary"]["from"] is not None
                else 0
            )
            cur.execute(
                """INSERT INTO vacancies (vacancy_id, vacancy_name, vacancy_area, salary, employer_id, vacancy_url) VALUES (%, %, %, %, %, %)""",
                (
                    vacancy.get("id"),
                    vacancy["name"],
                    vacancy["area"]["name"],
                    salary_from,
                    vacancy["employer"]["id"],
                    vacancy["alternate_url"],
                ),
            )

    conn.commit()
    conn.close()
