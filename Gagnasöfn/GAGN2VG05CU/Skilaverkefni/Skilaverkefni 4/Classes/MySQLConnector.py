import pymysql.cursors

class MySQLConnector():
    def __init__(self, net_thjonn, notandi, adgangsord, gagnagrunnur):
        try:
            self.connection = pymysql.connect(
                host=net_thjonn,
                user=notandi,
                password=adgangsord,
                db=gagnagrunnur,
                charset='utf8mb4',
                cursorclass=pymysql.cursors.DictCursor,
                autocommit=True
            )
        except RuntimeError:
            self.__criticalError("Incorrect Password")
            
    def __criticalError(self, error_msg):
        print("MySQL Connector critical error:",error_msg)
        print("Shutting down")
        exit()

    def run(self, sql):

        try:
            cursor = self.connection.cursor()
            cursor.execute(sql)
            result = cursor.fetchall()
            cursor.close()
        except Exception as error:
            print(error)
            result = None

        return result
