"""
ingest_clean.py

Provides functions to ingest and clean weather data.

Functions:
- ingest(filepath): Reads a CSV file into a DataFrame.
- clean(df): Cleans the DataFrame by dropping nulls, filling missing values, standardizing date formats, and removing unwanted rows.
"""

from .base import pd, parser

def ingest(filepath):
    """ 
    Reads a CSV file from the given filepath and returns a dataFrame
     
    Parameters:
        filepath : Path to the CSV file.
    Returns:
        DataFrame : DataFrame containing the weather data."""
    df = pd.read_csv(filepath)
    return df

def clean(df):
    """
    Takes a data frame and do the following in the given order:
    
    
    1. Handle Missing Values
            - Drop rows where date is missing
            - Fill missing values in temperature, humidity, and wind speed columns with mean or median.
    2. Standardize date
    3. Add a New Column
            - Adds a 'temperature_fahrenheit' column.
    4. Filter Data
            - Removes rows with 'weather_condition' as 'unknown' or null.
    
    Parameters:
        df : DataFrame to be cleaned(weather data)
        
    Returns:
        df : Cleaned DataFrame
    """
    df = df.dropna(subset=["date"])
    df = df.copy() 

    df.loc[:, "temperature_celsius"] = df["temperature_celsius"].fillna(df["temperature_celsius"].mean()).round(1)
    df.loc[:, "humidity_percent"] = df["humidity_percent"].fillna(df["humidity_percent"].mean()).round(1)
    df.loc[:, "wind_speed_kph"] = df["wind_speed_kph"].fillna(df["wind_speed_kph"].median()).round(1)
    df.loc[:, "date"] = df["date"].apply(parser.parse).dt.date
    df.loc[:, "temperature_fahrenheit"] = (df["temperature_celsius"] * 9/5 + 32).round(1)
    df = df.loc[(df["weather_condition"].str.lower() != "unknown") & (~df["weather_condition"].isnull())]

    return df
 