from flask_frozen import Freezer
from app import app

# Configure the freezer
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_REMOVE_EXTRA_FILES'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()
    print("✅ Site frozen successfully! Check the 'build' folder.")