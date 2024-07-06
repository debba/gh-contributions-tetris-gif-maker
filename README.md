# GitHub Contributions Tetris GIF Maker

This script generates an animated Tetris-style GIF based on a GitHub user's contributions for a specific year.

## Prerequisites

Make sure you have the following Python packages installed:

- `Pillow`
- `requests`
- `argparse`

You can install them using `pip`:

```sh
pip install -r requirements.txt
```

## Usage

- Clone the repository or download the main.py file.

- Run the script from the command line by providing the GitHub username and the year for which you want to fetch the contributions:

```sh
python main.py <username> <year>
```
For example:

```sh

python main.py debba 2024
```

The script will generate an animated GIF of the specified user's GitHub contributions for the specified year and save it in the images folder with the name github_tetris.gif.

It will generate a github_tetris.gif file in the images folder showing the daily contributions of the user debba for the year 2024 in Tetris style.

## Credits

This script was developed by debba.
