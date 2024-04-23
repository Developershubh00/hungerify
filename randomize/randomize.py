import streamlit as st
import random
import time

# Vegetarian Dishes
veg_dishes = [
    "Paneer Tikka", "Aloo Gobi", "Palak Paneer", "Vegetable Biryani",
    "Chana Masala", "Dal Makhani", "Baingan Bharta", "Veggie Korma",
    "Mushroom Masala", "Vegetable Pakoras"
]

# Non-Vegetarian Dishes
non_veg_dishes = [
    "Butter Chicken (Murgh Makhani)", "Chicken Tikka Masala", "Rogan Josh",
    "Lamb Biryani", "Tandoori Chicken", "Fish Curry (Machli Ka Salan)",
    "Chicken Korma", "Chicken Chettinad", "Mutton Curry (Mutton Rogan Josh)",
    "Chicken Biryani"
]

# Vegetarian Chinese Dishes
veg_chinese_dishes = [
    "Vegetable Manchurian", "Veg Hakka Noodles", "Gobi Manchurian",
    "Spring Rolls", "Veg Fried Rice", "Chilli Paneer", "Sweet Corn Soup",
    "Veg Manchow Soup", "American Chop Suey", "Schezwan Fried Rice"
]

# Non-Vegetarian Chinese Dishes
non_veg_chinese_dishes = [
    "Non-Veg Manchurian", "Non-Veg Hakka Noodles", "Chicken Spring Rolls",
    "Chicken Fried Rice", "Chilli Chicken"
]

# Beverages
beverages = [
    "Masala Chai", "Mango Lassi", "Fresh Lime Soda", "Rose Milk",
    "Jal Jeera", "Badam Milk", "Cold Coffee", "Nimbu Pani", "Coconut Water",
    "Chaas (Buttermilk)"
]

# Breads
breads = [
    "Naan", "Roti", "Paratha", "Kulcha", "Poori",
    "Chapati", "Bhatura", "Tandoori Roti", "Missi Roti",
    "Lachha Paratha"
]

def get_random_food(category):
    if category == "Vegetarian Dishes":
        return random.choice(veg_dishes)
    elif category == "Non-Vegetarian Dishes":
        return random.choice(non_veg_dishes)
    elif category == "Vegetarian Chinese Dishes":
        return random.choice(veg_chinese_dishes)
    elif category == "Non-Vegetarian Chinese Dishes":
        return random.choice(non_veg_chinese_dishes)
    elif category == "Beverages":
        return random.choice(beverages)
    elif category == "Breads":
        selected_dish = random.choice(veg_dishes + non_veg_dishes)
        return random.choice(breads)

def main():
    st.title("Hungerify")
    st.write("Hungerify is your AI-powered food recommendation system that helps you discover delicious dishes quickly and easily. Whether you're a corporation looking to streamline food choices for your employees or an individual seeking culinary inspiration, Hungerify has you covered!")
    st.write("- Personalized recommendations based on your dietary preferences.")
    st.write("- Wide range of options including vegetarian, non-vegetarian, Chinese cuisine, beverages, and breads.")
    st.write("- Quick and convenient solution for individuals and corporations alike.")
    st.write("- Reduce decision fatigue and enjoy your meals hassle-free with Hungerify.")

    with st.sidebar:
        st.header("Preferences")
        is_vegetarian = st.checkbox("Vegetarian")
        is_non_vegetarian = st.checkbox("Non-Vegetarian")
        is_chinese = st.checkbox("Include Chinese")
        include_beverage = st.checkbox("Include Beverages")
        include_bread = st.checkbox("Include Breads")

    randomize_button = st.button("Randomize")

    if randomize_button:
        st.write("Redirecting to the nearest outlet...")
        st.write("Please wait while we prepare your recommendation.")

        selected_categories = []
        if is_vegetarian:
            selected_categories.append("Vegetarian Dishes")
        if is_non_vegetarian:
            selected_categories.append("Non-Vegetarian Dishes")
        if is_chinese:
            selected_categories.extend(["Vegetarian Chinese Dishes", "Non-Vegetarian Chinese Dishes"])
        if include_beverage:
            selected_categories.append("Beverages")
        if include_bread:
            selected_categories.append("Breads")

        with st.spinner("Finding your random food..."):
            time.sleep(5)  # Simulating a delay for the loading animation

            for category in selected_categories:
                selected_food = get_random_food(category)
                st.success(f"Random {category}: {selected_food}")

if __name__ == "__main__":
    main()
