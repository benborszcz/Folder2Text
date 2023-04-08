import os
import magic
import argparse
import pathspec

def is_text_file(file_path):
    magic_obj = magic.Magic()
    file_type = magic_obj.from_file(file_path)
    return "text" in file_type

def read_gitignore(folder_path):
    gitignore_path = os.path.join(folder_path, ".gitignore")
    if os.path.exists(gitignore_path):
        with open(gitignore_path, "r") as gitignore_file:
            return gitignore_file.read().splitlines()
    return []

def read_and_combine_files(folder_path, output_file, ignore_gitignored=False):
    gitignore_patterns = read_gitignore(folder_path) if ignore_gitignored else []
    spec = pathspec.PathSpec.from_lines(pathspec.patterns.GitWildMatchPattern, gitignore_patterns)

    with open(output_file, 'w') as outfile:
        for root, _, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)

                # Check if the current file is the output file
                if file_path == os.path.join(root, output_file):
                    print(f"{file_path} Skipped")
                    continue

                if ".git" in file_path:
                    print(f"{file_path} Skipped")
                    continue

                if ignore_gitignored:
                    if spec.match_file(file_path) or file in {".gitignore", ".gcloudignore"}:
                        print(f"{file_path} Skipped")
                        continue

                if not is_text_file(file_path):
                    print(f"{file_path} Skipped")
                    continue

                relative_path = os.path.relpath(file_path, folder_path)
                outfile.write(f"{relative_path}\n")
                outfile.write("----------\n")
                
                with open(file_path, 'r', errors='ignore') as infile:
                    contents = infile.read()
                    print(f"{file_path} Scanned")
                    outfile.write(f"{contents}\n")
                
                outfile.write("----------\n\n")

def main():
    parser = argparse.ArgumentParser(description="Combine text files in a folder.")
    parser.add_argument("folder_path", help="Path to the folder containing the files.")
    parser.add_argument("output_file", help="Name of the output file.")
    parser.add_argument("--ignore-gitignored", action="store_true", help="Ignore files specified in .gitignore")
    args = parser.parse_args()

    read_and_combine_files(args.folder_path, args.output_file, args.ignore_gitignored)
    print(f"Files combined and saved to {args.output_file}")

if __name__ == "__main__":
    main()