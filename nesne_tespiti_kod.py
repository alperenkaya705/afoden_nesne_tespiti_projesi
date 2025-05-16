# 📌 Google Drive'a bağlan
from google.colab import drive
drive.mount('/content/drive')

# GPU bilgilerini kontrol edelim
!nvidia-smi

# Gerekli kütüphaneleri yükleyelim
!pip install -q kaggle matplotlib opencv-python PyYAML tqdm seaborn

# GPU hızlandırma için gerekli optimizasyonları yükleyelim
!pip install -q torch torchvision

# YOLOv9 reposunu klonlayalım
!git clone https://github.com/WongKinYiu/yolov9.git
%cd yolov9
!pip install -q -r requirements.txt

import os
from google.colab import files
import glob
import shutil
import random

# Kaggle API anahtarı var mı kontrol edelim, yoksa kullanıcıdan isteyelim
kaggle_dir = '/root/.kaggle'
if not os.path.exists(f'{kaggle_dir}/kaggle.json'):
    print("Lütfen Kaggle API anahtarınızı yükleyin.")
    print("Kaggle hesabınızdan anahtarı şuradan indirebilirsiniz: https://www.kaggle.com/account")
    print("'kaggle.json' dosyasını yüklemek için aşağıdaki hücreyi çalıştırın.")
    uploaded = files.upload()

    # Dosyayı doğru konuma taşıyalım ve izinleri ayarlayalım
    !mkdir -p {kaggle_dir}
    !cp kaggle.json {kaggle_dir}/
    !chmod 600 {kaggle_dir}/kaggle.json
else:
    print("Kaggle API yapılandırması mevcut.")

# Çalışma dizinini tanımlayalım (Colab'da /content altında çalışıyoruz)
WORK_DIR = '/content'
YOLOV9_DIR = f'{WORK_DIR}/yolov9'
DATASET_DIR = f'{WORK_DIR}/dataset'
AFO_DATASET_DIR = f'{WORK_DIR}/afo-dataset'

# AFO veri setini indirelim
!kaggle datasets download -d jangsienicajzkowy/afo-aerial-dataset-of-floating-objects
!unzip -q afo-aerial-dataset-of-floating-objects.zip -d {AFO_DATASET_DIR}

#SİLMEEEEE
!rm -r /content/afo-dataset/PART_1/PART_1/1category

#SİLMEEEEE
!rm -r /content/afo-dataset/PART_1/PART_1/2categories

#SİLMEEEEE
!rm -r /content/afo-dataset/PART_1/PART_1/2categories.names

#SİLMEEEEE
!rm -r /content/afo-dataset/PART_1/PART_1/readme.txt

#SİLMEEEEE
!rm -r /content/afo-dataset/PART_2/PART_2/readme.txt

#SİLMEEEEE
!rm -r /content/afo-dataset/PART_3/PART_3/readme.txt

# Veri seti yapısını kontrol edelim
!ls -la {AFO_DATASET_DIR}/

# YOLOv9 için veri seti yapısını oluşturalım
!mkdir -p {DATASET_DIR}/images/train {DATASET_DIR}/images/val {DATASET_DIR}/images/test
!mkdir -p {DATASET_DIR}/labels/train {DATASET_DIR}/labels/val {DATASET_DIR}/labels/test

# TXT dosyasının yolu (içinde kopyalanacak JPG isimleri var)
txt_dosya_yolu = "/content/afo-dataset/PART_1/PART_1/test.txt"

# JPG'lerin aranacağı kaynak klasörler (3 farklı klasör)
kaynak_klasorler = [
    "/content/afo-dataset/PART_1/PART_1/images",
    "/content/afo-dataset/PART_2/PART_2/images",
    "/content/afo-dataset/PART_3/PART_3/images"
]

# Kopyalanacak hedef klasör
hedef_klasor = "/content/dataset/images/test"

# Hedef klasörü oluştur (yoksa)
os.makedirs(hedef_klasor, exist_ok=True)

