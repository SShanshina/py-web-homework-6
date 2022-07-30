import asyncpg
from pprint import pprint


async def insert_people(pool: asyncpg.Pool, people):
    pprint(f'Загружаю в базу список {people}')
    query = f"INSERT INTO people (name, height, mass, hair_color, skin_color, eye_color, birth_year, gender," \
            f" homeworld, films, species, vehicles, starships, id) VALUES ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10, " \
            f"$11, $12, $13, $14)"
    async with pool.acquire() as connection:
        async with connection.transaction():
            await connection.executemany(query, people)


async def insert_db_session(people):
    pprint(f'Работаю со списком {people}')
    pool = await asyncpg.create_pool(
        'postgresql://asyncio_db_user:123@127.0.0.1:5432/asyncio_homework', min_size=20, max_size=20
    )
    await insert_people(pool, people)
    await pool.close()
