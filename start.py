import sqlite3
conn = sqlite3.connect('blog.db')
conn.execute("CREATE TABLE blog_table (blog_id INTEGER PRIMARY KEY, blog_title char(100) NOT NULL, blog_body char(100) NOT NULL)")
conn.execute("INSERT INTO blog_table (blog_title, blog_body) VALUES ('First post title','First post body')")
conn.commit()