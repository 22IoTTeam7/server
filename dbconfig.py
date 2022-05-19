import pymysql
import numpy as np


class dbcontroller:
    def __init__(self, host, id, pw, db_name):
        self.conn = pymysql.connect(host=host, user=id, password=pw, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()
        pass

    def insert_floor2(self, AP):
        sql='INSERT INTO Floor2 (AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10, AP11, AP12, AP13, AP14, AP15, AP16, ' \
            'AP17, AP18, AP19, AP20, AP21, AP22, AP23, AP24, AP25, AP26, AP27, AP28, AP29, AP30, AP31, AP32, AP33, Room) ' \
            'VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        self.curs.execute(sql, (AP[0], AP[1], AP[2], AP[3], AP[4], AP[5], AP[6], AP[7], AP[8], AP[9], AP[10],
                                AP[11], AP[12], AP[13], AP[14], AP[15], AP[16], AP[17], AP[18], AP[19], AP[20],
                                AP[21], AP[22], AP[23], AP[24], AP[25], AP[26], AP[27], AP[28], AP[29], AP[30],
                                AP[31], AP[32], AP[33]))
        self.conn.commit()

    def insert_floor4(self, AP2):
        sql = 'INSERT INTO Floor4 (AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10, AP11, AP12, AP13, AP14, AP15, AP16, ' \
              'AP17, AP18, AP19, AP20, AP21, AP22, AP23, AP24, AP25, AP26, AP27, AP28, AP29, AP30, AP31, AP32, AP33, AP34, ' \
              'AP35, AP36, AP37, AP38, AP39, AP40, AP41, AP42, AP43, AP44, Room) ' \
              'VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
              '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' \
              ', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        self.curs.execute(sql, (AP2[0], AP2[1], AP2[2], AP2[3], AP2[4], AP2[5], AP2[6], AP2[7], AP2[8], AP2[9], AP2[10],
                                AP2[11], AP2[12], AP2[13], AP2[14], AP2[15], AP2[16], AP2[17], AP2[18], AP2[19], AP2[20],
                                AP2[21], AP2[22], AP2[23], AP2[24], AP2[25], AP2[26], AP2[27], AP2[28], AP2[29], AP2[30],
                                AP2[31], AP2[32], AP2[33], AP2[34], AP2[35], AP2[36], AP2[37], AP2[38], AP2[39], AP2[40],
                                AP2[41], AP2[42], AP2[43], AP2[44]))
        self.conn.commit()

    def insert_floor5(self, AP2):
        sql = 'INSERT INTO Floor5 (AP1, AP2, AP3, AP4, AP5, AP6, AP7, AP8, AP9, AP10, AP11, AP12, AP13, AP14, AP15, AP16, ' \
              'AP17, AP18, AP19, AP20, AP21, AP22, AP23, AP24, AP25, AP26, AP27, AP28, AP29, AP30, AP31, AP32, AP33, AP34, ' \
              'AP35, AP36, AP37, AP38, AP39, AP40, AP41, AP42, AP43, AP44, AP45, AP46, AP47, AP48, AP49, Room) ' \
              'VALUE (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, ' \
              '%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s' \
              ', %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

        self.curs.execute(sql, (AP2[0], AP2[1], AP2[2], AP2[3], AP2[4], AP2[5], AP2[6], AP2[7], AP2[8], AP2[9],
                                AP2[10], AP2[11], AP2[12], AP2[13], AP2[14], AP2[15], AP2[16], AP2[17], AP2[18],
                                AP2[19], AP2[20], AP2[21], AP2[22], AP2[23], AP2[24], AP2[25], AP2[26], AP2[27],
                                AP2[28], AP2[29], AP2[30], AP2[31], AP2[32], AP2[33], AP2[34], AP2[35], AP2[36],
                                AP2[37], AP2[38], AP2[39], AP2[40], AP2[41], AP2[42], AP2[43], AP2[44], AP2[45],
                                AP2[46], AP2[47], AP2[48], AP2[49]))
        self.conn.commit()
