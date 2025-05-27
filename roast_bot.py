from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Funny, clueless, overly kind responses
RESPONSES = [
    "Oh wow, {input}? That sounds... important. I don’t really get it, but I’m proud of you!",
    "You just said '{input}' and I’m already impressed. What a genius move!",
    "Honestly, I have no clue what '{input}' means, but it feels right.",
    "Wait… '{input}'? Should I be taking notes?!",
    "Hold on. Are you a wizard? Because '{input}' sounds like magic.",
    "'{input}'? Absolutely iconic. Not sure why. But yes!",
    "That’s… something! You go, superstar!",
    "If I had a nickel for every time someone said '{input}', I’d be rich in confusion!",
    "'{input}' might just be the best thing I’ve ever heard… probably.",
    "Wow, the courage it took to say '{input}'... I’m emotional."
]

@app.route("/", methods=["GET", "POST"])
def home():
    response = None
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        if user_input.strip():
            template = random.choice(RESPONSES)
            response = template.format(input=user_input)
        else:
            response = "Oops! You didn’t type anything, but I support your silence!"

    return render_template("index.html", response=response, user_input=user_input)

if __name__ == "__main__":
    app.run(debug=True)
