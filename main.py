from weather import load_data_from_csv, generate_daily_summary, generate_summary

def main():
    csv_file = "python-weather-project/tests/data/example_one.csv"
    weather_data = load_data_from_csv(csv_file)

    summary = generate_summary(weather_data)
    print("Weekly Summary: ")
    print(summary)

    daily_summary = generate_daily_summary(weather_data)
    print("Daily Summary: ")
    print(daily_summary)

if __name__ == "__main__":
    main()