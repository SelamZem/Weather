from weather_pipeline.base import pd, parser
from weather_pipeline.ingest_clean import ingest, clean
from weather_pipeline.transform import save_df_to_csv
from weather_pipeline.top5 import save_txt

def main():
    # 1. Ingest raw data
    df = ingest("data/weather_data.csv")

    # 2. Clean the data
    cleaned_df = clean(df)

    # 3. Save cleaned data
    save_df_to_csv(cleaned_df)

    # 4. Generate report
    save_txt(cleaned_df)

if __name__ == "__main__":
    main()
