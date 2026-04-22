# PNG to SVG Batch Converter

This tool converts raster images (PNG/JPG) into SVG files using bitmap tracing.

It relies on Potrace for vectorisation.

---

## Requirements

### Python dependencies

Install required packages:

pip install pillow

---

### Potrace (required)

This project depends on the external binary:

:contentReference[oaicite:0]{index=0}

You must download it manually.

#### Download

Download Potrace for Windows:

http://potrace.sourceforge.net/

Choose the Windows 64-bit version and extract it.

---

## Folder setup

Place the extracted folder inside your project directory:

your_project/
├── init.py
└── potrace-1.16.win64/
    └── potrace.exe

The important requirement is that potrace.exe is located here:

potrace-1.16.win64/potrace.exe

---

## Usage

Run the script with:

python init.py &lt;input_folder&gt; &lt;output_folder&gt;

### Example:

python init.py examples examples_svg

---

## Behaviour

- Converts .png, .jpg, .jpeg files  
- Outputs .svg files to the target folder  
- Skips files that already exist  
- Uses Potrace for fast vector conversion  

---

## Troubleshooting

### “Potrace not found”

Ensure:
- potrace.exe exists in potrace-1.16.win64/
- Folder name is correct
- Script is executed from the project root

---

### “FileNotFoundError”

Check the printed path in the script:

print(POTRACE_PATH)

It must point directly to potrace.exe.

---

## Notes

- This tool performs binary thresholding, so colour images are simplified to black and white before vectorisation.
- For best results, use high-contrast logos or icons.