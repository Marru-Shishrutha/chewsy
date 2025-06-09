import streamlit as st
import random

# Sample recipe dataset (you can replace this with real data or API integration)
recipes = [
    {
        "title": "Grilled Veggie Bowl",
        "ingredients": ["broccoli", "carrots", "quinoa"],
        "diet": "vegan",
        "nutrition": "300 kcal | 12g protein | 8g fat"
    },
    {
        "title": "Chicken Salad",
        "ingredients": ["chicken", "lettuce", "tomatoes"],
        "diet": "high-protein",
        "nutrition": "400 kcal | 35g protein | 15g fat"
    },
    {
        "title": "Paneer Wrap",
        "ingredients": ["paneer", "capsicum", "tortilla"],
        "diet": "vegetarian",
        "nutrition": "420 kcal | 18g protein | 20g fat"
    }
]

def get_recommendations(preference, input_ingredient):
    matched = []
    for recipe in recipes:
        if preference.lower() in recipe['diet'] and input_ingredient.lower() in recipe['ingredients']:
            matched.append(recipe)
    if not matched:
        matched = [recipe for recipe in recipes if input_ingredient.lower() in recipe['ingredients']]
    return matched

# Streamlit UI
st.set_page_config(page_title="Chewsy - AI Food Assistant", page_icon="🥗")
st.title("🥗 Chewsy: Your AI-Powered Food Assistant")

st.markdown("""
Welcome to *Chewsy*! Get personalized meal suggestions based on your preferences 🍽
""")

# Input Section
col1, col2 = st.columns(2)
with col1:
    diet_pref = st.selectbox("Choose your dietary preference:", ["vegan", "vegetarian", "high-protein", "any"])
with col2:
    ingredient = st.text_input("Enter an ingredient you have:", "broccoli")

if st.button("Suggest Recipes"):
    results = get_recommendations(diet_pref, ingredient)
    if results:
        st.success(f"Found {len(results)} recipe(s) based on your input!")
        for r in results:
            st.subheader(r["title"])
            st.markdown(f"*Ingredients*: {', '.join(r['ingredients'])}")
            st.markdown(f"*Nutrition*: {r['nutrition']}")
            st.markdown("---")
    else:
        st.warning("No recipes found. Try another ingredient or preference!")

st.markdown("""
---
👨‍🍳 Built by the FoodFusionAI Team: Shishrutha, Pranthi, Vinay, Sharath, Revanth
""")