# TXT dosyasını oku ve her JPG için 3 klasörde ara
with open(txt_dosya_yolu, 'r') as file:
    for line in file:
        jpg_dosya = line.strip()  # Satır sonundaki boşlukları temizle

        if not jpg_dosya:  # Boş satırları atla
            continue

        dosya_bulundu = False

        # Tüm kaynak klasörlerde sırayla ara
        for kaynak_klasor in kaynak_klasorler:
            kaynak_yol = os.path.join(kaynak_klasor, jpg_dosya)

            if os.path.exists(kaynak_yol):
                hedef_yol = os.path.join(hedef_klasor, jpg_dosya)
                shutil.copy2(kaynak_yol, hedef_yol)
                print(f"✅ {jpg_dosya} bulundu ve kopyalandı: {kaynak_klasor}")
                dosya_bulundu = True
                break  # Dosya bulundu, diğer klasörlere bakmaya gerek yok

        if not dosya_bulundu:
            print(f"❌ {jpg_dosya} hiçbir klasörde bulunamadı!")

print("\nİşlem tamamlandı. Bulunamayan dosyalar '❌' ile işaretlendi.")



# TXT dosyasının yolu (içinde kopyalanacak JPG isimleri var)
txt_dosya_yolu = "/content/afo-dataset/PART_1/PART_1/train.txt"

# JPG'lerin aranacağı kaynak klasörler (3 farklı klasör)
kaynak_klasorler = [
    "/content/afo-dataset/PART_1/PART_1/images",
    "/content/afo-dataset/PART_2/PART_2/images",
    "/content/afo-dataset/PART_3/PART_3/images"
]

# Kopyalanacak hedef klasör
hedef_klasor = "/content/dataset/images/train"

# Hedef klasörü oluştur (yoksa)
os.makedirs(hedef_klasor, exist_ok=True)

# TXT dosyasını oku ve her JPG için 3 klasörde ara
with open(txt_dosya_yolu, 'r') as file:
    for line in file:
        jpg_dosya = line.strip()  # Satır sonundaki boşlukları temizle

        if not jpg_dosya:  # Boş satırları atla
            continue

        dosya_bulundu = False

        # Tüm kaynak klasörlerde sırayla ara
        for kaynak_klasor in kaynak_klasorler:
            kaynak_yol = os.path.join(kaynak_klasor, jpg_dosya)

            if os.path.exists(kaynak_yol):
                hedef_yol = os.path.join(hedef_klasor, jpg_dosya)
                shutil.copy2(kaynak_yol, hedef_yol)
                print(f"✅ {jpg_dosya} bulundu ve kopyalandı: {kaynak_klasor}")
                dosya_bulundu = True
                break  # Dosya bulundu, diğer klasörlere bakmaya gerek yok

        if not dosya_bulundu:
            print(f"❌ {jpg_dosya} hiçbir klasörde bulunamadı!")

print("\nİşlem tamamlandı. Bulunamayan dosyalar '❌' ile işaretlendi.")



# TXT dosyasının yolu (içinde kopyalanacak JPG isimleri var)
txt_dosya_yolu = "/content/afo-dataset/PART_1/PART_1/validation.txt"

# JPG'lerin aranacağı kaynak klasörler (3 farklı klasör)
kaynak_klasorler = [
    "/content/afo-dataset/PART_1/PART_1/images",
    "/content/afo-dataset/PART_2/PART_2/images",
    "/content/afo-dataset/PART_3/PART_3/images"
]

# Kopyalanacak hedef klasör
hedef_klasor = "/content/dataset/images/val"

# Hedef klasörü oluştur (yoksa)
os.makedirs(hedef_klasor, exist_ok=True)

