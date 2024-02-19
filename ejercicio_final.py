import openai

openai.api_key = "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"
system_rol = '''Hace de cuenta que sos un analizador de sentimientos.
                yo te paso sentimientos y vos analizas el sentimiento de los mensajes
                y me das una respuesta con al menos 1 caracter y como maximo 4 caracteres
                SOLO RESPUESTAS NUMERICAS.donde -1 es negatividad maxima 0 es nautral y 1 es positvidad
                (podes responder solo con ints o floats)'''

mensajes = [{"role":"system","content":system_rol}]

class AnalizadorDeSentimientos:
    def analizar_sentimiento(self,polaridad):
        if polaridad > -0.6 and polaridad <= -0.3:
            return "\x1b[1;31m" + "negativo"
        elif polaridad > -0.3 and polaridad <= -0.1:
            return "\x1b[1;31m" + "algo negativo"
        elif polaridad == 0:
            return "\x1b[1;33m" + "neutral"
        elif polaridad >= 0.1 and polaridad <= 0.4:
            return  "\x1b[1;32m" + "algo positivo"   
        elif polaridad >= 0.4 and polaridad <= 0.9:
            return  "\x1b[1;32m" + "positivo"   
        elif polaridad > 0.9:
            return "\x1b[1;32m" + "muy positivo"
        else:
            return "\x1b[1;33m" + "MUY NEGATIVO" 

analizador = AnalizadorDeSentimientos()

while True:
    user_prompt = input("\x1b[1;33m"+ "\n decime algo: " + "\x1b[1;37m")
    mensajes.append({"role":"user","content":user_prompt})

    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = mensajes,
        max_tokens = 8
    )
    respuesta = completion.choices[0].message["content"]
    mensajes.append({"role":"assistant","content":respuesta})

    sentimiento = analizador.analizar_sentimiento(respuesta)    
    print(sentimiento)