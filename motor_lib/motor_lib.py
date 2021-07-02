
# -*- coding: utf-8 -*-
# Time : 2021/5/12 13:53 PM
# Author : Shaojie Liu
# Email : jielness@zju.edu.cn
# Tel : 18868112367


from serial import Serial
from struct import pack
from time import sleep


class Motor:
    def __init__(self, serial='COM4', type1='CEM-FPM', type2='CEM-FPM'):
        self.mtype = ('CEM-FPM', 'EM-FPM')
        self.PSClib = [24153.6, 37781.28]
        self.state = 0
        self.motor1_pos = 0
        self.motor2_pos = 0
        self.motor1_angle = 0
        self.motor2_angle = 0
        if type1 == self.mtype[0]:
            self.SPC1 = self.PSClib[0]
        elif type1 == self.mtype[1]:
            self.SPC1 = self.PSClib[1]
        else:
            self.SPC1 = self.PSClib[0]

        if type2 == self.mtype[0]:
            self.SPC2 = self.PSClib[0]
        elif type2 == self.mtype[1]:
            self.SPC2 = self.PSClib[1]
        else:
            self.SPC2 = self.PSClib[0]

        self.motor = Serial(serial, 9600, timeout=0.5)
        self.state = 1
        temp_str = ''
        while temp_str != 'END\r\n':
            temp_str = self.motor.readline().decode('ascii')
        sleep(0.5)
        self.get_pos(1)
        self.get_pos(2)
        print('Please connect Mr.Liu if you meet problem or want to buy it.')
        print('Wechat: jilness, Tel: 18868112367')
        print('Motor Connected!')

    def run(self, motor_num=1, angle=0, ifprint=False, ):
        if motor_num == 1:
            steps = int(angle * self.SPC1 / 360)
            cmd = 'a'.encode('ascii') + pack('i', steps)
        elif motor_num == 2:
            steps = int(angle * self.SPC2 / 360)
            cmd = 'b'.encode('ascii') + pack('i', steps)
        else:
            return 0
        self.sendcmd(cmd)
        self.get_pos(motor_num, ifprint)
        if ifprint:
            print('Motor Rotation finished!')
        return 1

    def run_continue(self, motor_num=1, state=1,):
        if state == 1:
            if motor_num == 1:
                cmd = ('e'.encode('ascii') + pack('i', 0))
            elif motor_num == 2:
                cmd = ('h'.encode('ascii') + pack('i', 0))
            else:
                return 0
            self.sendcmd(cmd)
            return 1
        elif state == -1:
            if motor_num == 1:
                cmd = ('f'.encode('ascii') + pack('i', 0))
            elif motor_num == 2:
                cmd = ('i'.encode('ascii') + pack('i', 0))
            else:
                return 0
            self.sendcmd(cmd)
            return 1
        elif state == 0:
            if motor_num == 1:
                cmd = ('g'.encode('ascii') + pack('i', 0))
            elif motor_num == 2:
                cmd = ('j'.encode('ascii') + pack('i', 0))
            else:
                return 0
            self.sendcmd(cmd)
            if motor_num == 1:
                self.get_pos(1)
            elif motor_num == 2:
                self.get_pos(2)
            else:
                return 0
            return 1
        else:
            return 0

    def reset(self, motor_num=1, ifprint=False, ):
        if motor_num == 1:
            self.run(motor_num, -self.motor1_angle, ifprint)
        elif motor_num == 2:
            self.run(motor_num, -self.motor2_angle, ifprint)

    def get_pos(self, motor_num=1, ifprint=False, ):
        if motor_num == 1:
            cmd = 'c'.encode('ascii') + pack('i', 0)
        elif motor_num == 2:
            cmd = 'd'.encode('ascii') + pack('i', 0)
        else:
            return 0
        value = self.sendcmd(cmd)
        pos = value[0]
        if len(pos):
            if motor_num == 1:
                self.motor1_pos = int(pos)
                self.motor1_angle = 360 * self.motor1_pos / self.SPC1
            elif motor_num == 2:
                self.motor2_pos = int(pos)
                self.motor2_angle = 360 * self.motor2_pos / self.SPC2
        if ifprint:
            if motor_num == 1:
                print(f'Motor 1 position: {self.motor1_angle}')
            elif motor_num == 2:
                print(f'Motor 2 position: {self.motor2_angle}')
        return 1

    def save_pos(self, ifprint=False, ):
        cmd = 'k'.encode('ascii') + pack('i', 0)
        self.sendcmd(cmd)
        if ifprint:
            print(f'Save Position to EEPROM!')

    def clear_pos(self, motor_num=1, ifprint=False, ):
        if motor_num == 1:
            cmd = 'l'.encode('ascii') + pack('i', 0)
        elif motor_num == 2:
            cmd = 'm'.encode('ascii') + pack('i', 0)
        else:
            return 0
        self.sendcmd(cmd)
        if ifprint:
            print(f'Clear Motor {motor_num} Data!')
        return 1

    def sendcmd(self, cmd):
        self.motor.write(cmd)
        value = list()
        temp_str = ''
        while temp_str != 'END\r\n':
            temp_str = self.motor.readline().decode('ascii')
            if len(temp_str) != 0 and temp_str != 'END\r\n':
                value.append(temp_str.split()[0])
        return value

    def disconnect(self, ):
        if self.state == 1:
            self.save_pos(True)
            self.motor.close()
            self.state = 0

    def __del__(self):
        if self.state == 1:
            self.save_pos(True)
            self.motor.close()
            self.state = 0
