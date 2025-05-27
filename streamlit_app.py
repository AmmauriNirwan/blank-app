import streamlit as st

st.title("Maomao web gege ⚔️")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG-20250518-WA0011.jpg", width=200) 



st.title("Aplikasi Sederhana") 
st.header("Aplikasi Mengecek Nilai Genap/Ganjil") 
angka = st.number_input("Tulis sebuah Angka:", value=0, steps=1)

if (angka % 2) == 0: 
    st.write(f"{angka} adalah Bilangan Genap") 
else: 
    st.write(f"{angka} adalah Bilangan Ganjil") 
