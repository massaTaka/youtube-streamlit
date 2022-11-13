
import streamlit as st
import time

st.title('Streamlit 入門')

st.write('プレグレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  latest_iteration.text(f'Iteration {1+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'Done!!!!'

# st.dataframe(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#   np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#   columns=['lat', 'lon']
# )
# st.map(df)

# if st.checkbox('Show Image'):
#   img = Image.open('picture1.jpeg')
#   st.image(img, caption='study', use_column_width=True)
option = st.selectbox(
  'あなたが好きな数字を教えてください。',
  list(range(1, 11))
)
'あなたの好きな数字は、', option, 'です。'







left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
  right_column.write('ここは右カラムです')

expander1 = st.expander('問い合わせ1')
expander1.write('問い合わせ1の内容を書く')
expander2 = st.expander('問い合わせ2')
expander2.write('問い合わせ2の内容を書く')

# text = st.text_input('あなたの趣味を教えてください')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味：', text
# 'コンディション：', condition




