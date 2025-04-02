import streamlit as st

# Data storage
electronics = ["Samsung TV", "Hitachi AC"]
user_feedback = {
    "Samsung TV": {"Very Bad": 0, "Bad": 0, "Good": 0, "Very Good": 0},
    "Hitachi AC": {"Very Bad": 0, "Bad": 0, "Good": 0, "Very Good": 0}
}

# Admin credentials
ADMIN_ID = "data200"

# Streamlit UI
st.set_page_config(page_title="Electronics Feedback System", page_icon="📊", layout="centered")
st.title("📺 Electronics Feedback & Inventory System")

# Navigation Options
option = st.radio("Select an option:", ["Admin", "Customer"], horizontal=True)

if option == "Admin":
    st.subheader("🔑 Admin Login")
    admin_input = st.text_input("Enter Admin ID:", type="password")
    if st.button("Login"):
        if admin_input == ADMIN_ID:
            st.success("✅ Access Granted.")
            
            st.subheader("📊 Admin Dashboard")
            st.write("### Product Feedback:")
            for product, feedback in user_feedback.items():
                st.write(f"**{product}:** {feedback}")
            
            # Inventory Management
            st.write("### 🏷️ Inventory Management")
            new_product = st.text_input("Add New Product:")
            if st.button("Add Product"):
                if new_product and new_product not in electronics:
                    electronics.append(new_product)
                    user_feedback[new_product] = {"Very Bad": 0, "Bad": 0, "Good": 0, "Very Good": 0}
                    st.success(f"✅ '{new_product}' added to inventory.")
                else:
                    st.warning("⚠️ Product already exists or input is empty.")
            
            delete_product = st.selectbox("Select a Product to Delete:", electronics)
            if st.button("Delete Product"):
                if delete_product in electronics:
                    electronics.remove(delete_product)
                    del user_feedback[delete_product]
                    st.success(f"🗑️ '{delete_product}' removed from inventory.")
        else:
            st.error("❌ Incorrect Admin ID.")

elif option == "Customer":
    st.subheader("🛍️ Customer Feedback")
    st.write("### Choose a Product to Review")
    selected_product = st.selectbox("Select a Product:", electronics)
    
    st.subheader(f"💬 Feedback for {selected_product}")
    feedback_options = ["Very Bad", "Bad", "Good", "Very Good"]
    feedback = st.radio("Rate the Product:", feedback_options, index=2)
    if st.button("Submit Feedback"):
        user_feedback[selected_product][feedback] += 1
        st.success("🙏 Thank you for your feedback!")
