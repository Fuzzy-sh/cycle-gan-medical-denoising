import os
from pathlib import Path

# Define structure relative to current folder
structure = {
    ".": ["README.md", "requirements.txt", "main.py"],
    "models": ["generator.py", "discriminator.py"],
    "utils": ["metrics.py", "dataset_loader.py"],
    "examples": ["input_image.nii.gz", "output_image.nii.gz"],
}

# Create folders and files
for folder, files in structure.items():
    dir_path = Path(folder)
    dir_path.mkdir(parents=True, exist_ok=True)
    for file_name in files:
        file_path = dir_path / file_name
        if not file_path.exists():
            file_path.write_text(f"# {file_name}\n\n")
            print(f"Created {file_path}")

# Add README content
readme_path = Path("README.md")
readme_content = """# CycleGAN for Medical Image Denoising

This project provides a simplified implementation of a CycleGAN used for denoising medical images.  
The full version includes advanced pipelines used in an HPC environment with 3D NIfTI images and mixed precision training.

## Features
- ResNet-based Generator and Discriminator
- Paired and Unpaired Training Support
- Evaluation: PSNR, SSIM, and QILV
- AMP (Mixed Precision) Support

## Structure
- `models/`: Generator and Discriminator definitions
- `utils/`: Data loading and metrics
- `examples/`: Sample input/output NIfTI files

> This repo includes a simplified version only. Full training code is omitted for publication/privacy reasons.

## Contact
For collaboration or access to the full pipeline, please contact [your_email@example.com].

"""
readme_path.write_text(readme_content)
print(f"Updated {readme_path}")
