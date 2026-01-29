import streamlit as st

#header
st.header("students records managment")
#tittle
st.title("welcome to student records managment system")
#subheader
st.subheader("manage student records efficently and effectively")
#horizontal line
st.markdown("------------------------------------")
st.text("this appliicaation allow you to perform crud operation on student records using a sql ")
st.write("hello tadla shasank")
st.write(12345)
st.write(2,3,4,5,6)
st.markdown("italic text")
st.markdown("item 1\n")
st.markdown("<h3 style=color:orange>mausambi</h3>",unsafe_allow_html=True)
st.markdown("<h4 style=color:green>green</h4>",unsafe_allow_html=True)
st.caption("this is capytiion student managment system")
st.code(""" 
def add(a,b):
     return a+b
     """,language='python'   )
st.latex(r''' a^2+b^3 = c^2''')
st.divider()
if st.button("click me"):
    st.write('button clicked')
    st.success("operation succesfull")
    st.balloons()
    st.snow()
else:
    st.write("button not clicked yet")
    st.error("CONNECTION ERROR")
name=st.text_input("enter your name")
if name =="":
    st.warning("name cannot be emoty")
elif not name.isalpha():
    st.error("invalid input,plesse enter a alphabets")
else:
    st.write(f"hello,{name}")
age=st.number_input("ente your age",min_value=1,max_value=100,step=1)
st.write("your age is",age)
address=st.text_area("enter your adress")
st.write("your adress is",address)
st.checkbox("i agree the term and coindition")
st.radio("select your gender",{"male",'female','others'})
country=st.selectbox("select your country",('india','dubai'))
st.write("your country is",country)
age=st.slider("select your age", 0,90,9)
st.write(f"you are{age} years old")
with st.form("my_form"):
    email = st.text_input("Enter your email")
    age = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
    submit = st.form_submit_button("Submit")

if submit:
    st.write("Email:", email, "Age:", age)
    st.success("Form submitted successfully")

#  FORM 2 
with st.form("login"):
    name = st.text_input("Enter your name")
    age2 = st.number_input("Enter your age", min_value=1, max_value=100, step=1)
    login = st.form_submit_button("Login")

if login:
    st.write("Name:", name, "Age:", age2)
    st.success("Login successful")

# --COLUMNS 
col1, col2, col3 = st.columns(3)

with col1:
    st.text("This is column 1")

with col2:
    st.text("This is column 2")

with col3:
    st.text("This is column 3")

# --
data = {
    "Name": ["Anurag", "Sumit", "Rohit"],
    "Age": [21, 22, 20],
    "Course": ["B.Tech", "M.Tech", "BBA"]
}

st.table(data)
st.sidebar.title('sidebar tittle')
option=st.sidebar.selectbox('SELECT AN OPTION',("OPTION1","OPTION 2",'OPTION3'))
st.sidebar.write('you selected',option)








