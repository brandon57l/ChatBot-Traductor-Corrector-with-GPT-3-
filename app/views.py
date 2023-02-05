from django.shortcuts import render
from django.http import HttpResponse
import openai ,os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY", None)

def chat(request):
    chatbot_response = None

    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key
        user_input = request.POST.get('user_input')
        prompt = user_input

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150
        )
        chatbot_response = response["choices"][0]["text"]

    return render(request, "app/app.html", {"response":chatbot_response})

def trad(request):
    chatbot_response = None
    user_input = request.POST.get('user_input')
    langue = request.POST.get('langue')
    prompt =f"translate this text to {langue}: {user_input}"

    context = {"text":"","response":chatbot_response}

    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150
        )

        chatbot_response = response["choices"][0]["text"]
        context = {"text":user_input,"response":chatbot_response}

    return render(request, "app/trad.html", context)

def corrector(request):
    chatbot_response = None
    user_input = request.POST.get('user_input')
    prompt =f"Correct me the spelling, punctuation and grammatical error of this text in the same language, I want the return to be in a paragraph tag and for each changes i want the text to be in a span with the text color in skyblue and bold: {user_input}"

    context={"text":"", "response":chatbot_response}

    if api_key is not None and request.method == 'POST':
        openai.api_key = api_key

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.5,
            max_tokens=150
        )
        chatbot_response = response["choices"][0]["text"]
        print(f"\n \n \t {chatbot_response}")

        context={"text":user_input, "response":chatbot_response}

    return render(request, "app/corrector.html",context)