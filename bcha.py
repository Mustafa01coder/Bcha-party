import streamlit as st
import time

# Page Configuration
st.set_page_config(page_title="For My Bcha ❤️", page_icon="🌹", layout="centered")

# Custom CSS for Dark Theme & Centering
st.markdown("""
    <style>
    /* Full Page Black Background */
    .stApp {
        background-color: #000000 !important;
        color: #FFFFFF !important;
    }
    
    /* Center all content */
    .main-container {
        display: flex;
        flex-direction: column;
        align-items: center;
        text-align: center;
    }

    /* Titles and Headers in Red */
    h1, h3 {
        color: #ff4b4b !important;
        text-align: center;
        font-family: 'Georgia', serif;
    }

    /* Styling the Button */
    .stButton>button {
        width: 100%;
        border-radius: 20px;
        height: 3em;
        background-color: #ff4b4b;
        color: white;
        font-weight: bold;
        border: none;
    }
    
    .stButton>button:hover {
        background-color: #d32f2f;
        color: white;
    }

    /* Making sure normal text is white */
    p, span, label {
        color: #FFFFFF !important;
        text-align: center;
    }

    /* Formatting images */
    img {
        border-radius: 15px;
        border: 2px solid #333333;
        display: block;
        margin-left: auto;
        margin-right: auto;
    }

    /* Divider color */
    hr {
        border-top: 1px solid #333333 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Start Content Wrapper
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# 1. Header & Main Image
st.title("I'm Sorry, My Bcha... 😔❤️")

col_mid_1, col_mid_2, col_mid_3 = st.columns([1, 4, 1])
with col_mid_2:
    try:
        st.image("images/Main.jpeg", width=450, caption="I only want you, hamesha.")
    except:
        st.info("Bcha, yahan 'main.jpeg' honi thi. (Check images folder)")

st.write("---")

# 2. Heartfelt Message
st.markdown("""
### **Mery Dil Ki Bat**
Bcha mainy kl ki saari baatain bht bar read ki  hain or mjhy apni ghaltiyon ka ehsas hy. 
Mainy thumain 'zaleel' mehsoos karwaya or tumhari mental health ki qadar nahi ki.
medicines ly rahi ho or itne stress main ho, mjhy thumara sahara banna chehiyee tha.
""")

# 3. Promises Section (Aesthetic Info Box)
st.markdown("""
<div style="background-color: #1a1a1a; padding: 20px; border-radius: 15px; border: 1px solid #333333;">
    <h3 style="color: #ff4b4b; margin-bottom: 15px;">My Promises to You:</h3>
    <p style="text-align: left; margin-left: 20px;">✅ I will never let you feel disrespected again.</p>
    <p style="text-align: left; margin-left: 20px;">✅ I will trust you more than my insecurities.</p>
    <p style="text-align: left; margin-left: 20px;">✅ I will support you till the last breath of my life .</p>
    <p style="text-align: left; margin-left: 20px;">✅ I will be the man you first fell in love with.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")
with st.expander("Click to see what I've promised myself for us 🤍"):
    st.write("✅ **Your Health:** Thumara treatment or sukoon meri priority hoga.")
    st.write("✅ **Your Space:** Tumhein jitna time or space chahiye, main wait karoon ga.")
    st.write("✅ **Our Trust:** Purani baatein or kch bhi kabhi wapas nahi aayngy.")


# 4. The Decision Button
st.markdown("### Will you give our relation a one last chance? 🥺")

if 'forgiven' not in st.session_state:
    st.session_state.forgiven = False

col_b1, col_b2, col_b3 = st.columns([1, 2, 1])
with col_b2:
    if st.button("Yes, I Forgive You and Love You ❤️"):
        st.session_state.forgiven = True

# 5. Post-Forgiveness Gallery
if st.session_state.forgiven:
    st.balloons()
    st.snow()
    st.success("Thank you for not giving up on me! I love you infinity. 💋")
    
    st.markdown("### ❤️Mera Cute BCHA I Love You ❤️")
    
    g_col1, g_col2 = st.columns(2)
    
    with g_col1:
        try:
            st.image("images/1.jpeg", width=280, caption="Hamesha mery sath")
        except: st.write("🖼️ (Image 1 missing)")
        
        try:
            st.image("images/2.jpeg", width=280, caption="Your smile is my world")
        except: st.write("🖼️ (Image 2 missing)")

    with g_col2:
        try:
            st.image("images/3.jpeg", width=280, caption="Together Forever")
        except: st.write("🖼️ (Image 3 missing)")
        
        try:
            st.image("images/4.jpeg", width=280, caption="My Peace")
        except: st.write("🖼️ (Image 4 missing)")
            
    st.markdown("---")
    st.markdown("<h4 style='color: #ff4b4b;'>'Muhabbatt ka saboot sath rehna nhi, ik dosry ka sukoon banna hy.'</h4>", unsafe_allow_html=True)

st.write("---")
st.caption("Always Yours Babe. ❤️")


st.markdown('</div>', unsafe_allow_html=True)

