[Monophone HMMs dengan HTK - HCompV]

1. Copy folder mfcc (Hasil feature-extraction)
2. Buat folder hmm0
2. Definisikan list nama file .mfc sesuai isi folder mfcc (train.scp)
3. Jalankan HCompV -C config -f 0.01 -m -S train.scp -M hmm0 proto 