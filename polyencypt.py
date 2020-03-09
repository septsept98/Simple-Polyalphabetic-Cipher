abjad=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

pesan = input('Masukan Pesan : ')   # input pesan/plaint text
pesan = pesan.lower()   # pesan berupa huruf kecil

kunci = input('Masukan Kunci : ')   # input kunci/key
kunci = kunci.lower()   # kunci berupa huruf kecil
kunci = kunci*len(pesan)    # agar panjang kunci sama dengan panjang pesan

print('=== Enkripsi Polyalphabetic Cipher ===')
cipherText = ''
i = 0
for letter in pesan:        # perulangan sepanjang pesan yang dimasukkan
    if letter in abjad:         # apakah pesan termasuk dalam abjad
        angkapesan = abjad.index(letter)    # menjadikan huruf pesan menjadi angka
        angkakunci = abjad.index(kunci[i])  # menjadikan huruf kunci menjadi angka
        cipher = (angkapesan + angkakunci) % 26   # melakukan enkripsi
        cipherHuruf = abjad[cipher]     # menghurufkan hasil enkripsi
        cipherText = cipherText + cipherHuruf   # menggabungkan hasil enkripsi
        i = i+1
    else:
        cipherText = cipherText + letter   # menggabungkan hasil enkripsi jika terdapat spasi pada pesan

print('Pesan Enkripsi : '+cipherText)   # menampilkan hasil enkripsi

print('=== Dekripsi Polyalphabetic Cipher ===')
i = 0
plaintText = ''
for letter in cipherText:        # perulangan sepanjang pesan enkripsi
    if letter in abjad:         # apakah pesan enkripsi termasuk dalam abjad
        angkacipher = abjad.index(letter)   # menjadikan huruf enkripsi menjadi angka
        angkakunci = abjad.index(kunci[i])  # menjadikan huruf kunci menjadi angka
        plaint = (angkacipher - angkakunci) % 26   # melakukan dekripsi
        plaintHuruf = abjad[plaint]     # menghurufkan hasil dekripsi
        plaintText = plaintText + plaintHuruf   # menggabungkan hasil dekripsi
        i = i+1
    else:
        plaintText = plaintText + letter   # menggabungkan hasil dekripsi jika terdapat spasi pada pesan

print('Pesan Dekripsi : '+plaintText)