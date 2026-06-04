# MAIN FILE
# ///////////////////////////////////////////////////////////////
from main import *

# GLOBALS
# ///////////////////////////////////////////////////////////////
GLOBAL_STATE = False
GLOBAL_TITLE_BAR = True

class UIFunctions(MainWindow):
    def sunrise(ts):
        return datetime.datetime.utcfromtimestamp(ts).strftime('%H:%M')

    def sunset(ts):
        return datetime.datetime.utcfromtimestamp(ts).strftime('%H:%M')

    def LoadExtraPage(self):
        requestcity = requests.get('https://ipinfo.io')
        city_by_ip_json = requestcity.json()

        if self.ui.rb_ip.isChecked(): city = city_by_ip_json['city']
        elif self.ui.rb_text.isChecked():
            if not self.ui.text_weather_city.text().isspace():
                city = self.ui.text_weather_city.text()
            else:
                QMessageBox.about(self, "Загрузка погоды", "Введите название города!")
                return

        # OpenWeatherMap API key (get your own at https://openweathermap.org/api)
        api_key = os.getenv('OPENWEATHER_API_KEY', 'YOUR_API_KEY')
        requestweather = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&lang=RU&appid={api_key}')

        weather = requestweather.json()

        if weather['cod'] != 200:
            QMessageBox.about(self, "Загрузка погоды", "Не удалось загрузить погоду данного города!")
            return

        now = datetime.datetime.now()

        temp = weather['main']['temp'] - 273.15
        temp_feels = weather['main']['feels_like'] - 273.15
        humidity = weather['main']['humidity']
        visibility = weather['visibility']/1000
        description = weather['weather'][0]['description']
        wind = weather['wind']['speed']
        timezone = weather['timezone']
        sunrise_sec = weather['sys']['sunrise']
        sunset_sec = weather['sys']['sunset']

        sunrise = UIFunctions.sunrise(sunrise_sec + timezone)
        sunset = UIFunctions.sunset(sunset_sec + timezone)

        self.ui.label_weather_title.setText(f"Текущий город: {weather['name']}")
        self.ui.label_weather_last.setText(f"Последнее обновление: {now.hour}:{now.minute:02d}")

        self.ui.frame_image.setStyleSheet(f'background-image: url(":/weather/images/weather/{weather["weather"][0]["icon"]}@2x.png")')

        self.ui.label_weather_description.setText(description)

        self.ui.label_weather_temp.setText(f'Температура: {int(temp)} °C')

        self.ui.label_weather_feelslike.setText(f'Ощущается как: {int(temp_feels)} °C')
        self.ui.label_weather_humidity.setText(f'Влажность: {humidity}%')
        self.ui.label_weather_visibility.setText(f'Видимость: {visibility:.1f} км')
        self.ui.label_weather_wind.setText(f'Ветер: {wind:.2f} м/с')
        self.ui.label_weather_sunrise.setText('Рассвет: ' + (sunrise if sunrise_sec != 0 else 'Неизвестно'))
        self.ui.label_weather_sunset.setText('Закат: ' + (sunset if sunset_sec != 0 else 'Неизвестно'))


    # SWITCH THEME STYLE ON DARK/LIGHT
    # ///////////////////////////////////////////////////////////////
    def SwitchStyle(self, ButtonSwitcher):
        if ButtonSwitcher:
            if Settings.THEME_STYLE == 'dark': Settings.THEME_STYLE = 'light'
            else: Settings.THEME_STYLE = 'dark'

        theme_name = 'Светлую' if Settings.THEME_STYLE == 'dark' else 'Тёмную'
        self.ui.btn_theme.setText(f"Сменить на {theme_name} тему")
        themeFile = f"themes\\{Settings.THEME_STYLE}_theme.qss"

        # LOAD AND APPLY STYLE
        UIFunctions.theme(self, themeFile)

    # MAXIMIZE/RESTORE
    # ///////////////////////////////////////////////////////////////
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == False:
            self.showMaximized()
            GLOBAL_STATE = True
            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.maximizeRestoreAppBtn.setToolTip("Restore")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons_new/images/icons_new/icons8-восстановить-окно-48.png"))
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = False
            self.showNormal()
            self.resize(self.width() + 1, self.height() + 1)
            self.ui.appMargins.setContentsMargins(10, 10, 10, 10)
            self.ui.maximizeRestoreAppBtn.setToolTip("Maximize")
            self.ui.maximizeRestoreAppBtn.setIcon(QIcon(u":/icons_new/images/icons_new/icons8-развернуть-окно-50.png"))
            self.ui.frame_size_grip.show()

    # RETURN STATUS
    # ///////////////////////////////////////////////////////////////
    def returStatus(self):
        return GLOBAL_STATE

    # SET STATUS
    # ///////////////////////////////////////////////////////////////
    def setStatus(self, status):
        global GLOBAL_STATE
        GLOBAL_STATE = status

    # TOGGLE MENU
    # ///////////////////////////////////////////////////////////////
    def toggleMenu(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.leftMenuBg.width()
            maxExtend = Settings.MENU_WIDTH
            standard = 60

            # SET MAX WIDTH
            if width == 60:
                widthExtended = maxExtend
            else:
                widthExtended = standard

            # ANIMATION
            self.animation = QPropertyAnimation(self.ui.leftMenuBg, b"minimumWidth")
            self.animation.setDuration(Settings.TIME_ANIMATION)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

    # TOGGLE LEFT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleLeftBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraLeftBox.width()
            widthRightBox = self.ui.extraRightBox.width()
            maxExtend = Settings.LEFT_BOX_WIDTH
            color = Settings.BTN_LEFT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.toggleLeftBox.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.toggleLeftBox.setStyleSheet(style + color)
                if widthRightBox != 0:
                    style = self.ui.settingsTopBtn.styleSheet()
                    self.ui.settingsTopBtn.setStyleSheet(style.replace(Settings.BTN_RIGHT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.toggleLeftBox.setStyleSheet(style.replace(color, ''))

        UIFunctions.start_box_animation(self, width, widthRightBox, "left")

    # TOGGLE RIGHT BOX
    # ///////////////////////////////////////////////////////////////
    def toggleRightBox(self, enable):
        if enable:
            # GET WIDTH
            width = self.ui.extraRightBox.width()
            widthLeftBox = self.ui.extraLeftBox.width()
            maxExtend = Settings.RIGHT_BOX_WIDTH
            color = Settings.BTN_RIGHT_BOX_COLOR
            standard = 0

            # GET BTN STYLE
            style = self.ui.settingsTopBtn.styleSheet()

            # SET MAX WIDTH
            if width == 0:
                widthExtended = maxExtend
                # SELECT BTN
                self.ui.settingsTopBtn.setStyleSheet(style + color)
                if widthLeftBox != 0:
                    style = self.ui.toggleLeftBox.styleSheet()
                    self.ui.toggleLeftBox.setStyleSheet(style.replace(Settings.BTN_LEFT_BOX_COLOR, ''))
            else:
                widthExtended = standard
                # RESET BTN
                self.ui.settingsTopBtn.setStyleSheet(style.replace(color, ''))

            UIFunctions.start_box_animation(self, widthLeftBox, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0

        # Check values
        if left_box_width == 0 and direction == "left":
            left_width = Settings.LEFT_BOX_WIDTH
        else:
            left_width = 0
        # Check values
        if right_box_width == 0 and direction == "right":
            right_width = Settings.RIGHT_BOX_WIDTH
        else:
            right_width = 0

            # ANIMATION LEFT BOX
        self.left_box = QPropertyAnimation(self.ui.extraLeftBox, b"minimumWidth")
        self.left_box.setDuration(Settings.TIME_ANIMATION)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX
        self.right_box = QPropertyAnimation(self.ui.extraRightBox, b"minimumWidth")
        self.right_box.setDuration(Settings.TIME_ANIMATION)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

    # SELECT/DESELECT MENU
    # ///////////////////////////////////////////////////////////////
    # SELECT
    def selectMenu(getStyle):
        select = getStyle + Settings.MENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectMenu(getStyle):
        deselect = getStyle.replace(Settings.MENU_SELECTED_STYLESHEET, "")
        return deselect

    def selectExtraMenu(getStyle):
        select = getStyle + Settings.LEFT_EXTRAMENU_SELECTED_STYLESHEET
        return select

    # DESELECT
    def deselectExtraMenu(getStyle):
        deselect = getStyle.replace(Settings.LEFT_EXTRAMENU_SELECTED_STYLESHEET, "")
        return deselect

    # START SELECTION
#    def selectStandardMenu(self, widget):
#        for w in self.ui.topMenu.findChildren(QPushButton):
#            if w.objectName() == widget:
#                w.setStyleSheet(UIFunctions.selectMenu(w.styleSheet()))

    # RESET SELECTION
    def resetStyle_Menu(self, widget):
        for w in self.ui.topMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectMenu(w.styleSheet()))

        # RESET SELECTION
    def resetStyle_ExtraMenu(self, widget):
        for w in self.ui.extraTopMenu.findChildren(QPushButton):
            if w.objectName() != widget:
                w.setStyleSheet(UIFunctions.deselectExtraMenu(w.styleSheet()))

    # IMPORT THEMES FILES QSS/CSS
    # ///////////////////////////////////////////////////////////////
    def theme(self, file):
        str = open(file, 'r').read()
        self.ui.styleSheet.setStyleSheet(str)

    # START - GUI DEFINITIONS
    # ///////////////////////////////////////////////////////////////

    def uiDefinitions(self):
        def dobleClickMaximizeRestore(event):
            # IF DOUBLE CLICK CHANGE STATUS
            if event.type() == QEvent.MouseButtonDblClick:
                if Settings.ENABLE_CUSTOM_TITLE_BAR:
                    QTimer.singleShot(10, lambda: UIFunctions.maximize_restore(self))

        self.ui.titleRightInfo.mouseDoubleClickEvent = dobleClickMaximizeRestore

        if Settings.ENABLE_CUSTOM_TITLE_BAR:
            # STANDARD TITLE BAR
            self.setWindowFlags(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

            # MOVE WINDOW / MAXIMIZE / RESTORE
            def moveWindow(event):
                if Settings.ENABLE_CUSTOM_TITLE_BAR:
                    # IF MAXIMIZED CHANGE TO NORMAL
                    if UIFunctions.returStatus(self):
                        UIFunctions.maximize_restore(self)
                    # MOVE WINDOW
                    if event.buttons() == Qt.LeftButton:
                        self.move(self.pos() + event.globalPos() - self.dragPos)
                        self.dragPos = event.globalPos()
                        event.accept()

            self.ui.titleRightInfo.mouseMoveEvent = moveWindow

            self.ui.minimizeAppBtn.show()
            self.ui.maximizeRestoreAppBtn.show()
            self.ui.closeAppBtn.show()
            self.ui.frame_size_grip.show()
        else:
            self.setWindowFlags(Qt.Window)
            self.setAttribute(Qt.WA_NoSystemBackground)

            self.ui.appMargins.setContentsMargins(0, 0, 0, 0)
            self.ui.minimizeAppBtn.hide()
            self.ui.maximizeRestoreAppBtn.hide()
            self.ui.closeAppBtn.hide()
            self.ui.frame_size_grip.hide()

        # RESIZE WINDOW
        self.sizegrip = QSizeGrip(self.ui.frame_size_grip)
        self.sizegrip.setStyleSheet("width: 20px; height: 20px; margin 0px; padding: 0px;")

        # SHOW WINDOW
        self.show()

    def SwitchTitlebar(self, ButtonSwitcher):
        # USE CUSTOM TITLE BAR | USE AS "False" FOR MAC OR LINUX
        # ///////////////////////////////////////////////////////////////
        if ButtonSwitcher:
            if Settings.ENABLE_CUSTOM_TITLE_BAR:
                Settings.ENABLE_CUSTOM_TITLE_BAR = False
            else:
                Settings.ENABLE_CUSTOM_TITLE_BAR = True

        action = 'Убрать' if Settings.ENABLE_CUSTOM_TITLE_BAR else 'Установить'
        self.ui.btn_titlebar.setText(f"{action} заголовок")
        UIFunctions.uiDefinitions(self)

    def closeApp(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setText("Вы действительно хотите закрыть приложение?")
        msgBox.setWindowTitle("Подтверждение выхода")
        msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            sys.exit()

    def SaveButton(self):
        ConfigFile.config.set("theme_style", "default_style", Settings.THEME_STYLE)
        ConfigFile.config.set("titlebar", "use_custom_titlebar", "True" if Settings.ENABLE_CUSTOM_TITLE_BAR else "False")
        with open("config.ini", "w") as config_file:
            ConfigFile.config.write(config_file)
    # ///////////////////////////////////////////////////////////////
    # END - GUI DEFINITIONS
