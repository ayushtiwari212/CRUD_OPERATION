import streamlit as st
from pathlib import Path
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="File Manager",
    page_icon="🗂️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;700&family=Syne:wght@400;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

/* Dark industrial background */
.stApp {
    background-color: #0d0f14;
    color: #e8e6e0;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #13151c;
    border-right: 2px solid #2a2d38;
}
[data-testid="stSidebar"] * {
    color: #e8e6e0 !important;
}

/* Headings */
h1 { font-family: 'Syne', sans-serif; font-weight: 800; color: #f0c040 !important; letter-spacing: -1px; }
h2, h3 { font-family: 'Syne', sans-serif; font-weight: 700; color: #e8e6e0 !important; }

/* Buttons */
.stButton > button {
    background: #f0c040;
    color: #0d0f14;
    font-family: 'Syne', sans-serif;
    font-weight: 700;
    border: none;
    border-radius: 4px;
    padding: 0.5rem 1.5rem;
    transition: all 0.2s;
}
.stButton > button:hover {
    background: #ffd966;
    transform: translateY(-1px);
    box-shadow: 0 4px 16px rgba(240,192,64,0.3);
}

/* Input fields */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stSelectbox > div > div {
    background: #1a1d26 !important;
    color: #e8e6e0 !important;
    border: 1px solid #2a2d38 !important;
    border-radius: 4px !important;
    font-family: 'JetBrains Mono', monospace !important;
}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus {
    border-color: #f0c040 !important;
    box-shadow: 0 0 0 2px rgba(240,192,64,0.2) !important;
}

/* Radio buttons */
.stRadio > div { gap: 0.5rem; }
.stRadio label { color: #e8e6e0 !important; }

/* File explorer box */
.file-explorer {
    background: #1a1d26;
    border: 1px solid #2a2d38;
    border-radius: 6px;
    padding: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.82rem;
    max-height: 340px;
    overflow-y: auto;
    color: #a8c7fa;
}
.file-explorer .folder { color: #f0c040; }
.file-explorer .file   { color: #80cbc4; }

/* Status messages */
.success-box {
    background: #0f2a1a;
    border-left: 4px solid #4caf50;
    padding: 0.75rem 1rem;
    border-radius: 0 4px 4px 0;
    font-family: 'JetBrains Mono', monospace;
    color: #81c784;
    margin: 0.5rem 0;
}
.error-box {
    background: #2a0f0f;
    border-left: 4px solid #ef5350;
    padding: 0.75rem 1rem;
    border-radius: 0 4px 4px 0;
    font-family: 'JetBrains Mono', monospace;
    color: #e57373;
    margin: 0.5rem 0;
}
.info-box {
    background: #0f1a2a;
    border-left: 4px solid #42a5f5;
    padding: 0.75rem 1rem;
    border-radius: 0 4px 4px 0;
    font-family: 'JetBrains Mono', monospace;
    color: #90caf9;
    margin: 0.5rem 0;
}

/* Content display area */
.content-display {
    background: #1a1d26;
    border: 1px solid #2a2d38;
    border-radius: 6px;
    padding: 1.25rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    white-space: pre-wrap;
    color: #c8e6c9;
    min-height: 80px;
}

/* Divider */
hr { border-color: #2a2d38 !important; }

/* Label color fix */
label { color: #a0a4b0 !important; font-size: 0.82rem !important; letter-spacing: 0.05em; }
</style>
""", unsafe_allow_html=True)


# ── Helper: list files & folders ──────────────────────────────────────────────
def get_all_items():
    p = Path(".")
    return sorted(p.rglob("*"))


def render_explorer():
    items = get_all_items()
    if not items:
        return "<em style='color:#555'>No files or folders found.</em>"
    lines = []
    for item in items:
        depth = len(item.parts) - 1
        indent = "&nbsp;" * (depth * 4)
        if item.is_dir():
            lines.append(f'{indent}<span class="folder">📁 {item.name}/</span>')
        else:
            lines.append(f'{indent}<span class="file">📄 {item.name}</span>')
    return "\n".join(lines)


def msg(kind, text):
    css = {"success": "success-box", "error": "error-box", "info": "info-box"}
    icon = {"success": "✅", "error": "❌", "info": "ℹ️"}
    st.markdown(
        f'<div class="{css[kind]}">{icon[kind]}&nbsp; {text}</div>',
        unsafe_allow_html=True,
    )


# ── Sidebar navigation ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🗂️ File Manager")
    st.markdown("---")
    operation = st.radio(
        "SELECT OPERATION",
        options=[
            "📋 View All",
            "📝 Create File",
            "👁️ Read File",
            "✏️ Update File",
            "🗑️ Delete File",
            "🔤 Rename File",
            "📁 Create Folder",
            "🗑️ Delete Folder",
            "📄 Create File in Folder",
        ],
    )
    st.markdown("---")
    st.markdown(
        "<small style='color:#555;font-family:JetBrains Mono'>CRUD v1.0 · Streamlit</small>",
        unsafe_allow_html=True,
    )


# ── Main panel ────────────────────────────────────────────────────────────────
st.markdown("# File Manager")

# Always show explorer in an expander
with st.expander("🗂️  File Explorer", expanded=(operation == "📋 View All")):
    st.markdown(
        f'<div class="file-explorer">{render_explorer()}</div>',
        unsafe_allow_html=True,
    )
    if st.button("🔄 Refresh"):
        st.rerun()

st.markdown("---")

# ── Operations ────────────────────────────────────────────────────────────────

# 1. View All (already shown above)
if operation == "📋 View All":
    st.markdown("### All Files & Folders")
    st.info("Use the File Explorer panel above to browse your directory tree.")


# 2. Create File
elif operation == "📝 Create File":
    st.markdown("### Create New File")
    col1, col2 = st.columns([1, 2])
    with col1:
        file_name = st.text_input("File name", placeholder="e.g. notes.txt")
    with col2:
        content = st.text_area("File content", placeholder="Enter content here…", height=160)

    if st.button("Create File"):
        if not file_name.strip():
            msg("error", "Please enter a file name.")
        else:
            p = Path(file_name.strip())
            if p.exists():
                msg("error", f"'{file_name}' already exists.")
            else:
                try:
                    p.parent.mkdir(parents=True, exist_ok=True)
                    p.write_text(content)
                    msg("success", f"File '{file_name}' created successfully!")
                except Exception as e:
                    msg("error", str(e))


# 3. Read File
elif operation == "👁️ Read File":
    st.markdown("### Read File")
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")

    if st.button("Read File"):
        if not file_name.strip():
            msg("error", "Please enter a file name.")
        else:
            p = Path(file_name.strip())
            if not p.exists():
                msg("error", f"'{file_name}' not found.")
            elif p.is_dir():
                msg("error", f"'{file_name}' is a folder, not a file.")
            else:
                try:
                    content = p.read_text()
                    st.markdown("**File contents:**")
                    st.markdown(
                        f'<div class="content-display">{content if content else "<em>File is empty.</em>"}</div>',
                        unsafe_allow_html=True,
                    )
                except Exception as e:
                    msg("error", str(e))


# 4. Update File
elif operation == "✏️ Update File":
    st.markdown("### Update File")
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")
    update_mode = st.radio("Update mode", ["Overwrite", "Append"], horizontal=True)
    new_content = st.text_area("Content", placeholder="Enter content…", height=140)

    if st.button("Update File"):
        if not file_name.strip():
            msg("error", "Please enter a file name.")
        else:
            p = Path(file_name.strip())
            if not p.exists():
                msg("error", f"'{file_name}' does not exist.")
            else:
                try:
                    mode = "w" if update_mode == "Overwrite" else "a"
                    with open(p, mode) as f:
                        f.write(new_content)
                    msg("success", f"File '{file_name}' updated ({update_mode.lower()}).")
                except Exception as e:
                    msg("error", str(e))


# 5. Delete File
elif operation == "🗑️ Delete File":
    st.markdown("### Delete File")
    file_name = st.text_input("File name", placeholder="e.g. notes.txt")

    if st.button("Delete File", type="primary"):
        if not file_name.strip():
            msg("error", "Please enter a file name.")
        else:
            p = Path(file_name.strip())
            if not p.exists():
                msg("error", f"'{file_name}' not found.")
            elif p.is_dir():
                msg("error", "That's a folder. Use 'Delete Folder' instead.")
            else:
                try:
                    os.remove(p)
                    msg("success", f"File '{file_name}' deleted.")
                except Exception as e:
                    msg("error", str(e))


# 6. Rename File
elif operation == "🔤 Rename File":
    st.markdown("### Rename File")
    col1, col2 = st.columns(2)
    with col1:
        old_name = st.text_input("Current file name", placeholder="e.g. old.txt")
    with col2:
        new_name = st.text_input("New file name", placeholder="e.g. new.txt")

    if st.button("Rename File"):
        if not old_name.strip() or not new_name.strip():
            msg("error", "Please fill in both fields.")
        else:
            p = Path(old_name.strip())
            if not p.exists():
                msg("error", f"'{old_name}' not found.")
            else:
                try:
                    p.rename(new_name.strip())
                    msg("success", f"Renamed '{old_name}' → '{new_name}'.")
                except Exception as e:
                    msg("error", str(e))


# 7. Create Folder
elif operation == "📁 Create Folder":
    st.markdown("### Create Folder")
    folder_name = st.text_input("Folder name", placeholder="e.g. my_project")

    if st.button("Create Folder"):
        if not folder_name.strip():
            msg("error", "Please enter a folder name.")
        else:
            p = Path(folder_name.strip())
            if p.exists():
                msg("error", f"'{folder_name}' already exists.")
            else:
                try:
                    p.mkdir(parents=True)
                    msg("success", f"Folder '{folder_name}' created.")
                except Exception as e:
                    msg("error", str(e))


# 8. Delete Folder
elif operation == "🗑️ Delete Folder":
    st.markdown("### Delete Folder")
    folder_name = st.text_input("Folder name", placeholder="e.g. my_project")
    st.warning("⚠️ The folder must be empty before deletion.")

    if st.button("Delete Folder", type="primary"):
        if not folder_name.strip():
            msg("error", "Please enter a folder name.")
        else:
            p = Path(folder_name.strip())
            if not p.exists():
                msg("error", f"'{folder_name}' not found.")
            elif not p.is_dir():
                msg("error", f"'{folder_name}' is not a folder.")
            else:
                try:
                    p.rmdir()
                    msg("success", f"Folder '{folder_name}' deleted.")
                except OSError:
                    msg("error", "Folder is not empty. Remove files first.")
                except Exception as e:
                    msg("error", str(e))


# 9. Create File in Folder
elif operation == "📄 Create File in Folder":
    st.markdown("### Create File inside a Folder")
    col1, col2 = st.columns(2)
    with col1:
        folder_name = st.text_input("Folder name", placeholder="e.g. my_project")
    with col2:
        file_name = st.text_input("File name", placeholder="e.g. readme.txt")
    content = st.text_area("File content", placeholder="Enter content…", height=140)

    if st.button("Create File in Folder"):
        if not folder_name.strip() or not file_name.strip():
            msg("error", "Please fill in both folder and file names.")
        else:
            folder_p = Path(folder_name.strip())
            if not folder_p.exists():
                msg("error", f"Folder '{folder_name}' does not exist. Create it first.")
            else:
                file_p = folder_p / file_name.strip()
                if file_p.exists():
                    msg("error", f"'{file_p}' already exists.")
                else:
                    try:
                        file_p.write_text(content)
                        msg("success", f"File '{file_p}' created successfully!")
                    except Exception as e:
                        msg("error", str(e))