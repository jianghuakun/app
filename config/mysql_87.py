import pymysql
class mysql_87():
    test1 = pymysql.connect(
        '106.52.222.87',
        'root',
        '123456',
        'test1',
        autocommit=True
    )


    test1_cursor = test1.cursor()
    #device_mycursor = device.cursor()
    #video_cursor=video.cursor()
    #activity_cursor = activity.cursor()
