input_file_path = "pyproject.toml"
output_file_path = "requirements.txt"

with open(input_file_path, 'r') as input_file:
    with open(output_file_path, 'w') as output_file:
        for line in input_file:
            if '^' in line:
                library, version = map(str.strip, line.split('='))
                version = version.replace('^', '').replace('"', '')
                output_file.write(f'{library}=={version}\n')
