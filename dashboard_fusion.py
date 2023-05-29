import streamlit as st


def main():
    st.title("Simple Greeting App")

    name = st.text_input("Enter your name")
    button = st.button("Greet")

    if button:
        if name:
            st.write(f"Hello, {name}!")
        else:
            st.write("Please enter your name.")


if __name__ == "__main__":
    main()
