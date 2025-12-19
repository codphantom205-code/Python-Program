def merge_files(file1, file2, output_file):
    try:
        with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as out:
            out.write(f1.read() + "\n" + f2.read())
        print(f"Files merged into {output_file}")
    except Exception as e:
        print(f"Error: {e}")

merge_files('file1.txt', 'file2.txt', 'file3.txt')