from flask import Flask

app = Flask(__name__) #__name__ this is using the name of the folder (107)

@app.get("/")
def home():
    return "Hello from flask"

app.run(debug=True) # apply the changes on dthe code, live
