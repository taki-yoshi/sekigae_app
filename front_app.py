import streamlit as st
import pandas as pd
import chardet
import requests

#######コメント
st.title('席替えアプリ')
st.write('')
seats_sum = st.number_input(label='座席数を入力',value=1)
# ファイルアップロードの設定
uploaded_file = st.file_uploader('生徒の希望座席ファイル(csvファイル)をアップロードしてください', type='csv')

if uploaded_file is not None:
    # エンコーディングの設定
    rawdata = uploaded_file.read()
    result = chardet.detect(rawdata)
    encoding = result['encoding']

    uploaded_file.seek(0)
    data = pd.read_csv(uploaded_file, encoding=encoding)
    st.write('')
    st.write('希望調査表')
    st.write(data)
    st.write('')

    if st.button('席替え開始'):
        student_info={}
        for index,row in data.iterrows():
            preference=[str(rank) for rank in row[1:]]
            student_info[row['name']]=preference
            
        students_info=[student_info]
        # st.write(students_info)
            

        url = 'https://sekigae-app.onrender.com/seats_changed/'
        response = requests.post(url, json={'students': students_info,'seats_sum':seats_sum})

        if response.status_code == 200:
                st.header('席替え結果')
                changedseats_data = response.json()
                # st.write(changedseats_data)
                # print((changedseats_data.items()))
                for seats,name in changedseats_data.get('changed_seats').items():
                     st.write(seats,":",name[0])
                
        else:
            st.error(f'席替えエラー:{response.text}')  # APIエラーの表示
        
