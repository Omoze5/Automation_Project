from flask import Flask,render_template, url_for, request

app = Flask(__name__)
@app.route('/')
def index():
        return render_template('index.html', show_form=False)


@app.route('/showform', methods = ["GET", "POST"])
def show_form():
    if request.method == "POST":
          morning_sales =[float(x) for x in request.form['morning'].split(',')]
          evening_sales =[float(x) for x in request.form['evening'].split(',')]


          Total_Sales = sum(morning_sales) + sum(evening_sales)


          return render_template ('index.html', show_form=True, Total_Sale = "The total sales for the day is ${}".format (Total_Sales))
    return render_template ('index.html', show_form=True)


@app.route('/showform1', methods = ["GET", "POST"])
def show_form1():
    if request.method == "POST":
          hourly_rate =float(request.form['rate'])
          hours_worked =float(request.form['hours'])


          Workers_Salary = hourly_rate * hours_worked


          return render_template ('index.html', show_form1=True, Salary = "The workers salary for the day is ${}".format (Workers_Salary))
    return render_template ('index.html', show_form1=True)



@app.route('/showform2', methods = ["GET", "POST"])
def show_form2():
    if request.method == "POST":
          Total_sales = [float(x) for x in request.form['sales'].split(',')]
          Total_cost = [float(x) for x in request.form['cost'].split(',')]


          Profit = sum(Total_sales) - sum(Total_cost)


          return render_template ('index.html', show_form2=True, profit = "The total profit made from this sales is ${}".format (Profit))
    return render_template ('index.html', show_form2=True)



@app.route('/showform3', methods = ["GET", "POST"])
def show_form3():
    if request.method == "POST":
          Shift_sales = [float(x) for x in request.form['shift_sales'].split(',')]


          Shift_tips = (2 / 100) * sum(Shift_sales)


          return render_template ('index.html', show_form3=True, Tips = "The tip for this shift is ${}".format (Shift_tips))
    return render_template ('index.html', show_form3=True)




@app.route('/showform4', methods = ["GET", "POST"])
def show_form4():
    if request.method == "POST":
          Morning = [float(x) for x in request.form['first_sales'].split(',')]
          Evening = [float(x) for x in request.form['second_sales'].split(',')]


          Morning_tip = (2 / 100) * sum(Morning)
          Evening_tip = (2 / 100) * sum(Evening)

          Total_tips = Morning_tip + Evening_tip


          return render_template ('index.html', show_form4=True, total_Tips = "The total tip for the day is ${}".format (Total_tips))
    return render_template ('index.html', show_form4=True)













if __name__ == "__main__":
    app.run(debug=True)
    