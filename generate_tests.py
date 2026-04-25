import random
from pathlib import Path

def write_matrix(filepath: Path, matrix: list[list[float]], fmt: str = ".2f"):
    with open(filepath, 'w') as f:
        for row in matrix:
            f.write('\t'.join(f"{x:{fmt}}" for x in row) + '\n')

def main():
    dir_path = Path("test_data")
    dir_path.mkdir(exist_ok=True)
    random.seed(42)

    write_matrix(dir_path / "test1_small.txt", [
        [ 5.5,  2.3,  8.1,  1.7],
        [ 3.2,  7.4,  4.6,  9.0],
        [ 6.8,  1.1,  3.9,  5.3]
    ])

    write_matrix(dir_path / "test2_negative.txt", [
        [-3.5,  10.2,   0.7,  -7.1,  15.3],
        [ 8.4,  -2.6,   5.9,   3.3,  -1.8],
        [ 1.2,   4.5, -12.3,   6.7,   9.1],
        [-5.1,   7.8,   3.4,  -9.2,   2.5]
    ])

    write_matrix(dir_path / "test3_close.txt", [
        [0.10, 0.20, 0.30],
        [0.11, 0.19, 0.31],
        [0.09, 0.21, 0.29]
    ])

    # большая 50x10
    big = [[random.uniform(-100, 100) for _ in range(10)] for _ in range(50)]
    write_matrix(dir_path / "test4_large.txt", big)

    print(f"Сгенерировано 4 тестовых файла в: {dir_path}")

if __name__ == '__main__':
    main()
