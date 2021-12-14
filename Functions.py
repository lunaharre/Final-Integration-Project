# Luna Harre
# WorldFacts - A quiz on how knowledgable one is on world facts
# References: Gapminder.org, w3schools.com, Alex Patterson
def quiz1(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 1)
    else:
        score_wrong(score, 1)


def quiz2(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 2)
    else:
        score_wrong(score, 2)


def quiz3(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 3)
    else:
        score_wrong(score, 3)


def quiz4(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 4)
    else:
        score_wrong(score, 4)


def quiz5(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 5)
    else:
        score_wrong(score, 5)


def quiz6(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 6)
    else:
        score_wrong(score, 6)


def quiz7(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 7)
    else:
        score_wrong(score, 7)


def quiz8(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 8)
    else:
        score_wrong(score, 8)


def quiz9(question, answer, correct, score):
    print(question)
    ina = input(answer)
    if ina == correct:
        score_correct(score, 9)
    else:
        score_wrong(score, 9)


def score_correct(score, increment):
    # multiples score by four
    var = score ** 4
# divides score by increment
    var += score / increment
    score = var // score
    score = score - 2
    if score == 1002:
        score = score * 2
    if score != 0 and score % 2 == 1:
        score = score + score
    while score % 4 == 2:
        score = score + 3

    text = "Your score is now: " + score + "Great job!"
    print(text)


def score_wrong(score, decrement):
    if score < 0:
        score -= decrement

    boy = False
    if not boy:
        score = score / 7

    x = range(decrement)
    for X in x:
        score -= 2
    text = "Your score is now: " + score + "Better luck on the next one!"
    print(text, score)
