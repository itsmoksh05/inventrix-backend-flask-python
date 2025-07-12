import os
from dotenv import load_dotenv
from app import create_app

app = create_app()
load_dotenv()

print("Current Application Now in: ", os.getenv('FLASK_ENV'))

if __name__ == '__main__':
    app.run(debug=True)
