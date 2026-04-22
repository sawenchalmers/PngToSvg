import sys
import subprocess
import tempfile
from pathlib import Path
from PIL import Image

INPUT_EXTENSIONS = [".png", ".jpg", ".jpeg"]
POTRACE_PATH = Path(__file__).parent / "potrace-1.16.win64" / "potrace.exe"

def convert_with_potrace(input_file: Path, output_file: Path):
    if output_file.exists():
        return

    # Convert to black/white (required by Potrace)
    with Image.open(input_file) as img:
        bw = img.convert("L").point(lambda x: 0 if x < 128 else 255, "1")

        with tempfile.NamedTemporaryFile(suffix=".pbm", delete=False) as tmp:
            pbm_path = Path(tmp.name)
            bw.save(pbm_path)

    try:
        subprocess.run(
            [
                str(POTRACE_PATH),
                str(pbm_path),
                "-s",
                "-o", str(output_file)
            ],
            check=True
        )
        print(f"{input_file} converted to svg")
    finally:
        pbm_path.unlink(missing_ok=True)


def main():
    input_dir = Path(sys.argv[1])
    output_dir = Path(sys.argv[2])
    output_dir.mkdir(exist_ok=True)

    print("Converting to svgs.")

    for file in input_dir.iterdir():
        if file.suffix.lower() not in INPUT_EXTENSIONS:
            continue

        output_file = output_dir / (file.stem + ".svg")
        convert_with_potrace(file, output_file)


if __name__ == "__main__":
    main()