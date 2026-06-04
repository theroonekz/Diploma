from main import *

# WITH ACCESS TO MAIN WINDOW WIDGETS

class AppFunctions(MainWindow):
    def setThemeHack(self):
        Settings.BTN_LEFT_BOX_COLOR = "background-color: #495474;"
        Settings.BTN_RIGHT_BOX_COLOR = "background-color: #495474;"
        Settings.MENU_SELECTED_STYLESHEET = MENU_SELECTED_STYLESHEET = """
        border-left: 12px solid qlineargradient(spread:pad, x1:0.034, y1:0, x2:0.216, y2:0, stop:0.499 rgba(255, 121, 198, 255), stop:0.5 rgba(85, 170, 255, 0));
        background-color: #566388;
        """


        self.ui.text_lastname.setStyleSheet("background-color: #6272a4;")
        self.ui.text_firstname.setStyleSheet("background-color: #6272a4;")
        self.ui.text_middlename.setStyleSheet("background-color: #6272a4;")
        self.ui.text_age.setStyleSheet("background-color: #6272a4;")
        self.ui.text_phone.setStyleSheet("background-color: #6272a4;")
        self.ui.text_city.setStyleSheet("background-color: #6272a4;")

        self.ui.btn_text_clean.setStyleSheet("background-color: #6272a4;")

        self.ui.btn_Append.setStyleSheet("background-color: #6272a4;")
        self.ui.btn_Remove.setStyleSheet("background-color: #6272a4;")
        self.ui.btn_Update.setStyleSheet("background-color: #6272a4;")

        self.ui.box_gender.setStyleSheet("background-color: #6272a4;")