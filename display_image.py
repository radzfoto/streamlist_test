import streamlit as st
from pathlib import Path
from PIL import Image

import socket

# Run from command line: streamlit run display_image.py

def find_image(image_directory: Path, filename: str) -> Path | None:
    image_path: Path = Path(filename)
    # Search for the image in the directory tree
    for filepath in image_directory.rglob(image_path.as_posix()):
        return filepath
    return None

def main():
    st.title("Image Viewer")

    server_name = socket.getfqdn()
    print("Machine: " + server_name)
    print("Home dir: " + (Path().home().as_posix()))

    # Directory where your images are stored
    image_directory: Path = Path().home() / "src" / "streamlit_test" / "images"

    # User input for filename
    filename = st.text_input("Enter the name of the image file")

    if filename:
        # Find the image in the directory
        image_path = find_image(image_directory, filename)

        if image_path and image_path.is_file():
            # Display the image
            image = Image.open(image_path.as_posix())
            st.image(image, caption=f"Displaying: {filename}")
        else:
            st.warning("Image not found. Please check the filename.")

        # Buttons for next or quit
        col1, col2 = st.columns(2)
        with col1:
            next = st.button("Next")
        with col2:
            quit = st.button("Quit")

        if next:
            # Just clear the current state and wait for new input
            st.experimental_rerun()

        if quit:
            # Stop the Streamlit server
            st.stop()

if __name__ == "__main__":
    main()
