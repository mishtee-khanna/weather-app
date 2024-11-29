# Weather App

This is a simple Weather Application that displays the Air Quality Index (AQI) based on a user-provided ZIP code. The app fetches air quality data from the AirNow API and presents it in a graphical interface built with Python's `Tkinter` library.

## Features

- Accepts a ZIP code as input.
- Displays the air quality information including the city, AQI value, and air quality category.
- Changes background color based on the air quality category for better visualization:
  - **Good**: Green
  - **Moderate**: Yellow
  - **Unhealthy for Sensitive People**: Orange
  - **Unhealthy**: Red
  - **Very Unhealthy**: Purple
  - **Hazardous**: Maroon

## Requirements

To run this application, you need to have the following installed:

- Python 3.x
- `tkinter` (usually included with Python)
- `Pillow` (for image handling, though not currently utilized in this script)
- `requests` (for making API requests)

You can install the necessary Python packages using pip:

```bash
pip install pillow requests
```

## How to Run

1. Clone or download this repository to your local machine.
2. Ensure you have Python installed along with the required libraries.
3. Replace `"89C0897E-2BA1-4D11-94FA-0A0933AE9505"` with your own API key from [AirNow API](https://www.airnowapi.org/).
4. Run the script using the command:

```bash
python weather_app.py
```

5. Enter a valid ZIP code in the input box and click the **Lookup Zipcode** button.

## Files

- `weather_app.py`: The main application script.
- `taco1.ico`: An optional icon for the app (ensure the file is in the same directory as the script).

## Notes

- Ensure you have a stable internet connection as the app fetches data from the AirNow API.
- If the entered ZIP code is invalid or there is a network error, the app will display an error message.

## Future Improvements

- Add error handling to display more user-friendly error messages.
- Include additional weather details such as temperature, humidity, etc.
- Enhance the UI design and responsiveness.

## License

This project is licensed under the MIT License. Feel free to use and modify it as needed.

---

Enjoy using the Weather App!

