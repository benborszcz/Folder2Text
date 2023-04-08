# Folder2Text

Folder2Text is a simple command line tool that combines all the text files in a specified folder and its subfolders into a single text file. It can also ignore files specified in a `.gitignore` file present in the folder.

## Installation

Before installing Folder2Text, make sure you have Python 3.6 or higher installed on your system. You can check your Python version by running `python --version` in your command prompt or terminal.

1. Clone the repository or download the source code:

   ```
   git clone https://github.com/benborszcz/folder2text.git
   ```

   Alternatively, download the zip file and extract it.

2. Change to the project directory:

   ```
   cd folder2text
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

4. Install the package:

   ```
   pip install -e .
   ```

5. Verify the installation by running `folder2text --help`. If everything is set up correctly, you should see the help text for the tool.

## Usage

To combine text files in a folder, simply run:

```
folder2text /path/to/folder output_file.txt
```

Or naviagate to the folder and run:
```
folder2text . output_file.txt
```

This will create a file named `output_file.txt` with the combined contents of all text files in the specified folder and its subfolders.

If you want to ignore files specified in a `.gitignore` file present in the folder, use the `--ignore-gitignored` flag:

```
folder2text /path/to/folder output_file.txt --ignore-gitignored
```

## License

This project is licensed under the MIT License.

## Contributing

Feel free to submit issues, feature requests, and pull requests!
