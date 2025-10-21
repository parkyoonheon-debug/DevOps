# dbms_mysql.py
import pymysql

# MySQL 서버에 연결
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "exampledb"
)

# 커서 생성 => 커서를 통해 명령어 작성
cursor = conn.cursor()

# 명령어 실행
sql1 = '''
INSERT INTO employees(id, name, DeptID, ManagerID)
VALUES(8, 'Kenneth', 8, 101);
'''
cursor.fetchone(sql1)
conn.commit()
print("데이터 삽입 완료")
# 연결 해제
conn.close()