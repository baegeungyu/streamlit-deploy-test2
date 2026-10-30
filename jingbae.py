import streamlit as st
import random
st.title('jingbae world!!')


images = [
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT6CQpTnbP-l4Xj9Hy91o7x-s26ShlN0JSJHjkJ0bEvUw&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtVrS9APtoH9j6EYhyqbdyOEEc9TlEwrbaQEuuRBR_uQ&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTWRuUqVJ4V0PBuZRRR2cqYBXIfSTOBUZNaXJVUcBA1eA&s=10",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTDTw1kLUWoVh-MvdoPm9BzxU3zMQfUMt-60D5heR2SNA&s=10"
]

answer = st.chat_input("끼끼까까")


if answer:
    if "~" in answer:
        random_image = random.choice(images)
        st.image(random_image)
    else:
        st.write('특수 문자를 포함하세요')
