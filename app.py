import streamlit as st
from modules import run_assistant 

assistant = st.secrets.AI_uKnow


st.set_page_config(
    page_title = "AI_uKnow",
    page_icon = "🛸",
)

def main():
    st.title("Phrase EasyFix")
    user_input = st.chat_input("どんな状況で何を伝えたいか教えてください")

    temporary = st.empty()
    t = temporary.container()
    with t:
        st.write("翻訳してもらったり、自分の表現をチェックしてもらったり英会話中の咄嗟の確認に！")
        m1 = st.chat_message("user")
        a1 = st.chat_message("assistant")
        m2 = st.chat_message("user")
        a2 = st.chat_message("assistant")
        m3 = st.chat_message("user")
        a3 = st.chat_message("assistant")
        m1.write("フィッシュ&チップスの魚は何か聞きたい")
        a1.write("""
1. Could you tell me **what kind of fish** is typically used in Fish & Chips?
2. I'd like to know **which fish** is traditionally used in Fish & Chips.
3. I was wondering which **type of fish** is used for Fish & Chips?

""")
        m2.write("例：雛人形の由来を友達に教えてあげたい")
        a2.write("""
1. I'd like to share the **origin of** Hinaningyo with you! It's from a Japanese festival called Hinamatsuri.
2. Hinaningyo is **named after** a Japanese traditional festival called Hinamatsuri. Let me enlighten you about the origins of Hinaningyo.
3. It's **tied to** a traditional Japanese event known as Hinamatsuri.
""")
        m3.write("I want speak english very good!")
        a3.write("""
1. I **want to** speak English very well!
2. I **aim to** speak English fluently!
3. **My goal** is to become very good at speaking English!
""")

    if user_input:
        temporary.empty()
        run_assistant(assistant_id=assistant, txt=user_input)

if __name__ == "__main__":
    main()