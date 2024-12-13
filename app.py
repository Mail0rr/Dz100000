from flask import Flask, render_template, request

app = Flask(__name__)
filename = "poll.txt"


menu = [
    {
        "pizza": "Пепперони",
        "ingredients": "Протёртые томаты, моцарелла, салями, пикантные пепперони. Аллергены: злаки, лактоза.",
        "price": 305
    },
    {
        "pizza": "Сырная",
        "ingredients": "Моцарелла бейби, фета, пармезан, горгонзола, проволоне, моцарелла. Аллергены: глютен, лактоза.",
        "price": 280
    },
    {
        "pizza": "Маргарита",
        "ingredients": "Протёртые томаты, моцарелла, базилик. Аллергены: злаки, лактоза.",
        "price": 190
    },
    {
        "pizza": "Гавайская",
        "ingredients": "Курица, ананас, моцарелла, томатный соус. Аллергены: злаки, лактоза.",
        "price": 250
    },
    {
        "pizza": "Вегетарианская",
        "ingredients": "Цукини, баклажан, томаты черри, перец болгарский, моцарелла, томатный соус. Аллергены: злаки, лактоза.",
        "price": 220
    }
]


@app.route("/")
def index():
    return render_template("poll.html", menu=menu)


@app.post("/poll")
def poll():
    selected_pizza = request.form.get("pizza")
    if not selected_pizza:
        return "Вы не выбрали пиццу!", 400
    with open(filename, "a", encoding="utf-8") as out:
        out.write(selected_pizza + "\n")
    message = "Вы наш единственный клиент, для нас многое значит ваш выбор!"
    return render_template("thankyou.html", message=message)

@app.get("/result")
def result():
    with open(filename, "r", encoding="utf-8") as file:
        votes = file.read().splitlines()
    vote_count = {}
    for vote in votes:
        vote_count[vote] = vote_count.get(vote, 0) + 1
    return render_template("result.html", vote_count=vote_count)



if __name__ == '__main__':
    app.run(port=6060, debug=True)