1. Download julius source-code
2. ./configure --enable-words-int
3. sudo make
4. sudo make install
5. Edit file lexicon (ubah yang menyebabkan error menjadi sil)
6. Tambahkan <s> [<s>] sil dan </s> [</s>] sil
7. Ubah lm.arpa menjadi binary : mkbingram -nlf lm.arpa lm_bin
8. Jalankan padsp julius -input mic -C julius.conf