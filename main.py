import streamlit as st
import requests

# Streamlit 웹앱의 제목 설정
st.title('Generation 3D Model - DEMO')

# 사용자로부터 이미지 업로드 받기
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'jpeg', 'png'])
if uploaded_file is not None:
    # 파일을 임시 디렉토리에 저장
    with open("temp_image.jpg", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Kaedim API에 요청을 보내기 위한 URL과 헤더 설정
    url = 'https://api.kaedim3d.com/image-to-3d'
    headers = {
        'Authorization': 'Bearer YOUR_API_KEY',  # 여기에 Kaedim API 키를 입력하세요.
        'Content-Type': 'application/json',
    }

    # 이미지 파일의 URL이 필요하므로, 여기서는 임시로 이미지를 호스팅할 수 있는 방법을 찾아야 합니다.
    # 예를 들어, 이미지를 public URL로 제공하는 서버에 업로드 후 그 URL을 사용해야 합니다.
    # 이 예제에서는 사용자가 직접 URL을 제공한다고 가정합니다.
    image_url = st.text_input('Enter the image URL:')

    # API 요청을 보내 생성된 3D 모델의 정보를 받아옵니다.
    response = requests.post(url, headers=headers, json={'image_url': image_url})
    if response.status_code == 200:
        # 생성된 3D 모델의 다운로드 링크를 표시
        model_data = response.json()
        st.write('Your 3D model is ready!')
        st.write(f"Model URL: {model_data['model_url']}")
    else:
        st.error("An error occurred while processing your request.")
