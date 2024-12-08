from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def calculate_bmi():
    bmi = None
    category = None
    if request.method == "POST":
    
        try:
            weight = float(request.form.get("weight"))
            height = float(request.form.get("height"))
            if height > 0 and weight > 0:
             
                bmi = round(weight / (height ** 2), 2)
               
                if bmi < 18.5:
                    category = "Underweight"
                elif 18.5 <= bmi < 24.9:
                    category = "Normal weight"
                elif 25 <= bmi < 29.9:
                    category = "Overweight"
                else:
                    category = "Obesity"
        except ValueError:
            bmi = "Invalid input"
            category = None
    return render_template("index.html", bmi=bmi, category=category)

if __name__ == "__main__":
    app.run(port=5000)