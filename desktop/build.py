"""Build the PyQt6 client into one Windows executable."""
from pathlib import Path
import shutil
import subprocess
import sys


APP_DIR = Path(__file__).resolve().parent
APP_NAME = "CompetitorMonitor"


def build() -> None:
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        raise SystemExit(
            "PyInstaller is not installed. Run: "
            "python -m pip install -r desktop/requirements.txt"
        )

    command = [
        sys.executable,
        "-m", "PyInstaller",
        "--name", APP_NAME,
        "--onefile",
        "--windowed",
        "--noconfirm",
        "--clean",
        "--distpath", str(APP_DIR / "dist"),
        "--workpath", str(APP_DIR / "build"),
        "--specpath", str(APP_DIR),
        "--hidden-import", "PyQt6.QtCore",
        "--hidden-import", "PyQt6.QtGui",
        "--hidden-import", "PyQt6.QtWidgets",
        str(APP_DIR / "main.py"),
    ]

    print("Building CompetitorMonitor.exe...")
    subprocess.run(command, cwd=APP_DIR, check=True)

    exe_path = APP_DIR / "dist" / f"{APP_NAME}.exe"
    if not exe_path.exists():
        raise SystemExit("PyInstaller finished without creating the EXE")
    print(f"Ready: {exe_path}")


def clean() -> None:
    for path in (APP_DIR / "build", APP_DIR / "dist"):
        if path.exists():
            shutil.rmtree(path)
    for spec_file in APP_DIR.glob("*.spec"):
        spec_file.unlink()
    print("Build artifacts removed.")


if __name__ == "__main__":
    clean() if len(sys.argv) > 1 and sys.argv[1] == "clean" else build()
