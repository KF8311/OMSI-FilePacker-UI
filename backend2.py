source_directory = '.'
output_zip_file = "packed_files.zip"
def read_omsi_path(input_path):
    global source_directory
    source_directory = input_path
    print(source_directory)

def read_zip_file_name(input_name):
    global output_zip_file
    input_name += ".zip"
    output_zip_file = input_name
    print(output_zip_file)


def read_missing_files_list_frontend(zip_name):
    print(f"Data received: {zip_name}")
    return zip_name

def read_missing_files(missing_files_list):
    missing_files = missing_files_list
    # file_paths = [each.strip() for each in missing_files if each.strip() != '']
    #print(f"Data received: {file_paths}")


