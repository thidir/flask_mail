from flask import Flask
app =  Flask(__name__)
details= [
    {
        'name':'james',
        'age':2,
        'location':'Ho'
    },
    {
        'name':'John',
        'age':20,
        'location': 'Accra'
    }
]
@app.get("/")
def home():
    return render_templates('index.html')
