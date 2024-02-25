import streamlit as st

def create_top_navigation_bar():
    # Create a top navigation bar
    # st.header('This is a header with a divider', divider='rainbow')
    # url = "https://www.streamlit.io"
    # st.write("check out this [link](%s)" % url)
    # st.markdown("check out this [link](%s)" % url)

    st.markdown(
        """
        <style>
            .navbar {
                overflow: hidden;
                background-color: #333;
                position: fixed;
                top: 0;
                width: 100%; /* Set the width to 100% */
                height: 100px;
                margin-left: auto;
                margin-right: auto;
            }
            .navbar a {
                float: left;
                display: block;
                color: red; /* Change the color to red */
                text-align: center;
                padding: 14px 16px;
                text-decoration: none;
                font-size: 17px;
            }
            .navbar a:hover {
                background-color: #ddd;
                color: black;
            }
        </style>


        <div class="navbar">
            <a href="#home">Home</a>
            <a href="#about">About Us</a>
            <a href="#contact">Contact Information</a>
            <a href="#login">Login</a>
        </div>
        """,
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    create_top_navigation_bar()
