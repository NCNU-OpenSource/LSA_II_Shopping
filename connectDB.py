import pymysql

try:
    mydb = pymysql.connect(
        host="localhost",   # 資料庫主機地址
        user="root",        # 資料庫使用者名稱
        passwd="",    # 資料庫密碼
        database="lsa2"   # 直連資料庫，如果資料庫不存在，會輸出錯誤資訊
    )
    # 生成一個遊標物件(相當於cmd開啟mysql中的 mysql>)
    cursor = mydb.cursor(cursor=pymysql.cursors.DictCursor)  # 讓資料自動組織成字典
    
    # print("連線結果", mydb) # 印出連線結果
except:
    print("資料庫連接失敗：")