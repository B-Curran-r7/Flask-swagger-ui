# My Flask App

This project is a simple Flask application that serves a Swagger UI interface. It includes all necessary static files and templates to display the Swagger documentation.

## Project Structure

```
my-flask-app
├── static
│   ├── swagger-ui.css
│   ├── index.css
│   ├── favicon-32x32.png
│   ├── favicon-16x16.png
│   ├── swagger-ui-bundle.js
│   ├── swagger-ui-standalone-preset.js
│   └── swagger-initializer.js
├── templates
│   └── index.html
├── app.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd my-flask-app
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Flask application, execute the following command:
```
python app.py
```

The application will be available at `http://127.0.0.1:5000`.

## Usage

Navigate to the root URL in your web browser to view the Swagger UI.

## License

This project is licensed under the MIT License.