1. copy hmmdefs dan macros dari hmm7, train.scp dari step 5&6
2. copy dic_silence dan words-final dari step 3
3. copy monophones1 dari step 2

4. Jalankan HVite -A -D -T 1 -l '*' -o SWT -b SENT-END -C config -H macros -H hmmdefs -i aligned.mlf -m -t 250.0 150.0 1000.0 -y lab -a -I words-final.mlf -S train.scp dict_silence monophones1
5. Buat folder hmm8 dan hmm9
6. Jalankan HERest -A -D -T 1 -C config -I aligned.mlf -t 250.0 150.0 3000.0 -S train.scp -H macros -H hmmdefs -M hmm8 monophones1 
7. Jalankan HERest -A -D -T 1 -C config -I aligned.mlf -t 250.0 150.0 3000.0 -S train.scp -H hmm8/macros -H hmm8/hmmdefs -M hmm9 monophones1 

5. Pilih file untuk test, buat test.scp
6. Jalankan HVite -H macros -H hmmdefs -S test.scp -| '*' -i recout.mlf -w wdnet -p 0.0 -s 5.0 dict_silence monophones1
7. Jalankan HResults -I words.mlf monophones1 recout.mlf