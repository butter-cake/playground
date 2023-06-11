from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def basic():
    return render_template("server.html", times=3, color="lightblue")  # Return the string 'Hello World!' as a response

@app.route('/play')
def play():
    return render_template("server.html", times=3, color="lightblue")

@app.route('/play/<int:num>')
def plays(num):
    return render_template("server.html", times=num, color="lightblue")

@app.route('/play/<int:num>/<string:color>')
def color(num, color):
    return render_template("server.html", times=num, color=color)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True, host="localhost", port=8000)    # Run the app in debug mode.