# TXT dosyasını oku ve her JPG için 3 klasörde ara
with open(txt_dosya_yolu, 'r') as file:
    for line in file:
        jpg_dosya = line.strip()  # Satır sonundaki boşlukları temizle

        if not jpg_dosya:  # Boş satırları atla
            continue

        dosya_bulundu = False

        # Tüm kaynak klasörlerde sırayla ara
        for kaynak_klasor in kaynak_klasorler:
            kaynak_yol = os.path.join(kaynak_klasor, jpg_dosya)

            if os.path.exists(kaynak_yol):
                hedef_yol = os.path.join(hedef_klasor, jpg_dosya)
                shutil.copy2(kaynak_yol, hedef_yol)
                print(f"✅ {jpg_dosya} bulundu ve kopyalandı: {kaynak_klasor}")
                dosya_bulundu = True
                break  # Dosya bulundu, diğer klasörlere bakmaya gerek yok

        if not dosya_bulundu:
            print(f"❌ {jpg_dosya} hiçbir klasörde bulunamadı!")

print("\nİşlem tamamlandı. Bulunamayan dosyalar '❌' ile işaretlendi.")





import os
import shutil

# TXT dosyasının yolu (içinde .jpg uzantılı dosya isimleri var)
txt_dosya_yolu = "/content/afo-dataset/PART_1/PART_1/train.txt"

# TXT'lerin aranacağı kaynak klasörler
kaynak_klasorler = [
    "/content/afo-dataset/PART_1/PART_1/6categories"
]

# Kopyalanacak hedef klasör
hedef_klasor = "/content/dataset/labels/train"

# Hedef klasörü oluştur (yoksa)
os.makedirs(hedef_klasor, exist_ok=True)

# TXT dosyasını oku ve her satırdaki .jpg ismini .txt'ye çevirerek ara
with open(txt_dosya_yolu, 'r') as file:
    for line in file:
        # Satırdaki .jpg uzantısını .txt ile değiştir
        jpg_isim = line.strip()
        txt_isim = jpg_isim.replace('.jpg', '.txt')

        if not txt_isim:  # Boş satırları atla
            continue

        dosya_bulundu = False

        # Tüm kaynak klasörlerde sırayla ara
        for kaynak_klasor in kaynak_klasorler:
            kaynak_yol = os.path.join(kaynak_klasor, txt_isim)

            if os.path.exists(kaynak_yol):
                hedef_yol = os.path.join(hedef_klasor, txt_isim)
                shutil.copy2(kaynak_yol, hedef_yol)
                print(f"✅ {txt_isim} bulundu ve kopyalandı: {kaynak_klasor}")
                dosya_bulundu = True
                break  # Dosya bulundu, diğer klasörlere bakmaya gerek yok

        if not dosya_bulundu:
            print(f"❌ {txt_isim} hiçbir klasörde bulunamadı!")

print("\nİşlem tamamlandı. Bulunamayan dosyalar '❌' ile işaretlendi.")



import os
import shutil

# TXT dosyasının yolu (içinde .jpg uzantılı dosya isimleri var)
txt_dosya_yolu = "/content/afo-dataset/PART_1/PART_1/test.txt"

# TXT'lerin aranacağı kaynak klasörler
kaynak_klasorler = [
    "/content/afo-dataset/PART_1/PART_1/6categories"
]

# Kopyalanacak hedef klasör
hedef_klasor = "/content/dataset/labels/test"

# Hedef klasörü oluştur (yoksa)
os.makedirs(hedef_klasor, exist_ok=True)

# TXT dosyasını oku ve her satırdaki .jpg ismini .txt'ye çevirerek ara
with open(txt_dosya_yolu, 'r') as file:
    for line in file:
        # Satırdaki .jpg uzantısını .txt ile değiştir
        jpg_isim = line.strip()
        txt_isim = jpg_isim.replace('.jpg', '.txt')

        if not txt_isim:  # Boş satırları atla
            continue

        dosya_bulundu = False

        # Tüm kaynak klasörlerde sırayla ara
        for kaynak_klasor in kaynak_klasorler:
            kaynak_yol = os.path.join(kaynak_klasor, txt_isim)

            if os.path.exists(kaynak_yol):
                hedef_yol = os.path.join(hedef_klasor, txt_isim)
                shutil.copy2(kaynak_yol, hedef_yol)
                print(f"✅ {txt_isim} bulundu ve kopyalandı: {kaynak_klasor}")
                dosya_bulundu = True
                break  # Dosya bulundu, diğer klasörlere bakmaya gerek yok

        if not dosya_bulundu:
            print(f"❌ {txt_isim} hiçbir klasörde bulunamadı!")

