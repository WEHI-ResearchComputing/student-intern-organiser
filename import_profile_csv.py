import csv
import sqlite3
import sys
import zipfile
import shutil
import pandas as pd
"""
    Usage : python import_csv_from_redcap.py <csvfile> <zipfile>

    Usage : python import_csv_from_redcap.py TestStudentInternshi_DATA_LABELS_2023-06-27_1517.csv FilesReport_AllDataAllRecordsAnd_2023-06-27_1518.zip

"""

# db_directory = "./student_intern_data/"
# db_path = 'student_intern_data/student_intern_data.db'

def read_csv_file(csv_file_path):
    print(csv_file_path)
    df = pd.read_csv(csv_file_path)

    print(df)

    for index, row in df.iterrows():
        user_id = row[0]
        student_name = row[1]
        email = row[2]
        profile = row[3]



# def update_students_by_criteria(criteria, update_fields):
#     # Check if criteria and update_fields are not empty
#     if not criteria or not update_fields:
#         return "Criteria and update fields cannot be empty."

#     try:
#         conn = sqlite3.connect(db_path)
#         cursor = conn.cursor()

#         # Constructing the WHERE part of the SQL query from criteria
#         criteria_query_parts = [f"{key} = ?" for key in criteria.keys()]
#         criteria_query = " AND ".join(criteria_query_parts)

#         # Constructing the SET part of the SQL query from update_fields
#         update_query_parts = [f"{key} = ?" for key in update_fields.keys()]
#         update_query = ", ".join(update_query_parts)

#         # Constructing the complete SQL query
#         sql_query = f"UPDATE Students SET {update_query} WHERE {criteria_query}"

#         # Executing the query
#         cursor.execute(sql_query, list(update_fields.values()) + list(criteria.values()))
#         conn.commit()

#         if cursor.rowcount == 0:
#             print("No rows were updated. Please check your criteria.")
#             return
#         else:
#             print(f"Successfully updated {cursor.rowcount} row(s).")
#             return

#     except sqlite3.Error as e:
#         print(f"An error occurred: {e}")
#         return
#     finally:
#         if conn:
#             conn.close()

# def update_email(csv_path):
#     with open(csv_path, mode='r', encoding='utf-8') as file:
#         csv_reader = csv.reader(file)
#         # Skip the header
#         next(csv_reader, None)
#         # Read the data into a list of tuples
#         data_list = [(row[0], row[1], row[2]) for row in csv_reader]
    
#     for student_id, student_email, pic_name in data_list:
#         criteria = {"intern_id": student_id, "email": student_email}
#         update_fields = {"picture_path": db_directory + "attachments/profile_picture/" + pic_name}
#         update_students_by_criteria(criteria, update_fields)



