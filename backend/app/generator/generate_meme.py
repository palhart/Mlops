from app.generator.prompts import They_Dont_Know, Indifferent, Poor_Fix, Sad, Waiting, Is_Better, Pompous, No_Responsibility, Ineffective_Solution, Change_My_Mind, Accurate_Depiction, Equal, Stay_Away_From, Ruin, Scary, When_Not_Good
from app.generator.nlp.generate_answer import generate_output 
from app.generator.nlp.embedding import semantic_search
import json

def create_memes(user_input, meme_description):

    try:
        memes = [
            They_Dont_Know,
            Indifferent,
            Poor_Fix,
            Sad,
            Waiting,
            Is_Better,
            Pompous,
            No_Responsibility,
            Ineffective_Solution,
            Change_My_Mind,
            Accurate_Depiction,
            Equal,
            Stay_Away_From,
            Ruin,
            Scary,
            When_Not_Good,
        ]

        for meme in memes:
            if meme_description == meme.description:
                meme = eval(f"{meme.name}()")
                output = generate_output(instruction=meme.instruction, prompt=user_input)
                cleand_output = output.split("\n")

                json_output = json.loads(cleand_output[0])

                print(f'json_output: {json_output}')
                image_name = meme.create(json_output)

                context = {"meme": image_name}
                return context
        print("Meme type not found")
        context = {"meme": "error.png"}
        return context
    except Exception as e:
        print(e)
        context = {"meme": "error.png"}
        return context


def generate_meme(user_input):
    user_input = user_input.strip().replace("\r\n", ", ").replace(":", "-")

    try:
        names = [ 
            "sad",
            "this is not important to me",
            "waiting",
            "they don't know",
            "this is better than that",
            "poor fix",
            "two parties blaming eachother for something",
            "the solution was a poor way of doing it",
            "This is the way it is in my opinion",
            "accurate depiction",
            "something is the same as something else",
            "stay away from",
            "ruin",
            "scary",
            "when something is really bad",
        ]
        document_description = semantic_search(documents=names, meme_description=user_input)
        print(document_description)
        meme = create_memes(user_input, document_description)

    except Exception as e:
        print(e)
        meme = {"meme": "error.png"}
    
    return meme