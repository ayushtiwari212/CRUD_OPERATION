import streamlit as st
from pathlib import Path
import os

st.set_page_config(page_title="CRUD File Manager", page_icon="📁")

st.title("📁 CRUD Operation File Manager")

# ------------------ Helper Function ------------------

def read_files_and_folders():
    p = Path(".")
    items = list(p.rglob("*"))
    return items


# ------------------ Sidebar Menu ------------------

menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create File",
        "Read File",
        "Update File",
        "Delete File",
        "Rename File",
        "Create Folder",
        "Delete Folder"
    ]
)

# ------------------ Show Files & Folders ------------------

st.subheader("📂 Existing Files & Folders")

items = read_files_and_folders()

if items:
    for index, file in enumerate(items):
        st.write(f"{index} - {file}")
else:
    st.info("No files or folders found.")


# ------------------ Create File ------------------

if menu == "Create File":

    st.header("📄 Create File")

    file_name = st.text_input("Enter file name")
    content = st.text_area("Enter file content")

    if st.button("Create File"):

        try:
            p = Path(file_name)

            if p.exists():
                st.warning("File already exists!")

            else:
                with open(file_name, "w") as file:
                    file.write(content)

                st.success("File created successfully!")

        except Exception as e:
            st.error(e)


# ------------------ Read File ------------------

elif menu == "Read File":

    st.header("📖 Read File")

    file_name = st.text_input("Enter file name to read")

    if st.button("Read File"):

        try:
            p = Path(file_name)

            if p.exists():

                with open(file_name, "r") as file:
                    data = file.read()

                st.text_area("File Content", data, height=300)

            else:
                st.error("File not found!")

        except Exception as e:
            st.error(e)


# ------------------ Update File ------------------

elif menu == "Update File":

    st.header("✏️ Update File")

    file_name = st.text_input("Enter file name")

    option = st.radio(
        "Choose update option",
        ["Overwrite Content", "Append Content"]
    )

    content = st.text_area("Enter new content")

    if st.button("Update File"):

        try:
            p = Path(file_name)

            if p.exists():

                if option == "Overwrite Content":

                    with open(file_name, "w") as file:
                        file.write(content)

                    st.success("File content overwritten successfully!")

                elif option == "Append Content":

                    with open(file_name, "a") as file:
                        file.write(content)

                    st.success("Content appended successfully!")

            else:
                st.error("File does not exist!")

        except Exception as e:
            st.error(e)


# ------------------ Delete File ------------------

elif menu == "Delete File":

    st.header("🗑️ Delete File")

    file_name = st.text_input("Enter file name")

    if st.button("Delete File"):

        try:
            p = Path(file_name)

            if p.exists():

                os.remove(p)

                st.success("File deleted successfully!")

            else:
                st.error("File not found!")

        except Exception as e:
            st.error(e)


# ------------------ Rename File ------------------

elif menu == "Rename File":

    st.header("📝 Rename File")

    old_name = st.text_input("Enter old file name")
    new_name = st.text_input("Enter new file name")

    if st.button("Rename File"):

        try:
            p = Path(old_name)

            if p.exists():

                p.rename(new_name)

                st.success("File renamed successfully!")

            else:
                st.error("File not found!")

        except Exception as e:
            st.error(e)


# ------------------ Create Folder ------------------

elif menu == "Create Folder":

    st.header("📁 Create Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Create Folder"):

        try:
            p = Path(folder_name)

            if p.exists():

                st.warning("Folder already exists!")

            else:

                p.mkdir()

                st.success("Folder created successfully!")

        except Exception as e:
            st.error(e)


# ------------------ Delete Folder ------------------

elif menu == "Delete Folder":

    st.header("❌ Delete Folder")

    folder_name = st.text_input("Enter folder name")

    if st.button("Delete Folder"):

        try:
            p = Path(folder_name)

            if p.exists():

                p.rmdir()

                st.success("Folder deleted successfully!")

            else:
                st.error("Folder not found!")

        except Exception as e:
            st.error(e)