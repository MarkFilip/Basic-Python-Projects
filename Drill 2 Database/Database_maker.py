import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

conn = sqlite3.connect('test.db')

# Create Table with a primary key and a file name column

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files ( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        file_name TEXT \
        )")
    conn.commit()
conn.close

# Create a list with all the txt files from file_List
# then pass those values to the database

with conn:
    cur = conn.cursor()
    textList=[]
    for i in fileList:
        if i.endswith('.txt') == True:
            textList.append(i)
    for t in textList:    
        cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                        [t]) 
    conn.commit()
conn.close

# Query those file names from the database and print
# them

with conn:
    cur = conn.cursor()
    cur.execute("SELECT file_name FROM tbl_files")
    varFiles = cur.fetchall()
    for item in varFiles:
        msg = "File Name: {}".format(item[0])
        print(msg)
        









        
