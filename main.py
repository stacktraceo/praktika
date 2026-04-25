import sys
from pathlib import Path

from extremum_finder import process_file


def main():
    dir_path = Path(sys.argv[1])
    if not dir_path.is_dir():
        print(f"'{dir_path}' is not a directory", file=sys.stderr)
        sys.exit(1)

    txt_files = sorted(
        p for p in dir_path.iterdir()
        if (p.suffix == '.txt' or p.suffix == '.mtx') and 'result' not in p.name
    )

    if not txt_files:
        print("No .txt or .mtx files found in directory.")
        return

    output_lines: list[str] = []

    for i, filepath in enumerate(txt_files):
        if i > 0:
            output_lines.append("\n")
        process_file(filepath, output_lines)

    output_path = dir_path / "batch_result.txt"
    with open(output_path, 'w') as f:
        f.write('\n'.join(output_lines) + '\n')

    print(f"Files processed: {len(txt_files)}")
    print(f"Result: {output_path}")


if __name__ == '__main__':
    main()