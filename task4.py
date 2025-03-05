import streamlit as st

# 🌟 Streamlit Page Config
st.set_page_config(page_title="Even or Odd Checker", page_icon="🔢")

# 🎯 Title
st.title("🔢 Even or Odd Checker")
st.write("Enter a number to check whether it's Even or Odd. 🚀")

# 📝 User Input: Number
num = st.text_input("🔹 Enter a number:")

# 🚀 Check Even or Odd
if st.button("🔍 Check"):
    if num.isdigit():
        num = int(num)
        if num % 2 == 0:
            st.success(f"✅ {num} is an Even number.")
        else:
            st.success(f"✅ {num} is an Odd number.")
    else:
        st.error("❌ Error: Please enter a valid number!")

# 📌 Footer
st.markdown("---")
st.caption("Powered by Streamlit 🚀 made by muqaddas | Happy Coding! 😃")
