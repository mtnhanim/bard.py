# ERROR WITH THE CODE : TAKA NAI, TAI CHOLTESENA . 
import openai

#key validation
key = open("UNTOUCH/key.txt","r").read()
openai.api_key = key

model = 'gpt-3.5-turbo'
chat_history = []

while True:
    msg_content = input("You: ")

    if msg_content.lower() == "end":
        break

    else:
        chat_history.append({"role":"user","content":msg_content})
        response = openai.ChatCompletion.create(
            model = model,
            messages = chat_history
        )

        bot_reply_raw = response['choices'][0]['message']['content']
        bot_reply = bot_reply_raw.strip("\n").strip()

        print(f"ChatGPT: {bot_reply}")

        chat_history.append({"role":"assistant","content":bot_reply})


        #takar hishab

        total_token  = int(response['usage']['total_tokens'])
        spent_money = (total_token/1000)*0.002 

        print(f"\n({total_token} ta token gese ga, {spent_money} takar binimoye. sed, kanteci)")




