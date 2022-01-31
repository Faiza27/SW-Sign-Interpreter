

import configparser
import MySQLdb.cursors


def connect():
    config = configparser.ConfigParser()
    config.read('config.ini')
    mysqlDB_config = config[MySQLdb]

    return MySQLdb.connect(host = mysqlDB_config['host'],
                           user = mysqlDB_config['user'],
                           passwd = mysqlDB_config['pass'],
                           db = mysqlDB_config['db'])
