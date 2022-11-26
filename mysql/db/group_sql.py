class Group():
    def __init__(self, cursor):
        self.cursor = cursor


    def _create_table(self):
        query = """
            CREATE TABLE if not exists student_group(
            id INTEGER PRIMARY KEY AUTO_INCREMENT, 
            name VARCHAR(50) NOT NULL, 
            start_date DATE NOT NULL, 
            finish_date DATE NOT NULL 
            );  
            """
        self.cursor.execute(query)

    def add_new_group(self, data):
        query = f"""
            INSERT INTO student_group(name, start_date, finish_date)
            VALUES('{data["name"]}', '{data["start"]}', '{data["finish"]}');
            """

        self.cursor.execute(query)



    def get_all_groups(self):
        query = f"""
            SELECT * FROM student_group;
        """
        self.cursor.execute(query)
        return self.cursor.fetchall()



    def get_group(self, id):
        query = f"""
        SELECT * FROM student_group WHERE id={id};
        """
        self.cursor.execute(query)
        return self.cursor.fetchone()
