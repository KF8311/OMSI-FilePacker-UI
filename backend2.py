def read_omsi_path(input_path):
    source_directory = input_path
    print(f"Data received: {input_path}")

def read_missing_files(missing_files_list):
    missing_files = missing_files_list
    file_paths = [each.strip() for each in missing_files if each.strip() != '']
    print(f"Data received: {file_paths}")