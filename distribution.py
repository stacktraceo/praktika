from pathlib import Path

from extremum_finder import process_file_only_with_distribution


def main():
    # функция для распредления
    distribution = process_file_only_with_distribution(Path("tm1_O1_frag001.mtx"))

    output_path = "distribution.txt"

    with open(output_path, 'w') as f:
        f.write(" ".join(map(str, distribution)) + "\n")


if __name__ == '__main__':
    main()