
import os
from .base import pd
def save_txt(df, save_path='outputs/top5_average.txt'):
    """
    saves the top 5 cities with the highest average temperature in a text file
    
    Parameters:
        df : Cleaned DataFrame
        save_path : file path to save the txt file
    """
    top_five = df.groupby("city")["temperature_celsius"].mean().round(1).sort_values(ascending=False).head(5)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    top_five.to_csv(save_path, sep='|', index=True)
    
