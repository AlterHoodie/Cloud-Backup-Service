import streamlit as st
import json
import os

# Define the folder containing the log files
log_folder_path = r'C:\GIT\CC\CC_PRO\data\backups\History'

def main():
    st.title("Log Viewer")

    # List all files in the folder that have a '.log' extension
    try:
        log_files = [file for file in os.listdir(log_folder_path) if file.endswith('.log')]
    except Exception as e:
        st.error(f"Failed to read the directory: {e}")
        return

    # Dropdown to select a file
    selected_file = st.selectbox("Select a log file", log_files)

    if selected_file:
        # Construct the full path to the file
        full_file_path = os.path.join(log_folder_path, selected_file)

        # Read and process the file
        try:
            with open(full_file_path, 'r', encoding='utf-8-sig') as file:
                content = file.readlines()

            data = []
            for line in content[1:]:  # Skip the first line
                if line.strip():  # Ensure the line isn't empty
                    try:
                        log_entry = json.loads(line)
                        data.append(log_entry)
                    except json.JSONDecodeError as e:
                        st.error(f"Error parsing JSON in the following line: {line}")
                        st.error(f"Error message: {e}")
                        continue
                else:
                    st.warning("Skipped an empty line.")
            
            if data:  # Only display data if non-empty
                st.write("Log Records:")
                for record in data:
                    st.json(record)
        except Exception as e:
            st.error(f"Failed to open or read the file: {e}")

if __name__ == "__main__":
    main()
