from pathlib import Path


def read_matrix(filepath: Path) -> list[list[float]]:
    rows = []
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append([float(x) for x in line.split()])
    return rows


def square_matrix(matrix: list[list[float]]) -> list[list[float]]:
    return [[x ** 2 for x in row] for row in matrix]


# ищет экстремум в каждом столбце
# возвращает массив индексов строк в которой найден экстремум и само значение являющиеся экстремумом
def find_extremums(matrix: list[list[float]]) -> tuple[list[int], list[float]]:
    num_cols = len(matrix[0])

    # инициализируем первую строчку, что бы было от чего отталкиваться
    extreme_row_index = [0] * num_cols
    extreme_value = list(matrix[0])

    # проходимся по остальным
    for row_idx in range(1, len(matrix)):
        for col in range(num_cols):
            if matrix[row_idx][col] < extreme_value[col]:
                extreme_value[col] = matrix[row_idx][col]
                extreme_row_index[col] = row_idx

    return extreme_row_index, extreme_value

# считаем сколько экстремумов нашли в каждой строке (idx) - количество экстремумов в строке
def count_by_row(extreme_row_index: list[int]) -> dict[int, int]:
    counts: dict[int, int] = {}
    for row_idx in extreme_row_index:
        counts[row_idx] = counts.get(row_idx, 0) + 1
    return counts

# приаодим матрицу в читаемый вид
def format_matrix(matrix: list[list[float]], fmt: str = ".4f") -> list[str]:
    lines = []
    for row in matrix:
        lines.append('\t'.join(f"{x:{fmt}}" for x in row))
    return lines


def process_file_only_with_distribution(filepath: Path) -> list[int]:
    original = read_matrix(filepath)

    # возводим в квадрат элементы
    squared = square_matrix(original)

    # находим экстремум в модифицированной мартрице
    # распределение в extreme_row_index
    extreme_row_index, extreme_value = find_extremums(squared)

    return extreme_row_index

# функция для одного файла
def process_file(filepath: Path, output_lines: list[str]) -> None:
    # читаем
    original = read_matrix(filepath)
    if not original:
        output_lines.append(f"File {filepath.name} is empty.")
        return

    num_rows = len(original)
    num_cols = len(original[0])

    # возводим в квадрат элементы
    squared = square_matrix(original)

    # находим экстремум в модифицированной мартрице
    # распределение в extreme_row_index
    extreme_row_index, extreme_value = find_extremums(squared)

    # считаем сколько экстремумов нашли в каждой строке (idx) - количество экстремумов в строке
    row_counts = count_by_row(extreme_row_index)

    output_lines.append("################################################################")
    output_lines.append(f"# File: {filepath.name}")
    output_lines.append("################################################################")

    output_lines.append(f"\n=== Original matrix ({num_rows} x {num_cols}) ===")
    output_lines.extend(format_matrix(original, ".2f"))

    output_lines.append(f"\n=== Matrix after squaring ===")
    output_lines.extend(format_matrix(squared, ".2f"))

    # экстремумы (столбец -> в какой строке экстремум -> значение, сам экстремум)
    output_lines.append("\n=== Extremums by column ===")
    output_lines.append("Column -> Row index (squared value)")
    for col in range(num_cols):
        orig_val = original[extreme_row_index[col]][col]
        output_lines.append(
            f"  col[{col}] -> row[{extreme_row_index[col]}] "
            f"= {extreme_value[col]:.2f} (original: {orig_val:.2f})"
        )

    # массив индексов строк в которых найден экстремум для столбца i
    # колво элементов массива равно кол-ву столбцов матрицы
    arr_str = ', '.join(str(i) for i in extreme_row_index)
    output_lines.append(f"\nResult array (row indices): [{arr_str}]")

    # распрделение по строкам (сколько экстремумов в строке)
    output_lines.append("\n=== Extremum count by row ===")
    for row_idx in sorted(row_counts):
        output_lines.append(
            f"  row[{row_idx}] : {row_counts[row_idx]} extremum(s)"
        )