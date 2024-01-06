from PySide6.QtCore import Qt


def mouse_press_event(main_window, event):
    if event.button() == Qt.LeftButton:
        main_window.isDragging = True
        main_window.dragPos = event.globalPos() - main_window.pos()


def mouse_move_event(main_window, event):
    if main_window.isDragging:
        main_window.move(event.globalPos() - main_window.dragPos)


def mouse_release_event(main_window, event):
    if event.button() == Qt.LeftButton:
        main_window.isDragging = False
        main_window.dragPos = None


def minimize(main_window):
    main_window.showMinimized()


def maximize(main_window):
    if main_window.isMinimized:
        main_window.showMaximized()
        main_window.ui.maximize_pushButton.setText("◱")
        main_window.isMinimized = False
    else:
        main_window.showNormal()
        main_window.ui.maximize_pushButton.setText("□")
