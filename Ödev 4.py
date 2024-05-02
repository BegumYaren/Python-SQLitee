import sqlite3
import difflib

# SQLite veritabanına bağlanın veya oluşturun
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# Eğer tablo yoksa oluşturun
cursor.execute('''
CREATE TABLE IF NOT EXISTS texts (
    id INTEGER PRIMARY KEY,
    text1 TEXT,
    text2 TEXT
)
''')

# Kullanıcıdan iki metin alın
text1 = input("Lütfen ilk metni girin: ")
text2 = input("Lütfen ikinci metni girin: ")

# Metinleri veritabanına ekleyin
cursor.execute('INSERT INTO texts (text1, text2) VALUES (?, ?)', (text1, text2))
conn.commit()

# Benzerlik oranını hesaplayın
similarity_ratio = difflib.SequenceMatcher(None, text1, text2).ratio()

# Benzerlik oranını ekrana yazdırın
print(f"Benzerlik oranı: {similarity_ratio:.2%}")

# Benzerlik oranını 'benzerlik_durumu.txt' dosyasına kaydedin
try:
    with open('benzerlik_durumu.txt', 'w') as file:
        file.write(f"Metinler arasındaki benzerlik oranı: {similarity_ratio:.2%}\n")
    print("Benzerlik durumu dosyaya başarıyla yazıldı.")
except Exception as e:
    print(f"Dosyaya yazma hatası: {e}")

# Bağlantıyı ve cursor'ı kapatın
cursor.close()
conn.close()
