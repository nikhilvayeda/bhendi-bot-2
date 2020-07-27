

def RandomReply(message):

    if message == "hi":
        return "Hello!"

    elif message.find('ooo') != -1:
        return "Bhendi, bhendi!"

    elif message == "hello":
        return "Hi!"

    elif message == "fuck haters":
        return "Ab Saiman ki baari hai"

    elif message == "yalgaar hoe":
        return "Hoes mad :flushed:"

    elif message in ["carry tera baap hai", "carry sabka baap hai", "curry bhoi tera baap hai",
    "curry tera baap hai", "keri tera baap hai"] :
        return "Ok mom"

    elif message == "six":
        return "Teri shaadi fix :joy:"

    elif message == "pencil":
        return "Teri shaadi cancel :joy:"

    elif message == "ok mom":
        return "Wait thats illegal"

    elif message == "i wanna kill myself":
        return "**Dont do it you have more to accomplish suicide help line India 091529 87821**"

    elif message == "uh oh":
        return "Stinky"

    elif message == "general kenobi":
        return "**Hello there - Bhendi Bot v2.0 by Monke - General Kenobi**"

    elif message == "monke":
        return "Wholesome :hugging:"

    elif message[:7] == "=repeat":
        if len(message[7:]) > 0:
            return message[7:]

    else: return None



