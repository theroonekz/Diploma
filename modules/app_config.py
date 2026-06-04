import os
import configparser

class ConfigFile():
    config = configparser.ConfigParser()

    def createConfig(path):
        if os.path.exists(path):
            return

        ConfigFile.config.add_section("database_connect")
        ConfigFile.config.add_section("theme_style")
        ConfigFile.config.add_section("titlebar")

        ConfigFile.config.set("database_connect", "host", "localhost")
        ConfigFile.config.set("database_connect", "username", "your_username")
        ConfigFile.config.set("database_connect", "password", "your_password")
        ConfigFile.config.set("database_connect", "db", "your_database")

        ConfigFile.config.set("theme_style", "default_style", "dark")
        ConfigFile.config.set("titlebar", "use_custom_titlebar", "True")

        with open("config.ini", "w") as config_file:
            ConfigFile.config.write(config_file)

    def checkExists(path):
        ConfigFile.config.read("config.ini")

        if not ConfigFile.config.has_section("database_connect"): ConfigFile.config.add_section("database_connect")
        if not ConfigFile.config.has_section("theme_style"): ConfigFile.config.add_section("theme_style")
        if not ConfigFile.config.has_section("titlebar"): ConfigFile.config.add_section("titlebar")

        if not ConfigFile.config.has_option("database_connect", "host"): ConfigFile.config.set("database_connect", "host", "localhost")
        if not ConfigFile.config.has_option("database_connect", "username"): ConfigFile.config.set("database_connect", "username", "username")
        if not ConfigFile.config.has_option("database_connect", "password"): ConfigFile.config.set("database_connect", "password", "password")
        if not ConfigFile.config.has_option("database_connect", "db"): ConfigFile.config.set("database_connect", "db", "db")

        if not ConfigFile.config.has_option("theme_style", "default_style"): ConfigFile.config.set("theme_style", "default_style", "dark")
        if not ConfigFile.config.has_option("titlebar", "use_custom_titlebar"): ConfigFile.config.set("titlebar", "use_custom_titlebar", "True")

        with open("config.ini", "w") as config_file:
            ConfigFile.config.write(config_file)

    def loadConfig(self):
        ConfigFile.createConfig("config.ini")
        ConfigFile.checkExists("config.ini")
        ConfigFile.config.read("config.ini")
        # Loading = DATABASE
        self.DB_HOST = ConfigFile.config["database_connect"]["host"]
        self.DB_USERNAME = ConfigFile.config["database_connect"]["username"]
        self.DB_PASSWORD = ConfigFile.config["database_connect"]["password"]
        self.DB_DB = ConfigFile.config["database_connect"]["db"]

        # Loading = THEME
        self.THEME_STYLE = ConfigFile.config["theme_style"]["default_style"]

        # Loading = TITLEBAR
        self.ENABLE_CUSTOM_TITLE_BAR = (False if ConfigFile.config["titlebar"]["use_custom_titlebar"] == 'False' else True)