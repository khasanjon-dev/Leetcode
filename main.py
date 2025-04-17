import random

import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="1",
    host="localhost",
    port="5445",
)
conn.autocommit = True
cursor = conn.cursor()

try:
    random_ids = random.sample(range(1, 10_000_001), 1000)

    for idx, user_id in enumerate(random_ids, start=1):
        print(f"\n👤 [{idx}/1000] user_id = {user_id}")

        for i in range(1, 101):
            suffix = f"_upd{i}"
            query = """
                UPDATE billing.users
                SET name = name || %s
                WHERE id = %s;
            """
            cursor.execute(query, (suffix, user_id))
            print(f"  → Update {i}/100 done")

    print("\n✅ 1000 ta userga 100 martalik real update yakunlandi!")

finally:
    cursor.close()
    conn.close()
