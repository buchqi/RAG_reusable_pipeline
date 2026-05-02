import os 

def load_documents(folder_path):
    documents = []
    # Check all files in the folder
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        # Ensure it's a file, not a sub-folder
        if os.path.isfile(file_path):
            print(f"\n--- Reading: {filename} ---")
            
            # Try opening and reading the file
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents.append({
                        "source": filename,
                        "text":content
                    })
            except Exception as e:
                print(f"Could not read {filename} (it might be a binary file or have a different encoding): {e}")
    return documents        
    