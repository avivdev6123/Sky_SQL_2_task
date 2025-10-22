from sqlalchemy import create_engine, text

QUERY_FLIGHT_BY_ID = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ID = :id"
QUERY_FLIGHT_BY_DATE = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.DAY = :day AND flights.MONTH = :month AND flights.YEAR = :year"
QUERY_DELAYED_FLIGHT_BY_AIRLINE = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE airlines.AIRLINE LIKE :airline AND flights.DEPARTURE_DELAY > 0"
QUERY_DELAYED_FLIGHT_BY_AIRPORT = "SELECT flights.*, airlines.airline, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id WHERE flights.ORIGIN_AIRPORT = :airport OR flights.DESTINATION_AIRPORT = :airport AND flights.DEPARTURE_DELAY > 0"
# Define the database URL
DATABASE_URL = "sqlite:///data/flights.sqlite3"

# Create the engine
engine = create_engine(DATABASE_URL)


def execute_query(query, params):
    """
    Execute an SQL query with the params provided in a dictionary,
    and returns a list of records (dictionary-like objects).
    If an exception was raised, print the error, and return an empty list.
    """
    try:
        with engine.connect() as connection:
            records = []
            data = connection.execute(text(query), params)
            for row in data:
                records.append(row)
        return records
    except Exception as e:
        print("Query error:", e)
        return []


def get_flight_by_id(flight_id):
    """
    Searches for flight details using flight ID.
    If the flight was found, returns a list with a single record.
    """
    params = {'id': flight_id}
    return execute_query(QUERY_FLIGHT_BY_ID, params or {})

def get_flights_by_date(day, month, year):
    """
        Searches for flight details matching the year, month and day.
        If the flight was found, returns a list with a single record.
        """
    params = {
        'day': day,
        'month': month,
        'year': year
    }
    return execute_query(QUERY_FLIGHT_BY_DATE, params or {})

def get_delayed_flights_by_airline(airline_name):
    """
        Searches for delayed flight details matching by the airline name.
        If the flight was found, returns a list with a single record.
        """
    params = {
        'airline': airline_name
    }
    return execute_query(QUERY_DELAYED_FLIGHT_BY_AIRLINE, params or {})

def get_delayed_flights_by_airport(airport):
    """
        Searches for delayed flight details matching by the airport name.
        If the flight was found, returns a list with a single record.
        """
    params = {
        'airport' : airport
    }
    return execute_query(QUERY_DELAYED_FLIGHT_BY_AIRPORT, params or {})