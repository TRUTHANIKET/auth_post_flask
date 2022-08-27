from web import createapp
from flask_sqlalchemy import SQLAlchemy

app = createapp()

if __name__=='__main__':
    app.run(debug=True)

