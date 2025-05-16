
import os

def save_df_to_csv(df, save_path='outputs/tranformed_weather_data.csv'):
    """
    Saves the given DataFrame as a CSV file to the specified path.
    
    Parameters:
        df : Cleaned DataFrame
        save_path : file path to save the csv file
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
