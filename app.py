import streamlit as st
from factorial import calculate_factorial

def main():
    #title 
    st.title("Factorial Calculator")

    number=st.number_input("Enter an interger number:", min_value = 0, max_value = 900, value =0, step = 1)

    button = st.button ("Calculate")

    if button:
        result = calculate_factorial(number)
        st.write(f"The factorial of {number} is {result}")

if __name__ == "__main__":
    main()
