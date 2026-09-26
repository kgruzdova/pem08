# CompetitorAI Desktop

The single PyQt6 desktop application for this project. It mirrors the web interface:

- competitor text analysis;
- image analysis with file picker and drag-and-drop;
- website parsing through the backend and Selenium Chrome;
- request history viewing and clearing;
- asynchronous requests without freezing the UI.

## Run

Start the backend from the project root:

```powershell
python run.py
```

Then, in another terminal:

```powershell
python desktop/main.py
```

The backend must be available at `http://localhost:8000`.

## Build EXE

```powershell
python -m pip install -r desktop/requirements.txt
python desktop/build.py
```

The executable is created at:

```text
desktop/dist/CompetitorMonitor.exe
```

To remove build artifacts:

```powershell
python desktop/build.py clean
```
