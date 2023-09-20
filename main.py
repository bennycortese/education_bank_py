import openai
import os
from dotenv import load_dotenv


def iterate_on_questions(textbook_text, previous_questions):
    openai.organization = "org-1EAYlJSwfnMNuS2Z6d6I4cNU"
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()
    prompt_messages = []
    prompt_messages.append({"role": "system", "content": "You are an instructor designing new course content."})
    prompt_messages.append({"role": "user",
                            "content": "I am going to feed you textbook data and I want you to read it without saying "
                                       "anything. Say yes if you understand"})
    for text_chunk in textbook_text:
        prompt_messages.append({"role": "user", "content": text_chunk})
    prompt_messages.append({"role": "user", "content": "Ok that is all the textbook data, say yes if you understand"})
    prompt_messages.append({"role": "user",
                            "content": "I am going to give you 5 sample multiple choice questions, I want you to "
                                       "identify which ones are too simplistic and don't require complex thought. "
                                       "Explain why they don't require much complex thought. Say "
                                       "yes if you understand"})
    prompt_messages.append({"role": "user",
                            "content": previous_questions})
    prompt_messages.append({"role": "user",
                            "content": "Ok, now that you understand why those were too simplistic, can you write me 5 "
                                       "new questions given the information from the textbook and using your "
                                       "knowledge of what is too simplistic. Avoid questions with answers which can "
                                       "be found "
                                       "directly in the text and prefer questions that require synthesis of that "
                                       "knowledge and critical thinking. "
                                       "Put them in a multiple choice format and then list the answers"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=prompt_messages
    )

    return completion.choices[0].message['content']


def iterate_on_questions_with_rating(textbook_text, previous_questions, rating):
    openai.organization = "org-1EAYlJSwfnMNuS2Z6d6I4cNU"
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()
    prompt_messages = []
    prompt_messages.append({"role": "system", "content": "You are an instructor designing new course content."})
    prompt_messages.append({"role": "user",
                            "content": "I am going to feed you textbook data and I want you to read it without saying "
                                       "anything. Say yes if you understand"})
    for text_chunk in textbook_text:
        prompt_messages.append({"role": "user", "content": text_chunk})
    prompt_messages.append({"role": "user", "content": "Ok that is all the textbook data, say yes if you understand"})
    prompt_messages.append({"role": "user",
                            "content": "I am going to give you 5 sample multiple choice questions, I want you to "
                                       "identify which ones are too simplistic and don't require complex thought. "
                                       "These are rated with this rating " + rating + ","
                                       "Explain why they don't require much complex thought. Say "
                                       "yes if you understand"})
    prompt_messages.append({"role": "user",
                            "content": previous_questions})
    prompt_messages.append({"role": "user",
                            "content": "Ok, now that you understand why those were too simplistic, can you write me 5 "
                                       "new questions given the information from the textbook and using your "
                                       "knowledge of what is too simplistic. Avoid questions with answers which can "
                                       "be found "
                                       "directly in the text and prefer questions that require synthesis of that "
                                       "knowledge and critical thinking. "
                                       "Put them in a multiple choice format and then list the answers"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=prompt_messages
    )

    return completion.choices[0].message['content']


def write_questions(textbook_text):
    # Use a breakpoint in the code line below to debug your script.
    openai.organization = "org-1EAYlJSwfnMNuS2Z6d6I4cNU"
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    openai.Model.list()
    prompt_messages = []
    prompt_messages.append({"role": "system", "content": "You are an instructor designing new course content."})
    prompt_messages.append({"role": "user",
                            "content": "I am going to feed you textbook data and I want you to read it without saying "
                                       "anything. Say yes if you understand"})
    for text_chunk in textbook_text:
        prompt_messages.append({"role": "user", "content": text_chunk})
    prompt_messages.append({"role": "user", "content": "Ok that is all the textbook data, say yes if you understand"})
    prompt_messages.append({"role": "user",
                            "content": "Write 5 questions from what you read that require a combination of critical "
                                       "thinking and synthesis. Avoid questions with answers which can be found "
                                       "directly in the text. Put them in a multiple choice format and then list "
                                       "the answers"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=prompt_messages
    )

    return completion.choices[0].message['content']


def textbook_scrape(textbook_file_name):
    f = open(textbook_file_name, "r", encoding="utf-8")
    line = f.read()
    n = 4096
    return [line[i:i + n] for i in range(0, len(line), n)]


def summary_extraction(textbook_text):
    text_arrays = []
    summarized_text = []
    for i in range(0, len(textbook_text), 3):
        text_arrays.append([textbook_text[i], textbook_text[i + 1], textbook_text[i + 2]])
    for text_array in text_arrays:
        summarized_text.append(summarize_text(text_array))
    return summarized_text


def summarize_text(textbook_text):
    openai.organization = "org-1EAYlJSwfnMNuS2Z6d6I4cNU"
    load_dotenv()
    openai.api_key = os.getenv("OPENAI_API_KEY")
    prompt_messages = []
    prompt_messages.append(
        {"role": "system", "content": "You are an intelligent reader who is good at summarizing text."})
    prompt_messages.append({"role": "user",
                            "content": "I am going to feed you textbook data and I want you to read it without saying anything. Say yes if you understand."})
    for text_chunk in textbook_text:
        prompt_messages.append({"role": "user", "content": text_chunk})
    prompt_messages.append({"role": "user", "content": "Ok that is all the textbook data, say yes if you understand"})
    prompt_messages.append({"role": "user",
                            "content": "Write a summary of no more than 300 words from that data, focusing on what seems to be the most important content for students' learning objectives to be maximized from those summaries"})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0301",
        messages=prompt_messages
    )
    return completion.choices[0].message['content']


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(textbook_scrape("ch1PrinciplesSysDesign.txt"))
    summaries = summary_extraction(textbook_scrape("ch1PrinciplesSysDesign.txt"))
    previous_questions = iterate_on_questions(summaries, iterate_on_questions(summaries, iterate_on_questions(summaries, write_questions(summaries))))
    print(previous_questions)
    rating = input("Please rate how these questions are from 1 to 10: ")
    rated_questions_1 = iterate_on_questions_with_rating(summaries, previous_questions, rating)
    print(rated_questions_1)

    # for line in textbook_scrape("ch1PrinciplesSysDesign.txt"):
    #    print(line)
    # textbook_scrape("ch1IntroGameTheory.txt")
    # textbook_scrape("w.txt")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
