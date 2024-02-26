import streamlit as st
from modules import run_assistant 

assistant = st.secrets.AI_uKnow

# #Initialize OpenAI client and set default assistant_id
# client = OpenAI(api_key=api)


def main():
    st.title("AI版　なんてuKnow?")
    user_input = st.chat_input("どんな状況で何を伝えたいか教えてください")

    temporary = st.empty()
    t = temporary.container()
    with t:
        m1 = st.chat_message("user")
        a1 = st.chat_message("assistant")
        m2 = st.chat_message("user")
        a2 = st.chat_message("assistant")
        m1.write("隣のお爺さんが毎晩遅くまで熱唱している")
        a1.write("""
1. The elderly man next door **sings loudly** until late at night every evening.
2. It seems the elderly gentleman next door **enjoys singing loudly** late into the night.
3. Have you noticed the late-night **singing** from the elderly man next door every night?

""")
        m2.write("例：雛人形の由来を友達に教えてあげたい")
        a2.write("""
1. I'd like to share the **origin of** Hinaningyo with you! It's from a Japanese festival called Hinamatsuri.
2. Hinaningyo is **named after** a Japanese traditional festival called Hinamatsuri. Let me enlighten you about the origins of Hinaningyo.
3. It's **tied to** a traditional Japanese event known as Hinamatsuri.
""")

    if user_input:
        temporary.empty()
        run_assistant(assistant_id=assistant, txt=user_input)

if __name__ == "__main__":
    main()