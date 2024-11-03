print('='*60)
print('\t\t QUIZ BAHASA JEPANG')
print('='*60)

def permainan_baru():
    tebakan = []
    tebakan_benar = 0
    nomor_pertanyaan = 1

    for kunci in pertanyaan:
        print('='*80)
        print(kunci)
        for i in opsi[nomor_pertanyaan-1]:
            print(i)
        tebak = input('TEKAN ENTER (A, B, C, ATAU D): ')
        tebak = tebak.upper()
        tebakan.append(tebak)

        tebakan_benar += cek_jawaban(pertanyaan.get(kunci), tebak)
        nomor_pertanyaan += 1

    tampilkan_scor(tebakan_benar, tebakan)

def cek_jawaban(jawaban, tebak):
    if jawaban == tebak:
        print('\t\t\t=====BENAR!=====')
        return 1
    else:
        print('\t\t\t=====SALAH!=====')
        return 0

def tampilkan_scor(tebakan_benar, tebakan):
    print('='*60)
    print('\t\t\tHASIL')
    print('='*60)
    print('JAWABAN\t: ', end= ' ')
    for i in pertanyaan:
        print(pertanyaan.get(i), end= ' ')
    print()

    print('TEBAKAN\t: ', end= ' ')
    for i in tebakan:
        print(i, end= ' ')
    print()

    skor = int((tebakan_benar / len(pertanyaan)) * 100)
    print('SCOR\t: ' + str(skor) + '%')

def main_lagi():
    respons = input('\nApakah kamu mau bermain lagi?:\nya atau tidak: ')
    respons = respons.lower()

    if respons == 'ya':
        return True
    else:
        return False

pertanyaan = {
    "1. Bagaimana cara mengatakan Nama saya adalah dalam bahasa Jepang?: ": "A",
    "2. Apa arti dari salam ini? おはようございます ?: ": "B",
    "3. Bagaimana cara menanyakan -Siapa nama Anda?- dalam bahasa Jepang?: ": "C",
    "4. Bagaimana cara mengatakan -Saya berasal dari Indonesia- dalam bahasa Jepang?: ": "D",
    "5. Bagaimana cara mengatakan -Saya seorang guru- dalam bahasa Jepang?: ": "B",
    "6. Bagaimana cara menanyakan -Berapa umur Anda?- dalam bahasa Jepang?:": "C",
    "7. Bagaimana cara mengatakan -Hobi saya adalah membaca- dalam bahasa Jepang?:": "C",
    "8. Bagaimana cara mengatakan -Sekarang jam 3- dalam bahasa Jepang?: ": "B",
    "9. Bagaimana cara menanyakan -Hari ini tanggal berapa?- dalam bahasa Jepang?:":"C",
    "10. Apa arti dari -どこ- ?: ": "B",
}

opsi = [
    ['A. わたしのなまえは [nama Anda] です', 'B. わたしは [nama Anda] です', 'C. おはようございます', 'D. こんにちは'],
    ['A. Selamat malam', 'B. Selamat pagi', 'C. Selamat siang', 'D. Terima kasih'],
    ['A. あなたはだれですか？', 'B. あなたのしごとはなんですか？', 'C. あなたのなまえはなんですか？', 'D. あなたのかぞくは？'],
    ['A. わたしはインドネシアです', 'B. わたしはインドネシアじんです', 'C. わたしはインドネシアへいきます', 'D. わたしはインドネシアからきました'],
    ['A. わたしはがくせいです', 'B. わたしはせんせいです', 'C. わたしはかいしゃいんです', 'D. わたしはしゅふです'],
    ['A. あなたはどこにすんでいますか？', 'B. あなたはなんじですか？', 'C. あなたはなんさいですか？', 'D. あなたはなんねんせいですか？'],
    ['A. わたしのしゅみはうたいます', 'B. わたしのしゅみはえいがです', 'C. わたしのしゅみはどくしょです', 'D. わたしのしゅみはりょうりです'],
    ['A. いまはんじです', 'B. いまさんじです', 'C. いまろくじです', 'D. いまにじです'],
    ['A. きょうはなんじですか？', 'B. あしたはなんにちですか？', 'C. きょうはなんにちですか？', 'D. ことしはなんにちですか？'],
    ['A. Kapan', 'B. Di mana', 'C. Siapa', 'D. Apa']
]

while main_lagi():
    permainan_baru()

print('\n\t=======BYEEE, SAMPAI KETEMU LAGI=======')
