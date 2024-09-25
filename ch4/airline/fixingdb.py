from flights.models import *
from django.db import connection

flights = Flight.objects.all()

def execute_sql(sql):
    with connection.cursor() as cursor:
        cursor.execute(sql)
        return cursor.fetchall()


# First, let's see the current structure of the flights_flight table
print("Table structure:")
print(execute_sql("PRAGMA table_info(flights_flight);"))

# Now, let's see what's in the table
print("\nCurrent entries in flights_flight:")
print(execute_sql("SELECT * FROM flights_flight;"))


# Let's delete all entries in the flights_flight table
with connection.cursor() as cursor:
    cursor.execute("DELETE FROM flights_flight;")
    print(f"\nDeleted {cursor.rowcount} rows from flights_flight.")

# Verify the deletion
print("\nRemaining entries in flights_flight:")
print(execute_sql("SELECT * FROM flights_flight;"))




try:
    for flight in flights:
        print(flight.__dict__)
except Exception as kms:
    print(f"An error occurred: {kms}")

try:
    for flight in flights:
        flight.delete()
        print("Flight deleted successfully")
except Flight.DoesNotExist:
    print("Flight with origin 'New York' does not exist")
except Exception as e:
    print(f"An error occurred: {e}")