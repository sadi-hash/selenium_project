class Student():
        def __init__(self, cursor):
            self.cursor = cursor


        def create_table(self):
            query = """
            CREATE TABLE IF NOT EXISTS student(
                id INTEGER PRIMARY KEY AUTO_INCREMENT,
                first_name VARCHAR(50) NOT NULL,
                last_name VARCHAR(60) NOT NULL,
                email VARCHAR(60) NOT NULL UNIQUE,
                group_id INTEGER NOT NULL,
                FOREIGN KEY(group_id) REFERENCES student_group(id)
            );
            """
            self.cursor.execute(query)


        def add_new_student(self, data):
            query = f"""
            INSERT INTO student(first_name, last_name, email, group_id)
            VALUES('{data["first_name"]}','{data["last_name"]}',
            '{data["email"]}','{data["group_id"]}'
            );
        """
            self.cursor.execute(query)

        def get_all_students(self):
            query = f"""
            SELECT * FROM student;
        """   
            self.cursor.execute(query)
            return self.cursor.fetchall()


        def get_students_by_group(self, group_id):
            query = f"""
            SELECT * FROM student WHERE group_id = {group_id};
        """
            self.cursor.execute(query)
            return self.cursor.fetchall()
        

        def delete_student(self, student_id):
            query = f"""
            DELETE FROM student WHERE id={student_id}
        """
            self.cursor.execute(query)

