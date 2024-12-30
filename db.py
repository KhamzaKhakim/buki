import psycopg2
import json

conn = psycopg2.connect(
    dbname="postgres",
    user="",
    password="",
    host="localhost",
    port="5432"
)
cursor = conn.cursor()

with open('buki/tutors-final.json', 'r', encoding='utf-8') as file:
    tutors_data = json.load(file)

for tutor in tutors_data:
    rating = float(tutor['rating']) if tutor['rating'] is not None else 0.0
    reviewCount = int(tutor['reviewCount']) if tutor['reviewCount'] is not None else 0


    cursor.execute('''
    INSERT INTO tutors (name, subjects, degree, experience, city, price, can_work_online, short_description, rating, review_count)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ''', (
        tutor['name'],
        tutor['subjects'],  # Make sure 'subjects' is a list
        tutor['degree'],
        tutor['experience'],
        tutor['city'],
        tutor['price'],
        tutor['canWorkOnline'],  # Ensure this is a boolean
        tutor['shortDescription'],
        rating,
        reviewCount  # Convert review count to an integer
    ))

# Commit changes to the database
conn.commit()

# Verify the data by selecting all rows
cursor.execute('SELECT * FROM tutors')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()

print("Data inserted successfully!")
