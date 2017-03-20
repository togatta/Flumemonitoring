## Flume Monitoring Flume
script python ini sih cuma script berantakan yang gw buat untuk monitoring proses flume, supaya kalo ada proses mati dia ngasih tau lewat email dan ngerestart servicenya sih biar ga error gitu

### Line Yang Perlu diubah

di line 23 sender = '(isi alamat sendernya)' menjadi misal sender = '(test@test.com)'
di line 24 recipients = ['isi alamat si penerimanya'] menjadi misal recipients = ['test1@test.co','test2@test.com']

### Penggunaannya

Jika linenya udah diubah, cara pemakaiannya adalah sebagai berikut :


flumemonitoring.py [spasi] [lokasi path log] [spasi]  [nama agent]


contoh :

flumemonitoring.py /var/log/flume/flume.log test
