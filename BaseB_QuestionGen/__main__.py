import json
import random
# Fall 2019 CS10 Final Question 6 Exam Generation
def main():
    questions = [genQuestion() for i in range(5)]
    save = {"questions": questions}
    print(json.dumps(save))

    with open('output.txt', 'w') as outfile:
         json.dump(save, outfile)

def genQuestion():
    #chooses what variable B is
    first_b = random.choice([1,2])
    opperator1 = opperator_gen()
    opperator2 = opperator_gen()
    subx = sub_gen(10)
    suby = sub_gen(10)
    subz = sub_gen(10)
    if (first_b == 1):
        x = "B"
        if (2 == random.choice([2,3])):
            y = "B"
            z = "1"
        else:
            z = "B"
            y = "1"
    elif (first_b == 2):
        y = "B"
        if (1 ==random.choice([1,3])):
            x = "B"
            z = "1"
        else:
            z = "B"
            x = "1"
    answer = answer_gen(x,y,z, opperator1, opperator2)
    prompt = ("<b>What is " + x + subx + opperator1 + "("  + y + suby + opperator2 + z + subz + ") in base B? <b>" )
    return {"prompt":prompt, "answer": answer}


def answer_gen(x,y,z, opperator1, opperator2):
    if (x == "B"):
        x = 10
    else:
        x = 1
    if (y == "B"):
        y = 10
    else:
        y = 1
    if (z == "B"):
        z = 10
    else:
        z = 1

    if (opperator2 == "-"):
        inner = y - z
    elif (opperator2 == "+"):
        inner = y + z
    elif (opperator2 == "*"):
        inner = y * z
    if (opperator1 == "-"):
        return x - inner
    elif (opperator1 == "+"):
        return x + inner
    elif (opperator1 == "*"):
        return x * inner
def sub_gen(x):
    return "<sub>" + str(x) + "<sub>"

def opperator_gen():
    return random.choice(["-","+","*"])



if __name__ == "__main__":
    main()
