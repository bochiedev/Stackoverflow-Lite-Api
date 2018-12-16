from stackoverflow import create_app
from stackoverflow.config import Config

app = create_app(Config)

if __name__ == "__main__":
    app.run(debug=True)
