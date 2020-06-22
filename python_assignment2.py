import sqlite3

fileList = ('information.docx', 'Hello.txt', 'myImage.png', \
    'myMovie.mpg', 'Word.txt', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('files.db')


with conn:
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS tbl_filetypes(\
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        fileName TEXT\
        )')
    conn.commit()
conn.close()


for i in fileList:
    if i.endswith('.txt'):
        conn = sqlite3.connect('files.db')
        cur = conn.cursor()
        cur.execute("INSERT INTO tbl_filetypes(fileName) VALUES (?)",\
            [i])
        conn.commit()
        conn.close()
    else:
        pass


conn = sqlite3.connect('files.db')
with conn:
    cur = conn.cursor()
    cur.execute("SELECT * FROM tbl_filetypes")
    varFile = cur.fetchall()
    for item in varFile:
        msg = "The file type is {}".format(item)
        print(msg)
conn.close()
