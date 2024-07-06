# GitHub Contributions Tetris GIF Maker

This script generates an animated Tetris-style GIF based on a GitHub user's contributions for a specific year.

[![@debba 2023 - sample](https://raw.githubusercontent.com/debba/gh-contributions-tetris-gif-maker/main/sample/tetris_debba_2023.gif)](https://www.github.com/debba)

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

## Docker Usage

- Create `docker/crontab` file  (You can start from `docker/crontab.example`)
- Create `upload_to_s3.py` (You can start from `upload_to_s3.example.py`)
- Create a docker build
```sh
docker build -t github-tetris-maker docker
```
- Execute ad docker container
```sh
docker run -d --name github-tetris-maker \
  -e AWS_ACCESS_KEY_ID=your_access_key_id \
  -e AWS_SECRET_ACCESS_KEY=your_secret_access_key \
  github-tetris-maker
```

You can show container logs with the following command:
```sh
docker logs -f github-tetris-maker
```


## Credits

This script was developed by debba.
