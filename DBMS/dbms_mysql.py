# dbms_mysql.py
import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "exampledb",
    charset = "utf8mb4",
    cursorclass =pymysql.cursors.DictCursor
)

# 커서 생성 => 커서를 통해 명령어 작성
cursor = conn.cursor()

# 명령어 실행
cursor.execute("SELECT DATABASE()")
# 한 번 호출에 하나의 Row를 가져올 때 사용
# print("현재 데이터베이스: ", cursor.fetchone())
print("현재 데이터베이스: ", type(cursor.fetchone()))
# print("현재 데이터베이스: ", cursor.fetchall())
# print("현재 데이터베이스: ", cursor.fetchmany(2))


# 연결 해제 함수
conn.close()