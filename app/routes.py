from app.application import app


@app.route('/')
def index():
    return '<h1>Hello World! {}</h1>'.format(app.env)
