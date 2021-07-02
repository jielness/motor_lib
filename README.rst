
motor_lib
====

电机控制库

object = Motor(serial='COM4', type1='CEM-FPM', type2='CEM-FPM')

    功能：创建电机实例

    serial 端口号

    type1 MOTOR1端口连接的电机类型，'CEM-FPM'表示30mm同轴电机，'EM-FPM'表示自由空间电机

    type2 MOTOR2端口连接的电机类型，'CEM-FPM'表示30mm同轴电机，'EM-FPM'表示自由空间电机


def run(motor_num=1, angle=30, ifprint=False, )

    功能：使电机旋转

    motor_num 电机编号，1是MOTOR1，2是MOTOR2

    angle 旋转角度，正值顺时针旋转，负值逆时针旋转

    ifprint 执行完操作是否打印：Motor Rotation finished!，True打印，False不打印

    返回值 1表示命令正确并顺利执行，0表示命令错误没有执行


def run_continue(motor_num=1, state=1,)

    功能：使电机连续旋转

    motor_num 电机编号，1是MOTOR1，2是MOTOR2

    state 电机状态，1表示连续顺时针旋转，-1表示连续逆时针旋转，0表示停止旋转

    返回值 1表示命令正确并顺利执行，0表示命令错误没有执行


def reset(motor_num=1, ifprint=False, )

    功能：使电机复位

    motor_num 电机编号，1是MOTOR1，2是MOTOR2

    ifprint 执行完操作是否打印：Motor Rotation finished!，True打印，False不打印

    无返回值


def get_pos(motor_num=1, ifprint=False, )

    功能：获取电机位置

    motor_num 电机编号，1是MOTOR1，2是MOTOR2

    ifprint 是否打印电机位置，True打印，False不打印

    返回值 1表示命令正确并顺利执行，0表示命令错误没有执行


def save_pos(ifprint=False, )

    功能：把电机当前位置记录在EEPROM中（相当于硬盘，下次连接自动读取），这个功能用于断开连接前执行

    ifprint 执行完操作是否打印：Save Position to EEPROM!，True打印，False不打印

    无返回值


def clear_pos(motor_num, ifprint=False, )

    功能：清空EEPROM数据（相当于清空硬盘），这个功能用于重新设置电机位置的时候使用

    motor_num 电机编号，1是MOTOR1，2是MOTOR2

    ifprint 是否打印操作提示，True打印，False不打印

    返回值 1表示命令正确并顺利执行，0表示命令错误没有执行


def disconnect()

    功能：断开连接，自动执行save_pos()函数




