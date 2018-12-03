from app import  app
@app.route('/')
@app.route('/index')
def index():
    return "hell0, World!"

