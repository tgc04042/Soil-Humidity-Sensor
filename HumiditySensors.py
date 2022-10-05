
import serial
import pymysql
import requests
from time import sleep
import re

senPort = serial.Serial('dev/ttyACM0', 9600)
fcPort = serial.Serial('dev/ttyACM1', 9600)
chopPort = serial.Serial('dev/ttyACM2', 9600)
vacuumPort = serial.Serial('dev/ttyACM3', 9600)
senPort.lushInput()
fcPort.flushInput()
chopPort.flushInput()
vacuumPort.flushInput()



class MysqlController:
    def __init__(self,host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()
        self.curs.execute('create table SEN0114(s_date, soil_humi)')
        self.curs.execute('create table FC_28(s_date, soil_humi)')
        self.curs.execute('create table Chopsticks(s_date, soil_humi)')
        self.curs.execute('create table VacuumChopsticks(s_date, soil_humi)')

    def insert_sen0114(self,s_num, data_value):

        try:
            with self.conn.cursor() as self.curs:
                sql = 'insert into SEN0114 values (%s, %s)'
                self.curs.execute(sql, (s_num, data_value))
                self.conn.commit()
        finally:
            self.conn.close()

    def insert_fc_28(self, s_num, data_value):

        try:
            with self.conn.cursor() as self.curs:
                sql = 'insert into SEN0114 values (%s, %s)'
                self.curs.execute(sql, (s_num, data_value))
                self.conn.commit()
        finally:
            self.conn.close()

    def insert_chopsticks(self, s_num, data_value):

        try:
            with self.conn.cursor() as self.curs:
                sql = 'insert into SEN0114 values (%s, %s)'
                self.curs.execute(sql, (s_num, data_value))
                self.conn.commit()
        finally:
            self.conn.close()

    def insert_vacuumchopsticks(self, s_num, data_value):

        try:
            with self.conn.cursor() as self.curs:
                sql = 'insert into SEN0114 values (%s, %s)'
                self.curs.execute(sql, (s_num, data_value))
                self.conn.commit()
        finally:
            self.conn.close()




if __name__== "__main__":
    sqlCon = MysqlController.__init__('203.250.32.41', 'pi', 'wogns5839', 'HumiditySensor')

    i=0
    j=0

    while 1:
        if i>0:
            break

        for j in range(0,7200):
            sen0114 = senPort.readline()
            sqlCon.insert_sen0114(j, sen0114)

            fc28 = fcPort.readline()
            sqlCon.insert_fc_28(j, fc28)

            chopsticks = chopPort.readline()
            sqlCon.insert_chopsticks(j, chopsticks)

            vacuumChopsticks = vacuumPort.readline()
            sqlCon.insert_vacuumchopsticks(j, vacuumChopsticks)

            i+=1
