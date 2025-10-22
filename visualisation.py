import matplotlib as mpl
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text
import pandas as pd

DATABASE_URL = "sqlite:///data/flights.sqlite3"

def percentage_of_delayed_flight_per_airline():
    QUERY = "SELECT flights.*, airlines.airline as AIRLINE_NAME, flights.ID as FLIGHT_ID, flights.DEPARTURE_DELAY as DELAY FROM flights JOIN airlines ON flights.airline = airlines.id"
    engine = create_engine(DATABASE_URL)
    df = pd.read_sql(QUERY, engine)
    df["is_delayed"] = df["DEPARTURE_DELAY"] > 0
    agg_data = df.groupby("AIRLINE_NAME").agg(
        total_flights=("FLIGHT_ID", "count"),
        delayed_flights=("is_delayed", "sum")
    )

    # aggregating flights table
    agg_data["delay_percentage"] = (agg_data["delayed_flights"] / agg_data["total_flights"]) * 100
    agg_data = agg_data.sort_values("delay_percentage", ascending=False)

    #plotting
    plt.figure(figsize=(10, 6))
    plt.bar(agg_data.index, agg_data["delay_percentage"])
    plt.xticks(rotation=45, ha='right')
    plt.title("Percentage of Delayed Flights per Airline")
    plt.ylabel("Delay Percentage (%)")
    plt.xlabel("Airline")
    plt.tight_layout()
    plt.show()

    return agg_data