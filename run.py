# moved here, so src module is added to the PYTONPATH
import os
from src.api import app

app.run(debug=True, host=os.environ['HOST'], port=int(os.environ['PORT']))
