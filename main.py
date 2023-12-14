import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie

st.set_page_config(layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_coder1 = load_lottieurl("https://lottie.host/542a3048-f22d-42ba-b2ff-66cebe79aa2a/9o8eVnaUVt.json")
lottie_coder2 = load_lottieurl("https://lottie.host/4107a362-2e3f-461a-89c2-730631e8b0a2/1Gv8HGrDmB.json")
lottie_coder3 = load_lottieurl("https://lottie.host/6b69c3fe-e094-435a-8b5d-affd578c02a2/L3lYYqqt6D.json")
lottie_coder4 = load_lottieurl("https://lottie.host/3e61f2cc-8372-43b1-8ab3-2d120231b1da/yoItHKjRHc.json")



st.write("##")
st.title('ADINA')
st.write("Silahkan Kunjungi link dibawah ini https://adinaajha.github.io/memory/")
st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options =['About','project','Goal'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation= 'horizontal'
    )

if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            
            code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js" integrity="sha512-aNMyYYxdIxIaot0Y1/PLuEu3eipGCmsEUBrUq+7aVyPGMFH8z0eTP0tkqAvv34fzN6z+201d3T8HPb1svWSKHQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script>
        let container = document.querySelector('.container');
        for (var i = 0; i<=400; i++){
            let block = document.createElement('div');
            block.classList.add('block');
            container.appendChild(block);
        }

        let block =document.querySelectorAll('.block');
        let animation = anime.timeline({
            targets: block,
            easing: 'easeInOutExpo',
            loop: true,
            delay: anime.stagger(10, {start:50}),
        })

        animation
        .add({
            scale: 0,
            translateX: function(){
                return anime.random(360, 2100);
            },
            translateY: function(){
                return anime.random(360, -2100);
            },
            rotate: function(){
                return anime.random(-360, 360);
            },
            duration: function(){ return anime.random(500, 3000);}
        })
        .add({
            scale: 1,
            translateX: 0,
            translateY: 0,
            rotate: 0,
            duration: function(){return anime.random(500, 3000);}
        })
    </script>
    
</body>
</html>

  





'''
            st.code(code, language='javascript')
            st.json({
    'Nama': 'Adina',
    'Nim': '4229455768',
    'Prodi':'Rekayasa Perangkat Lunak',
    'Universitas':'STMIK IKMI kota cirebon',
    'Mahasiswa': [
        'Semester 1',
        'Semester 2',
        'Semester 3',
        'Semester 4',
    ],
})
            st.lottie(lottie_coder4)
            st_lottie(lottie_coder2)

        with col2:

            st_lottie(lottie_coder1)
            st_lottie(lottie_coder4)
            st.write('Perkenalkan Nama saya Adina')
            st.title('skill')
            st.subheader('javascript, and python')
    st.write("---")

if selected =="project":
    with st.container():
        col3, col4 = st.columns(2)
        with col3:
              st.json({
    'Nama': 'Adina',
    'Nim': '4229455768',
    'Prodi':'Rekayasa Perangkat Lunak',
    'Universitas':'STMIK IKMI kota cirebon',
    'Mahasiswa': [
        'Semester 1',
        'Semester 2',
        'Semester 3',
        'Semester 4',
    ],
})
        
        with col4:
            st_lottie(lottie_coder2)
    st.write("---")

if selected == 'Goal':

    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            code = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div class="container"></div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/animejs/3.2.2/anime.min.js" integrity="sha512-aNMyYYxdIxIaot0Y1/PLuEu3eipGCmsEUBrUq+7aVyPGMFH8z0eTP0tkqAvv34fzN6z+201d3T8HPb1svWSKHQ==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>
    <script>
        let container = document.querySelector('.container');
        for (var i = 0; i<=400; i++){
            let block = document.createElement('div');
            block.classList.add('block');
            container.appendChild(block);
        }

        let block =document.querySelectorAll('.block');
        let animation = anime.timeline({
            targets: block,
            easing: 'easeInOutExpo',
            loop: true,
            delay: anime.stagger(10, {start:50}),
        })

        animation
        .add({
            scale: 0,
            translateX: function(){
                return anime.random(360, 2100);
            },
            translateY: function(){
                return anime.random(360, -2100);
            },
            rotate: function(){
                return anime.random(-360, 360);
            },
            duration: function(){ return anime.random(500, 3000);}
        })
        .add({
            scale: 1,
            translateX: 0,
            translateY: 0,
            rotate: 0,
            duration: function(){return anime.random(500, 3000);}
        })
    </script>
    
</body>
</html>

  





'''
            st.code(code, language='javascript')

        with col6:
            st_lottie(lottie_coder4)
            st.json({
    'Nama': 'Adina',
    'Nim': '4229455768',
    'Prodi':'Rekayasa Perangkat Lunak',
    'Universitas':'STMIK IKMI kota cirebon',
    'Mahasiswa': [
        'Semester 1',
        'Semester 2',
        'Semester 3',
        'Semester 4',
    ],
})
    st.write("---")

if selected == 'Contact Page':
    st.header("Get in Touch! Via Mail Or Via github")
    st.write("adinaajha335@gmail.com")
    st.write(" https://adinaajha.github.io/memory/")
    st_lottie(lottie_coder4)
    st.write('---')

  