print("\nİşlem tamamlandı. Bulunamayan dosyalar '❌' ile işaretlendi.")



import os
import shutil

# TXT dosyasının yolu (içinde .jpg uzantılı dosya isimleri var)
txt_dosya_yolu = "/content/afo-dataset/PART_1/PART_1/validation.txt"

# TXT'lerin aranacağı kaynak klasörler
kaynak_klasorler = [
    "/content/afo-dataset/PART_1/PART_1/6categories"
]

# Kopyalanacak hedef klasör
hedef_klasor = "/content/dataset/labels/val"

# Hedef klasörü oluştur (yoksa)
os.makedirs(hedef_klasor, exist_ok=True)

# TXT dosyasını oku ve her satırdaki .jpg ismini .txt'ye çevirerek ara
with open(txt_dosya_yolu, 'r') as file:
    for line in file:
        # Satırdaki .jpg uzantısını .txt ile değiştir
        jpg_isim = line.strip()
        txt_isim = jpg_isim.replace('.jpg', '.txt')

        if not txt_isim:  # Boş satırları atla
            continue

        dosya_bulundu = False

        # Tüm kaynak klasörlerde sırayla ara
        for kaynak_klasor in kaynak_klasorler:
            kaynak_yol = os.path.join(kaynak_klasor, txt_isim)

            if os.path.exists(kaynak_yol):
                hedef_yol = os.path.join(hedef_klasor, txt_isim)
                shutil.copy2(kaynak_yol, hedef_yol)
                print(f"✅ {txt_isim} bulundu ve kopyalandı: {kaynak_klasor}")
                dosya_bulundu = True
                break  # Dosya bulundu, diğer klasörlere bakmaya gerek yok

        if not dosya_bulundu:
            print(f"❌ {txt_isim} hiçbir klasörde bulunamadı!")

print("\nİşlem tamamlandı. Bulunamayan dosyalar '❌' ile işaretlendi.")







# Dosya sayılarını kontrol edelim
print("Kopyalanan dosya sayıları:")
print(f"Eğitim görüntüleri: {len(os.listdir(f'{DATASET_DIR}/images/train'))}")
print(f"Eğitim etiketleri: {len(os.listdir(f'{DATASET_DIR}/labels/train'))}")
print(f"Doğrulama görüntüleri: {len(os.listdir(f'{DATASET_DIR}/images/val'))}")
print(f"Doğrulama etiketleri: {len(os.listdir(f'{DATASET_DIR}/labels/val'))}")
print(f"Test görüntüleri: {len(os.listdir(f'{DATASET_DIR}/images/test'))}")
print(f"Test etiketleri: {len(os.listdir(f'{DATASET_DIR}/labels/test'))}")

# Eğer dosya sayıları eşleşmiyorsa uyarı ver
if len(os.listdir(f'{DATASET_DIR}/images/train')) != len(os.listdir(f'{DATASET_DIR}/labels/train')):
    print("UYARI: Eğitim görüntüleri ve etiketleri sayısı eşleşmiyor!")

if len(os.listdir(f'{DATASET_DIR}/images/val')) != len(os.listdir(f'{DATASET_DIR}/labels/val')):
    print("UYARI: Doğrulama görüntüleri ve etiketleri sayısı eşleşmiyor!")

if len(os.listdir(f'{DATASET_DIR}/images/test')) != len(os.listdir(f'{DATASET_DIR}/labels/test')):
    print("UYARI: Test görüntüleri ve etiketleri sayısı eşleşmiyor!")

