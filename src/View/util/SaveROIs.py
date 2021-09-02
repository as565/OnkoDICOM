from PySide6 import QtCore

from src.View.mainpage.DrawROIWindow.SaveROIProgressWindow import \
    SaveROIProgressWindow


def connectSaveROIProgress(window, roi_list, rtss, new_roi_name, roi_saved_signal):
    # Create a popup window that modifies the RTSTRUCT and tells the user
    # that processing is happening.
    progress_window = SaveROIProgressWindow(window,
                                            QtCore.Qt.WindowTitleHint)
    progress_window.signal_roi_saved.connect(roi_saved_signal)
    progress_window.start_saving(rtss, new_roi_name,
                                 roi_list)
    progress_window.show()
