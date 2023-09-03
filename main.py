import openai
import os
from dotenv import load_dotenv

def print_hi(textbook_text):
    # Use a breakpoint in the code line below to debug your script.
    openai.organization = "org-1EAYlJSwfnMNuS2Z6d6I4cNU"
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()
    prompt_messages = []
    prompt_messages.append({"role": "system", "content": "You are an instructor designing new course content."})
    prompt_messages.append({"role": "user", "content": "I am going to feed you textbook data and I want you to read it without saying anything. Say yes if you understand"})
    for text_chunk in textbook_text:
        prompt_messages.append({"role": "user", "content": text_chunk})
    prompt_messages.append({"role": "user", "content": "Ok that is all the textbook data, say yes if you understand"})
    prompt_messages.append({"role": "user", "content": "Write 5 questions from what you read that require a combination of critical thinking and synthesis, put them in a multiple choice format and then list the answers"})
    completion = openai.ChatCompletion.create(
        model="gpt-4-32k",
        messages=prompt_messages
    )

    #{"role": "system", "content": "You are an instructor designing new course content."},
            #{"role": "user", "content": "I am going to feed you textbook data and I want you to read it without saying anything. Say yes if you understand"},
            #{"role": "user", "content": textbook_text},
            #{"role": "user", "content": "Ok that is all the textbook data, say yes if you understand"},
            #{"role": "user", "content": "Write 5 questions from what you read that require a combination of critical thinking and synthesis, put them in a multiple choice format and then list the answers"}
    print(completion.choices[0].message)


def textbook_scrape(textbook_file_name):
    f = open(textbook_file_name, "r", encoding="utf-8")
    line = f.read()
    n = 4096
    return [line[i:i + n] for i in range(0, len(line), n)]
    return f.read()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi(textbook_scrape("ch1PrinciplesSysDesign.txt"))
    #for line in textbook_scrape("ch1PrinciplesSysDesign.txt"):
    #    print(line)
    #textbook_scrape("ch1IntroGameTheory.txt")
    #textbook_scrape("w.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