# Sınıf bilgilerini almak için bir etiketi inceleyelim
try:
    # Etiket dosyalarını kontrol edelim
    label_files = os.listdir(f'{DATASET_DIR}/labels/train')
    if label_files:
        sample_label = os.path.join(f'{DATASET_DIR}/labels/train', random.choice(label_files))
        print(f"Örnek etiket dosyası ({sample_label}) içeriği:")
        !cat {sample_label}

        # Kaç sınıf var görelim
        all_classes = set()
        for label_file in glob.glob(f'{DATASET_DIR}/labels/train/*.txt'):
            with open(label_file, 'r') as f:
                for line in f:
                    parts = line.strip().split()
                    if parts:  # Boş satırları atla
                        try:
                            class_id = int(parts[0])
                            all_classes.add(class_id)
                        except (ValueError, IndexError):
                            print(f"UYARI: Geçersiz format - {label_file}: {line}")

        print(f"\nVeri setinde tespit edilen sınıf ID'leri: {sorted(all_classes)}")
        num_classes = len(all_classes)
        print(f"Toplam sınıf sayısı: {num_classes}")
    else:
        print("Etiket dosyası bulunamadı.")
        num_classes = 1  # Varsayılan
except Exception as e:
    print(f"Etiketleri incelemede hata: {e}")
    num_classes = 1  # Varsayılan



# Sınıf isimlerini belirle
class_names = []
for i in range(num_classes):
    class_names.append(f'class_{i}')  # Varsayılan sınıf isimleri

data_yaml = f"""
train: {DATASET_DIR}/images/train
val: {DATASET_DIR}/images/val
test: {DATASET_DIR}/images/test

# Sınıf sayısı ve isimleri
nc: {num_classes}  # Sınıf sayısı
names: {class_names}  # Sınıf isimleri
"""

with open(f'{YOLOV9_DIR}/data/afo.yaml', 'w') as f:
    f.write(data_yaml)

print("Oluşturulan data.yaml içeriği:")
!cat {YOLOV9_DIR}/data/afo.yaml





!mkdir -p {YOLOV9_DIR}/weights
!wget -P {YOLOV9_DIR}/weights https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt




import torch
print(torch.cuda.is_available())  # False ise GPU yok demektir

import time

# Eğitim başlangıç zamanı
start_time = time.time()

# Eğitimi başlatalım
!cd {YOLOV9_DIR} && python train_dual.py --workers 2 --device 0 --batch 8 --data data/afo.yaml --img 640 --cfg models/detect/yolov9-c.yaml --weights weights/yolov9-c.pt --name yolov9-afo --hyp data/hyps/hyp.scratch-high.yaml --patience 50 --epochs 300

# Eğitim bitiş zamanı
end_time = time.time()

