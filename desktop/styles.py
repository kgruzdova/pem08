"""Warm editorial visual theme for the PyQt6 desktop application."""

DARK_THEME = """
QMainWindow, QWidget {
    background-color: #f5f1ea;
    color: #162033;
    font-family: 'Segoe UI', 'Arial', sans-serif;
    font-size: 14px;
}

#sidebar { background-color: #111a2a; border: none; }
#logo { color: #f36f4d; font-size: 21px; font-weight: 700; padding: 28px 24px; }

QPushButton#navButton {
    background-color: transparent; color: #aeb7c4; border: 1px solid transparent;
    border-radius: 14px; padding: 14px 16px; text-align: left;
    font-size: 14px; font-weight: 600;
}
QPushButton#navButton:hover { background-color: #1d2a3e; color: #fffaf2; }
QPushButton#navButton:checked { background-color: #f36f4d; color: #fffaf2; border-color: #f36f4d; }

QFrame#card {
    background-color: #fffdf9; border: 1px solid #e7dfd4; border-radius: 24px;
}
QFrame#card:hover { border-color: #d9cabb; }

QLabel#title { color: #111a2a; font-size: 32px; font-weight: 800; }
QLabel#subtitle { color: #718092; font-size: 15px; }
QLabel#cardTitle { color: #111a2a; font-size: 20px; font-weight: 750; }
QLabel#cardDescription { color: #7b8795; font-size: 13px; }
QLabel#sectionTitle { color: #e75d42; font-size: 14px; font-weight: 750; margin-bottom: 8px; }

QTextEdit, QLineEdit {
    background-color: #faf7f2; border: 1px solid #ded4c8; border-radius: 14px;
    padding: 13px; color: #162033; font-size: 14px; selection-background-color: #f6b29d;
}
QTextEdit:focus, QLineEdit:focus { border: 2px solid #f36f4d; background-color: #fffdf9; }
QTextEdit::placeholder, QLineEdit::placeholder { color: #a7a097; }

QPushButton#primaryButton {
    background-color: #f36f4d; color: #fffaf2; border: none; border-radius: 14px;
    padding: 14px 24px; font-size: 14px; font-weight: 750;
}
QPushButton#primaryButton:hover { background-color: #dd593c; }
QPushButton#primaryButton:pressed { background-color: #c94b32; }
QPushButton#primaryButton:disabled { background-color: #d8cec3; color: #9d948a; }

QPushButton#secondaryButton {
    background-color: #f4ede5; color: #596575; border: 1px solid #ded4c8;
    border-radius: 12px; padding: 11px 18px; font-size: 14px; font-weight: 650;
}
QPushButton#secondaryButton:hover { background-color: #ebe0d5; color: #162033; }

QFrame#uploadZone {
    background-color: #faf7f2; border: 2px dashed #cdbfb1;
    border-radius: 20px; min-height: 200px;
}
QFrame#uploadZone:hover { border-color: #f36f4d; background-color: #fff4ee; }

QScrollArea { background-color: transparent; border: none; }
QScrollBar:vertical { background-color: transparent; width: 9px; }
QScrollBar::handle:vertical { background-color: #cdbfb1; border-radius: 4px; min-height: 34px; }
QScrollBar::handle:vertical:hover { background-color: #a99b8e; }
QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { height: 0px; }

QFrame#resultsCard, QFrame#resultBlock {
    background-color: #fffdf9; border: 1px solid #e7dfd4; border-radius: 18px;
}
QFrame#resultBlock { border-left: 4px solid #f36f4d; padding: 16px; margin: 8px 0; }
QFrame#historyItem { background-color: #fffdf9; border: 1px solid #e7dfd4; border-radius: 16px; padding: 12px; }
QFrame#historyItem:hover { border-color: #f3b29f; }

QProgressBar { background-color: #e6ddd3; border: none; border-radius: 4px; height: 8px; }
QProgressBar::chunk { background-color: #f36f4d; border-radius: 4px; }

QToolTip { background-color: #111a2a; color: #fffaf2; border: none; border-radius: 8px; padding: 8px; }
"""
