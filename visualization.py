import matplotlib.pyplot as plt

def plot_weather_data(df, output_image='weather_visualization.png'):
    plt.figure(figsize=(10, 6))
    plt.plot(df['Date'], df['Temperature'], marker='o', label='Temperature')
    plt.plot(df['Date'], df['Humidity'], marker='s', label='Humidity')
    plt.title('Weather Data')
    plt.xlabel('Date')
    plt.ylabel('Values')
    plt.xticks(rotation=45)
    plt.legend()
    plt.tight_layout()
    plt.savefig(output_image)
    plt.close()