# Süreyi hesapla
total_time = end_time - start_time
hours = total_time // 3600
minutes = (total_time // 60)%60
seconds = total_time % 60

print(f"\n✅ Eğitim tamamlandı. Toplam süre: {int(hours)} saat {int(minutes)} dakika {int(seconds)} saniye.")

# Tüm runs klasörünü Drive'a kopyala (örnek adıyla)
!cp -r /content/yolov9/runs /content/drive/MyDrive/parametreli_runs_2



import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Sonuç dosyasını oku
results_csv = '/content/drive/MyDrive/parametreli_runs_2/train/yolov9-afo/results.csv'
if os.path.exists(results_csv):
    results = pd.read_csv(results_csv)

    # Sütun isimlerini temizle (başındaki ve sonundaki boşlukları kaldır)
    results.columns = results.columns.str.strip()

    # Grafikleri hazırlayalım
    plt.figure(figsize=(20, 15))

    # Kayıp grafiği
    plt.subplot(2, 2, 1)
    plt.plot(results['epoch'], results['train/box_loss'], label='train/box_loss')
    plt.plot(results['epoch'], results['train/cls_loss'], label='train/cls_loss')
    plt.plot(results['epoch'], results['train/dfl_loss'], label='train/dfl_loss')
    plt.title('Training Losses')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    # mAP grafiği
    plt.subplot(2, 2, 2)
    plt.plot(results['epoch'], results['metrics/mAP_0.5'], label='mAP50')
    plt.plot(results['epoch'], results['metrics/mAP_0.5:0.95'], label='mAP50-95')
    plt.title('mAP Metrics')
    plt.xlabel('Epoch')
    plt.ylabel('mAP')
    plt.legend()

    # Precision ve Recall
    plt.subplot(2, 2, 3)
    plt.plot(results['epoch'], results['metrics/precision'], label='Precision')
    plt.plot(results['epoch'], results['metrics/recall'], label='Recall')
    plt.title('Precision and Recall Metrics')
    plt.xlabel('Epoch')
    plt.ylabel('Value')
    plt.legend()

    # Validation kayıpları
    plt.subplot(2, 2, 4)
    plt.plot(results['epoch'], results['val/box_loss'], label='val/box_loss')
    plt.plot(results['epoch'], results['val/cls_loss'], label='val/cls_loss')
    plt.plot(results['epoch'], results['val/dfl_loss'], label='val/dfl_loss')
    plt.title('Validation Losses')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()

    plt.tight_layout()
    plt.show()

    # Son 5 epoch için performans metriklerini gösteren tablo
    print("\nSon 5 epoch için performans metrikleri:")
    last_5_epochs = results.tail(5)[['epoch', 'metrics/precision', 'metrics/recall', 'metrics/mAP_0.5', 'metrics/mAP_0.5:0.95']]
    last_5_epochs.columns = ['Epoch', 'Precision', 'Recall', 'mAP50', 'mAP50-95']
    print(last_5_epochs)

    # En iyi sonuçları göster
    best_map = results['metrics/mAP_0.5:0.95'].max()
    best_epoch = results.loc[results['metrics/mAP_0.5:0.95'].idxmax(), 'epoch']
    print(f"\nEn iyi mAP50-95: {best_map:.4f} (Epoch {best_epoch:.0f})")
else:
    print("Sonuç dosyası bulunamadı. Eğitim henüz tamamlanmamış olabilir.")



# Test seti üzerinde değerlendirme yapalım
!cd {YOLOV9_DIR} && python val.py --data data/afo.yaml --weights /content/drive/MyDrive/parametreli_runs_2/train/yolov9-afo/weights/best.pt --batch 8 --img 640 --conf 0.001 --iou 0.65 --device 0 --save-json --save-conf



!cd {YOLOV9_DIR} && python detect.py \
    --weights /content/drive/MyDrive/parametreli_runs_2/train/yolov9-afo/weights/best.pt \
    --conf 0.25 \
    --img-size 640 \
    --source {DATASET_DIR}/images/test \
    --save-txt \
    --save-conf \
    --data {DATASET_DIR}/afo.yaml



import pandas as pd

# Sonuç dosyasını oku
results = pd.read_csv(results_csv)

# Sütun isimlerini temizle (ön ve arka boşlukları kaldır)
results.columns = results.columns.str.strip()

# Model performans özeti
print("\nModel Performans Özeti:")
if os.path.exists(results_csv):
    print(f"Toplam epoch sayısı: {len(results)}")
    last_epoch = results.iloc[-1]

    # Burada doğru sütun isimlerini kullanıyoruz
    print(f"Son epoch mAP50: {last_epoch['metrics/mAP_0.5']:.4f}")
    print(f"Son epoch mAP50-95: {last_epoch['metrics/mAP_0.5:0.95']:.4f}")
    print(f"Son epoch Precision: {last_epoch['metrics/precision']:.4f}")
    print(f"Son epoch Recall: {last_epoch['metrics/recall']:.4f}")

    # En iyi epoch bilgileri
    best_idx = results['metrics/mAP_0.5:0.95'].idxmax()
    best_epoch = results.iloc[best_idx]

    print(f"\nEn iyi performans (Epoch {best_idx}):")
    print(f"En iyi mAP50: {best_epoch['metrics/mAP_0.5']:.4f}")
    print(f"En iyi mAP50-95: {best_epoch['metrics/mAP_0.5:0.95']:.4f}")
    print(f"En iyi Precision: {best_epoch['metrics/precision']:.4f}")
    print(f"En iyi Recall: {best_epoch['metrics/recall']:.4f}")
else:
    print("Sonuç dosyası bulunamadı.")




# Tüm runs klasörünü Drive'a kopyala (örnek adıyla)
!cp -r /content/yolov9/runs /content/drive/MyDrive/runs-2nci-kez











