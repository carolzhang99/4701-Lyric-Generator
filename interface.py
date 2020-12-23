import os
import openai

openai.api_key = os.getenv('OPENAI_KEY')
genre = input("Enter your genre: ")
artist = input("Enter your artist: ")

# three methods call the gpt api, and fills in parameters based on the genre passed in
def gpt3(prompt, engine='davinci', response_length=64,
         temperature, top_p=1, frequency_penalty, presence_penalty,
         artist, genre, example, stop_seq=[]):

         if genre == "pop":
           temperature = 0.6
           frequency_penalty = 0.6
           presence_penalty = 0.2
         elif genre == "rap":
           temperature = 0.8
           frequency_penalty = 0.7
           presence_penalty = 0.4
         elif genre == "country":
           temperature = 0.5
           frequency_penalty = 0.5
           presence_penalty = 0.1

    response = openai.Completion.create(
        prompt= "generate lyrics for" + "artist:" + artist + "genre:" + genre,
        engine=engine,
        max_tokens=response_length,
        temperature=temperature,
        top_p=top_p,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        stop=stop_seq,
    )
    answer = response.choices[0]['text']
    new_prompt = prompt + start_text + answer + restart_text
    return answer, new_prompt

print(gpt())
