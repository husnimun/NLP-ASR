[Monophone HMMs dengan HTK - HCompV]

1. Buat folder hmm0
2. Definisikan list nama file .mfc sesuai isi folder mfcc (train.scp)
3. Jalankan HCompV -C config -f 0.01 -m -S train.scp -M hmm0 proto 
4. Jalankan HMMDefsGeneration.py berdasarkan hmmo/proto (copy proto ke proto_template.txt) -> hmmdefs
5. Masukkan file hasil step-2 phones0.mlf
6. Buat file macros dari vFloors di tambah ~o <MFCC_0_D_A> <VecSize> 39 di awal baris (hmmo)
7. HERest -C config -I phones0.mlf -t 250.0 150.0 1000.0 -S train.scp -H hmm0/macros -H hmm0/hmmdefs -M hmm1 monophones0
8. Ulangi sampai hmm3 
9. Copy hmm3 rename hmm4 (ada langkah khusus pada hmm4)
10. HHEd -H hmm4/macros -H hmm4/hmmdefs -M hmm5 sil.hed monophones1
11. Lanjutkan hingga hmm7 dengan phones1 dan monophones1
		HERest -C config -I phones1.mlf -t 250.0 150.0 1000.0 -S train.scp -H hmm5/macros -H hmm5/hmmdefs -M hmm6 monophones1