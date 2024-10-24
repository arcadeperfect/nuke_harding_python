import os
import shutil
import zipfile
from pathlib import Path

def build_release():
    # Project paths
    project_root = Path(__file__).parent.parent
    src_dir = project_root / "src" / "nuke_harding_python"
    vendor_dir = src_dir / "vendor"
    pysequitur_src = project_root.parent / "pysequitur" / "src" / "pysequitur"
    
    # Create vendor directory if it doesn't exist
    vendor_dir.mkdir(exist_ok=True)
    
    # Copy pysequitur into vendor directory
    vendor_pysequitur = vendor_dir / "pysequitur"
    if vendor_pysequitur.exists():
        shutil.rmtree(vendor_pysequitur)
    shutil.copytree(pysequitur_src, vendor_pysequitur)
    
    # Create distributable zip
    dist_dir = project_root / "dist"
    dist_dir.mkdir(exist_ok=True)
    
    zip_path = dist_dir / "nuke_harding_python.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        # Add all files from src directory
        for root, _, files in os.walk(src_dir):
            for file in files:
                file_path = Path(root) / file
                arc_path = file_path.relative_to(src_dir)
                zf.write(file_path, arc_path)

if __name__ == "__main__":
    build_release()