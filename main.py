import sys
import os
import platform
import pymysql
import io
import xlwt
import xlrd
import datetime
import requests

# IMPORT / GUI AND MODULES AND WIDGETS
# ///////////////////////////////////////////////////////////////
from modules import *

# SET AS GLOBAL WIDGETS
# ///////////////////////////////////////////////////////////////
widgets = None
con = None
cursor = None

db_db = None

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        ConfigFile()
        ConfigFile.loadConfig(Settings)

        if not os.path.exists("export"):
            os.mkdir("export")

        # SET AS GLOBAL WIDGETS
        # ///////////////////////////////////////////////////////////////
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        # DATABASE LOADING
        # ///////////////////////////////////////////////////////////////

        self.ConnectToDatabase(True)

        # APP NAME
        # ///////////////////////////////////////////////////////////////
        title = "ТОО «ФХ «УЛАН»"
        description = "ТОО «ФЕРМЕРСКОЕ ХОЗЯЙСТВО «УЛАН»"
        # APPLY TEXTS
        self.setWindowTitle(title)
        widgets.titleRightInfo.setText(description)

        # TOGGLE MENU
        # ///////////////////////////////////////////////////////////////
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        # SET UI DEFINITIONS
        # ///////////////////////////////////////////////////////////////
        UIFunctions.uiDefinitions(self)

        # LOAD EXTRA PAGE INFO - WEATHER
        UIFunctions.LoadExtraPage(self)
        self.ui.btn_weather_enter.clicked.connect(lambda: UIFunctions.LoadExtraPage(self))
        self.ui.text_weather_city.setEnabled(False)

        def WeatherEnableEnter():
            self.ui.text_weather_city.setEnabled(True)

        self.ui.rb_text.toggled.connect(WeatherEnableEnter)

        def WeatherDisableEnter():
            self.ui.text_weather_city.setEnabled(False)
            self.ui.text_weather_city.setText("")

        self.ui.rb_ip.toggled.connect(WeatherDisableEnter)

        # QTableWidget PARAMETERS
        # ///////////////////////////////////////////////////////////////
        self.ui.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget_2.horizontalHeader().setVisible(True)

        # BUTTONS CLICK
        # ///////////////////////////////////////////////////////////////
        widgets.btn_home.clicked.connect(self.buttonClick)
        widgets.btn_export.clicked.connect(self.buttonClick)
        widgets.btn_import.clicked.connect(self.buttonClick)
        widgets.btn_save.clicked.connect(self.buttonClick)
        widgets.btn_weather.clicked.connect(self.buttonClick)

        widgets.btn_info.clicked.connect(self.buttonClick)
        widgets.btn_db.clicked.connect(self.buttonClick)
        widgets.btn_author.clicked.connect(self.buttonClick)

        self.ui.btn_db_connector.clicked.connect(self.button_DataBaseClick)
        self.ui.btn_db_loadconfig.clicked.connect(self.LoadDBFromConfig)
        self.ui.btn_db_save.clicked.connect(self.SaveDBFromConfig)

        # EXTRA LEFT BOX
        def openCloseLeftBox():
            UIFunctions.toggleLeftBox(self, True)
        widgets.toggleLeftBox.clicked.connect(openCloseLeftBox)
        widgets.extraCloseColumnBtn.clicked.connect(openCloseLeftBox)

        # //////////////////////////////////////////
        # /////////////// PAGE TABLE ///////////////
        # ///////////////// START ///////////////////
        self.ui.box_gender_select.setVisible(False)

        self.ui.text_id.returnPressed.connect(self.text_PressedFunction)
        self.ui.btn_text_clean.clicked.connect(self.text_CleanFunction)
        self.ui.btn_Append.clicked.connect(self.Append_Function)
        self.ui.btn_Update.clicked.connect(self.Update_Function)
        self.ui.btn_Remove.clicked.connect(self.Remove_Function)


        self.ui.btn_find_clean.clicked.connect(self.find_CleanFunction)
        self.ui.btn_Find.clicked.connect(self.Find_Function)
        self.ui.box_find.currentIndexChanged.connect(self.find_SelectFunction)

        self.ui.tableWidget_2.cellClicked.connect(self.cellClicked)
        self.ui.btn_table_refresh.clicked.connect(self.Table_Refresh)
        self.ui.box_sort.currentIndexChanged.connect(self.table_SortFunction)
        # ////////////////// END ////////////////////
        # //////////////////////////////////////////

        # EXTRA RIGHT BOX
        def openCloseRightBox():
            UIFunctions.toggleRightBox(self, True)
        widgets.settingsTopBtn.clicked.connect(openCloseRightBox)

        # SWITCH STYLE BUTTON
        widgets.btn_theme.clicked.connect(lambda: UIFunctions.SwitchStyle(self, True))

        # SWITCH TITLEBAR BUTTON
        widgets.btn_titlebar.clicked.connect(lambda: UIFunctions.SwitchTitlebar(self, True))

        # SWITCH TITLEBAR BUTTON
        widgets.btn_save_settings.clicked.connect(lambda: UIFunctions.SaveButton(self))

        AppFunctions.setThemeHack(self)

        # MINIMIZE WINDOW
        self.ui.minimizeAppBtn.clicked.connect(lambda: self.showMinimized())

        # MAXIMIZE/RESTORE WINDOW
        self.ui.maximizeRestoreAppBtn.clicked.connect(lambda: UIFunctions.maximize_restore(self))

        # CLOSE APPLICATION WINDOW
        self.ui.closeAppBtn.clicked.connect(lambda: UIFunctions.closeApp(self))

        # SET CUSTOM THEME
        # ///////////////////////////////////////////////////////////////
        UIFunctions.SwitchStyle(self, False)
        UIFunctions.SwitchTitlebar(self, False)

        # SET HOME PAGE AND SELECT MENU
        # ///////////////////////////////////////////////////////////////
        widgets.stackedWidget.setCurrentWidget(widgets.page_table)
        widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))
        widgets.btn_info.setStyleSheet(UIFunctions.selectExtraMenu(widgets.btn_info.styleSheet()))

    # BUTTONS CLICK
    # Post here your functions for clicked buttons
    # ///////////////////////////////////////////////////////////////

    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # MENU - SHOW HOME PAGE
        if btnName == "btn_home":
            widgets.stackedWidget.setCurrentWidget(widgets.page_table)
            UIFunctions.resetStyle_Menu(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        if btnName == "btn_export":
            self.exportFunction()

        if btnName == "btn_import":
            self.importFunction()

        if btnName == "btn_save":
            self.saveFunction()

        # EXTRAMENU - SHOW INFORMATION PAGE
        if btnName == "btn_info":
            widgets.stackedWidget_2.setCurrentWidget(widgets.page_info)
            UIFunctions.resetStyle_ExtraMenu(self, btnName)
            btn.setStyleSheet(UIFunctions.selectExtraMenu(btn.styleSheet()))

        # SHOW DATABASE PAGE
        if btnName == "btn_db":
            widgets.stackedWidget_2.setCurrentWidget(widgets.page_db)
            UIFunctions.resetStyle_ExtraMenu(self, btnName)
            btn.setStyleSheet(UIFunctions.selectExtraMenu(btn.styleSheet()))

        # SHOW AUTHOR PAGE
        if btnName == "btn_author":
            widgets.stackedWidget_2.setCurrentWidget(widgets.page_author)
            UIFunctions.resetStyle_ExtraMenu(self, btnName)
            btn.setStyleSheet(UIFunctions.selectExtraMenu(btn.styleSheet()))

        # CLOSE PROGRAM
        if btnName == "btn_weather":
            widgets.stackedWidget.setCurrentWidget(widgets.page_weather)
            UIFunctions.resetStyle_Menu(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

    def exportFunction(self):
        wb = xlwt.Workbook()

        if Settings.IMPORTED:
            QMessageBox.about(self, "Экспорт таблицы", "Сначала верните данные таблицы!")
            return

        try:
            cursor.execute('select * from ulan')
            datas = cursor.fetchall()

            cursor.execute("select count(*) from ulan")
            number = list(cursor)
            rowcount = number[0][0]
            colcount = 8
        except:
            QMessageBox.about(self, "Экспорт таблицы", "Не удалось экспортировать таблицу!")
            return

        now = datetime.datetime.now()
        sheet1 = wb.add_sheet('Sheet1')

        title_names = ['id', 'lastname', 'firstname', 'middlename', 'gender', 'age', 'phone_number', 'city']

        font_title = xlwt.Font()
        font_title.name = 'Times New Roman'
        font_title.bold = True
        font_title.height = 200

        style_title = xlwt.XFStyle()
        style_title.font = font_title

        for j in range(colcount):
            sheet1.write(0, j, title_names[j], style_title)

        for i in range(rowcount):
            for j in range(colcount):
                sheet1.write(i + 1, j, datas[i][j])

        sheet1.write(0, 9, "markedXLS")

        export_dir = f"export\\{db_db}"
        if not os.path.exists(export_dir):
            os.makedirs(export_dir, exist_ok=True)

        filename = f"{now.day}.{now.month}.{now.year} {now.hour}-{now.minute}-{now.second}.xls"
        filepath = f"export\\{db_db}\\{filename}"
        wb.save(filepath)

        QMessageBox.about(self, "Экспорт таблицы", 
                         f"Таблица успешно экспортирована!\n\nБаза данных: {db_db}\nНазвание: {filename}")

    def importFunction(self):
        directory = QFileDialog.getOpenFileName(self, 'Open file', 'export/', "Excel Files (*.xls)")[0]
        filenamesplit = directory.split("export/")

        if directory == '':
            return

        wb = xlrd.open_workbook(directory, formatting_info=True)
        sheet = wb.sheet_by_index(0)

        if sheet.ncols < 9:
            QMessageBox.about(self, "Импорт таблицы", "Эта таблица не может быть импортирована!")
            return

        if not sheet.cell_value(0, 9) == 'markedXLS':
            QMessageBox.about(self, "Импорт таблицы", "Эта таблица не может быть импортирована!")
            return

        rowcount = sheet.nrows
        colcount = 8

        self.ui.tableWidget_2.setRowCount(rowcount - 1)

        for i in range(rowcount-1):
            for j in range(colcount):
                    self.ui.tableWidget_2.setItem(i, j, QTableWidgetItem(str(
                        int(sheet.cell_value(i + 1, j)) if j == 0 else sheet.cell_value(i + 1, j)   )))

        self.ui.leftFrame.setVisible(False)
        self.ui.table_upFrame.setVisible(False)
        self.ui.btn_table_refresh.setText("Вернуть")
        Settings.IMPORTED = True
        self.ui.label_name_import.setText("Файл: %s" % filenamesplit[1])
        QMessageBox.about(self, "Импорт таблицы", "Таблица успешно импортирована!")

    def saveFunction(self):
        if not Settings.IMPORTED:
            QMessageBox.about(self, "Перезапись таблицы", "Не выбран файл!")
            return

        try:
            if con.open:
                msgBox = QMessageBox()
                msgBox.setIcon(QMessageBox.Information)
                msgBox.setText("Вы действительно хотите перезаписать данные таблицы в подключенной БД?")
                msgBox.setWindowTitle("Подтверждение действия")
                msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

                returnValue = msgBox.exec()
                if returnValue == QMessageBox.Cancel:
                    return
        except:
            QMessageBox.about(self, "Перезапись таблицы", "Нет подключения к БД!")
            return

        rowcount = self.ui.tableWidget_2.rowCount()

        try:
            sql = 'DELETE from ulan'
            cursor.execute(sql)

            for i in range(rowcount):
                sql = 'insert into ulan  (`lastname`, `firstname`, `middlename`, `gender`, `age`, `phone_number`, `city`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
                cursor.execute(sql, (
                    self.ui.tableWidget_2.item(i, 1).text(),
                    self.ui.tableWidget_2.item(i, 2).text(),
                    self.ui.tableWidget_2.item(i, 3).text(),
                    self.ui.tableWidget_2.item(i, 4).text(),
                    self.ui.tableWidget_2.item(i, 5).text(),
                    self.ui.tableWidget_2.item(i, 6).text(),
                    self.ui.tableWidget_2.item(i, 7).text()))
                con.commit()

            self.Table_Refresh()
            self.ui.stackedWidget.setCurrentWidget(widgets.page_table)
            UIFunctions.resetStyle_Menu(self, self.ui.btn_home)
            self.ui.btn_home.setStyleSheet(UIFunctions.selectMenu(self.ui.btn_home.styleSheet()))
            QMessageBox.about(self, "Перезапись таблицы", "Таблица в Базе Данных успешно перезаписана!")

        except:
            QMessageBox.about(self, "Перезапись таблицы", "Нет подключения к БД!")

    def ConnectToDatabase(self, once):
        if once: global con, cursor, db_db

        db_host = Settings.DB_HOST if once else self.ui.text_host.text()
        db_user = Settings.DB_USERNAME if once else self.ui.text_username.text()
        db_password = Settings.DB_PASSWORD if once else self.ui.text_password.text()
        db_db = Settings.DB_DB if once else self.ui.text_db.text()

        if once: self.ui.text_host.setText(Settings.DB_HOST)
        if once: self.ui.text_username.setText(Settings.DB_USERNAME)
        if once: self.ui.text_password.setText(Settings.DB_PASSWORD)
        if once: self.ui.text_db.setText(Settings.DB_DB)

        try:
            con = pymysql.connect(host=db_host, user=db_user, password=db_password, db=db_db, charset='utf8mb4')
            cursor = con.cursor()
            self.ConnectedDB()
            self.CheckTableValid()
            if not Settings.IMPORTED: self.Table_Refresh()
        except:
            self.NotConnectedDB()
            QMessageBox.about(self, "Соединение с базой данных", "Нет подключения. \nПроверьте настройки.")

    def ConnectedDB(self):
        self.ui.label.setText("Соединение установлено")
        self.ui.label.setStyleSheet("color: lime")
        self.ui.btn_db_connector.setText("Отключить")
        self.ui.btn_db_loadconfig.setVisible(False)
        self.ui.btn_db_save.setVisible(True)

        self.ui.text_host.setEnabled(False)
        self.ui.text_username.setEnabled(False)
        self.ui.text_password.setEnabled(False)
        self.ui.text_db.setEnabled(False)

    def NotConnectedDB(self):
        self.ui.label.setText("Соединение отсутствует")
        self.ui.label.setStyleSheet("color: red")
        self.ui.btn_db_loadconfig.setVisible(True)
        self.ui.btn_db_save.setVisible(False)
        self.ui.btn_db_connector.setText("Подключить")
        self.ui.text_host.setEnabled(True)
        self.ui.text_username.setEnabled(True)
        self.ui.text_password.setEnabled(True)
        self.ui.text_db.setEnabled(True)
        self.ui.text_host.setText("")
        self.ui.text_username.setText("")
        self.ui.text_password.setText("")
        self.ui.text_db.setText("")

    def CheckTableValid(self):
        sql = """CREATE TABLE IF NOT EXISTS ulan ( \
                       `id` INTEGER(11) NOT NULL AUTO_INCREMENT, \
                       `lastname` VARCHAR(64) NOT NULL, \
                       `firstname` VARCHAR(64) NOT NULL, \
                       `middlename` VARCHAR(64) NOT NULL, \
                       `gender` VARCHAR(64) NOT NULL, \
                       `age` VARCHAR(64) NOT NULL, \
                       `phone_number` VARCHAR(64) NOT NULL, \
                       `city` VARCHAR(255) NOT NULL, \
                       PRIMARY KEY (id) \
                   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin \
                   AUTO_INCREMENT=1;"""

        cursor.execute(sql)

    def LoadDBFromConfig(self):
        ConfigFile()
        ConfigFile.loadConfig(Settings)

        self.ui.text_host.setText(Settings.DB_HOST)
        self.ui.text_username.setText(Settings.DB_USERNAME)
        self.ui.text_password.setText(Settings.DB_PASSWORD)
        self.ui.text_db.setText(Settings.DB_DB)

    def SaveDBFromConfig(self):
        if not con.open:
            QMessageBox.about(self, "Сохранение конфигурации", "Сначала нужно подключиться к Базе Данных!")
            return

        ConfigFile.config.set("database_connect", "host", self.ui.text_host.text())
        ConfigFile.config.set("database_connect", "username", self.ui.text_username.text())
        ConfigFile.config.set("database_connect", "password", self.ui.text_password.text())
        ConfigFile.config.set("database_connect", "db", self.ui.text_db.text())

        with open("config.ini", "w") as config_file:
            ConfigFile.config.write(config_file)

        ConfigFile.loadConfig(Settings)

        QMessageBox.about(self, "Сохранение конфигурации", "Конфигурация успешно сохранена!")

    def button_DataBaseClick(self):
        try:
            if con.open:
                con.close()
                cursor.close()
                self.NotConnectedDB()
                if not Settings.IMPORTED: self.ui.tableWidget_2.setRowCount(0)
                QMessageBox.about(self, "Соединение с базой данных", "Успешно отключились от Базы Данных!")
                return
        except:
            QMessageBox.about(self, "Соединение с базой данных", "Не удалось подключиться к Базе Данных!")

        self.ConnectToDatabase(False)

    def validate_person_data(self, lastname, firstname, middlename, age, phone_number, city):
        """Validate person data fields"""
        if not lastname.isalpha() or lastname.isspace() or not lastname.istitle():
            return False, "Фамилия указана не верно!"
        if not firstname.isalpha() or firstname.isspace() or not firstname.istitle():
            return False, "Имя указано не верно!"
        if not middlename.isalpha() or middlename.isspace() or not middlename.istitle():
            return False, "Отчество указано не верно!"
        if not age.isnumeric() or age.isspace():
            return False, "Возраст указан не верно!"
        if not phone_number.isnumeric() or phone_number.isspace():
            return False, "Сотовый указан не верно!"
        if not city.isalpha() or city.isspace() or not city.istitle():
            return False, "Город указан не верно!"
        if int(age) < 1 or int(age) > 122:
            return False, "Введите корректный возраст!"
        if len(phone_number) < 6 or len(phone_number) > 16:
            return False, "Введите корректный сотовый!"
        return True, ""

    def cellClicked(self, row, column):
        self.ui.text_id.setText(str(self.ui.tableWidget_2.item(row, 0).text()))
        self.ui.text_lastname.setText(str(self.ui.tableWidget_2.item(row, 1).text()))
        self.ui.text_firstname.setText(str(self.ui.tableWidget_2.item(row, 2).text()))
        self.ui.text_middlename.setText(str(self.ui.tableWidget_2.item(row, 3).text()))
        self.ui.box_gender.setCurrentIndex(0 if self.ui.tableWidget_2.item(row, 4).text() == "Мужской" else 1)
        self.ui.text_age.setText(str(self.ui.tableWidget_2.item(row, 5).text()))
        self.ui.text_phone.setText(str(self.ui.tableWidget_2.item(row, 6).text()))
        self.ui.text_city.setText(str(self.ui.tableWidget_2.item(row, 7).text()))

    def table_SortFunction(self):
        self.ui.tableWidget_2.sortItems(self.ui.box_sort.currentIndex())

    def Table_Refresh(self):
        self.ui.leftFrame.setVisible(True)
        self.ui.table_upFrame.setVisible(True)
        self.ui.btn_table_refresh.setText("Обновить")
        Settings.IMPORTED = False
        self.ui.label_name_import.setText("")

        try:
            if not con.open:
                return
        except:
            self.NotConnectedDB()
            QMessageBox.about("Обновление таблицы", "Нет подключения к БД")
            return

        try:
            cursor.execute("select count(*) from ulan")
            number = list(cursor)
        except:
            QMessageBox.about(self, "Обновление таблицы", "Нет записей в таблице!")
            return

        rowcount = number[0][0]
        colcount = 8

        self.ui.tableWidget_2.setRowCount(rowcount)

        try:
            cursor.execute("select * from ulan")
            datas = cursor.fetchall()
        except con.Error as Err:
            print("Ошибка", Err)
            return

        for i in range(rowcount):
            for j in range(colcount):
                self.ui.tableWidget_2.setItem(i, j, QTableWidgetItem(str(datas[i][j])))

        self.ui.box_sort.setCurrentIndex(0)

    def find_SelectFunction(self):
        self.ui.box_gender_select.setCurrentIndex(0)
        if self.ui.box_find.currentIndex() == 4:
            self.ui.box_gender_select.setVisible(True)
            self.ui.text_find.setVisible(False)
        else:
            self.ui.box_gender_select.setVisible(False)
            self.ui.text_find.setVisible(True)

    def text_PressedFunction(self):
        id = self.ui.text_id.text()
        self.text_CleanFunction()
        self.ui.text_id.setText(id)

        try:
            cursor.execute("select * from ulan where id = %s", id)
            datas = cursor.fetchall()

            self.ui.text_lastname.setText(datas[0][1])
            self.ui.text_firstname.setText(datas[0][2])
            self.ui.text_middlename.setText(datas[0][3])
            self.ui.box_gender.setCurrentIndex(0 if datas[0][4] == "Мужской" else 1)
            self.ui.text_age.setText(datas[0][5])
            self.ui.text_phone.setText(datas[0][6])
            self.ui.text_city.setText(datas[0][7])
        except:
            QMessageBox.about(self, "Поиск по коду", "Нет записи по этому коду")

    def text_CleanFunction(self):
        self.ui.text_id.setText("")
        self.ui.text_lastname.setText("")
        self.ui.text_firstname.setText("")
        self.ui.text_middlename.setText("")
        self.ui.box_gender.setCurrentIndex(0)
        self.ui.text_age.setText("")
        self.ui.text_phone.setText("")
        self.ui.text_city.setText("")

    def find_CleanFunction(self):
        self.ui.box_find.setCurrentIndex(0)
        self.ui.text_find.setText("")
        self.find_SelectFunction()

    def Find_Function(self):
        try:
            if not con.open:
                return
        except:
            QMessageBox.about("Поиск записи", "Нет подключения к БД")
            return

        text_find = self.ui.text_find.text()
        selected_index = self.ui.box_find.currentIndex()

        if text_find.isspace() or text_find == '' and not self.ui.box_find.currentIndex() == 4:
            QMessageBox.about(self, "Поиск записи", "Введите хоть что-нибудь!")
            return

        rofl = text_find
        text_find = '%' + rofl + '%'

        try:
            if selected_index == 0:
                cursor.execute('select count(*) from ulan where id like %s', text_find)
                number = list(cursor)
                cursor.execute('select *from ulan where id like %s', text_find)
            elif selected_index == 1:
                cursor.execute("select count(*) from ulan where lastname like %s", text_find)
                number = list(cursor)
                cursor.execute("select *from ulan where lastname like %s", text_find)
            elif selected_index == 2:
                cursor.execute('select count(*) from ulan where firstname like %s', text_find)
                number = list(cursor)
                cursor.execute('select *from ulan where firstname like %s', text_find)
            elif selected_index == 3:
                cursor.execute('select count(*) from ulan where middlename like %s', text_find)
                number = list(cursor)
                cursor.execute('select *from ulan where middlename like %s', text_find)
            elif selected_index == 4:
                cursor.execute('select count(*) from ulan where gender like %s', self.ui.box_gender_select.currentText())
                number = list(cursor)
                cursor.execute('select *from ulan where gender like %s', self.ui.box_gender_select.currentText())
            elif selected_index == 5:
                cursor.execute('select count(*) from ulan where age like %s', text_find)
                number = list(cursor)
                cursor.execute('select *from ulan where age like %s', text_find)
            elif selected_index == 6:
                cursor.execute('select count(*) from ulan where phone_number like %s', text_find)
                number = list(cursor)
                cursor.execute('select *from ulan where phone_number like %s', text_find)
            elif selected_index == 7:
                cursor.execute('select count(*) from ulan where city like %s', text_find)
                number = list(cursor)
                cursor.execute('select *from ulan where city like %s', text_find)
        except:
            QMessageBox.about(self, "Поиск записи", "Не удалось найти запись!")
            return

        datas = cursor.fetchall()
        colcount = 8

        rowcount = number[0][0]

        self.ui.tableWidget_2.setRowCount(rowcount)

        if rowcount < 1:
            QMessageBox.about(self, "Поиск записи", "Данные не найдены!")
            return

        for i in range(rowcount):
            for j in range(colcount):
                self.ui.tableWidget_2.setItem(i, j, QTableWidgetItem(str(datas[i][j])))

    def Remove_Function(self):
        try:
            if not con.open:
                return
        except:
            QMessageBox.about("Удаление записи", "Нет подключения к БД")
            return

        id = self.ui.text_id.text()

        if id.isspace() or not id.isdigit():
            QMessageBox.about(self, "Удаление записи", "Укажите код!")
            return

        try: # id_found вызывает ошибку и тригерит except
            cursor.execute("select id from ulan where id = %s", id)
            number = cursor.fetchall()
            id_found = number[0][0]
            sql = 'delete from ulan where id=%s'
            cursor.execute(sql, (id))
            con.commit()
            self.text_CleanFunction()
            self.Table_Refresh()
            QMessageBox.about(self, "Удаление записи", "Запись успешно удалена!")
        except:
            QMessageBox.about(self, "Удаление записи", "Не удалось удалить запись!")

    def Update_Function(self):
        try:
            if not con.open:
                return
        except:
            QMessageBox.about("Изменение записи", "Нет подключения к БД")
            return

        id = self.ui.text_id.text()

        lastname = self.ui.text_lastname.text()
        firstname = self.ui.text_firstname.text()
        middlename = self.ui.text_middlename.text()
        gender = self.ui.box_gender.currentText()
        age = self.ui.text_age.text()
        phone_number = self.ui.text_phone.text()
        city = self.ui.text_city.text()

        if id.isspace() or not id.isdigit():
            QMessageBox.about(self, "Изменение записи", "Укажите код!")
            return

        try: # id_found вызывает ошибку и тригерит except
            cursor.execute("select id from ulan where id = %s", id)
            number = cursor.fetchall()
            id_found = number[0][0]
        except:
            QMessageBox.about(self, "Изменение записи", "Такого кода не существует")
            return

        # Validate input data
        is_valid, error_message = self.validate_person_data(lastname, firstname, middlename, age, phone_number, city)
        if not is_valid:
            QMessageBox.about(self, "Изменение записи", error_message)
            return

        try:
            sql = 'update ulan set lastname=%s, firstname=%s, middlename=%s, gender=%s, age=%s, phone_number=%s, city=%s where id=%s'
            cursor.execute(sql, (lastname, firstname, middlename, gender, age, phone_number, city, id))
            con.commit()
            self.text_CleanFunction()
            self.Table_Refresh()
            QMessageBox.about(self, "Изменение записи", "Запись успешно изменена!")
        except:
            QMessageBox.about(self, "Изменение записи", "Не удалось изменить запись!")

    def Append_Function(self):
        try:
            if not con.open:
                return
        except:
            QMessageBox.about("Добавление записи", "Нет подключения к БД")
            return

        lastname = self.ui.text_lastname.text()
        firstname = self.ui.text_firstname.text()
        middlename = self.ui.text_middlename.text()
        gender = self.ui.box_gender.currentText()
        age = self.ui.text_age.text()
        phone_number = self.ui.text_phone.text()
        city = self.ui.text_city.text()

        # Validate input data
        is_valid, error_message = self.validate_person_data(lastname, firstname, middlename, age, phone_number, city)
        if not is_valid:
            QMessageBox.about(self, "Добавление записи", error_message)
            return

        try:
            sql = 'insert into ulan (`lastname`, `firstname`, `middlename`, `gender`, `age`, `phone_number`, `city`) VALUES(%s, %s, %s, %s, %s, %s, %s)'
            cursor.execute(sql, (lastname, firstname, middlename, gender, age, phone_number, city))
            con.commit()
            self.text_CleanFunction()
            self.Table_Refresh()
            QMessageBox.about(self, "Добавление записи", "Запись успешно добавлена!")
        except:
            QMessageBox.about(self, "Добавление записи", "Не удалось добавить запись!")
        return

    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
