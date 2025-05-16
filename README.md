# AFO Veri Seti ile YOLOv9 Kullanılarak Deniz Ortamında Küçük Nesne Tespiti
Bu proje, Gölhisar Uygulamalı Bilimler Yüksekokulu'nda AFODEN grubu tarafından, YOLOv9 modeli kullanılarak deniz ortamında nesne tespiti amacıyla gerçekleştirilmiştir.

## Grup: AFODEN
**Grup Üyeleri**  
- İsmail Can Dağ  
- Doğukan Olağ  
- Alperen Kaya
- Murat Turan    
- Zafer Göktaş  

---

## Projenin Amacı

Bu proje, deniz yüzeyinde yürütülen arama kurtarma çalışmalarına destek olmak amacıyla geliştirilmiştir. İHA’larla elde edilen hava görüntüleri üzerinde, küçük nesnelerin hızlı ve yüksek doğrulukla tespiti için **YOLOv9** modeli uygulanmıştır. Sistem, insan, bot, sal gibi hayati öneme sahip nesneleri otomatik olarak tanımayı hedeflemektedir.

---

## Kullanılan Veri Seti

- **Adı**: AFO (Aerial Floating Object)
- Veri seti 6 ülkede 35 farklı lokasyonda insansız hava araçları ile çekilmiş 50 farklı videodan alınan görseller ve görsellerde bulunan nesneler ile hazırlanmıştır.
- **Toplam Görsel**: 3.647
- **Etiketli Nesne Sayısı**: 39.991  
- **Nesne Sınıfları**:  
  - İnsan  
  - Bot  
  - Tahta  
  - Şamandıra  
  - Yelkenli  
  - Kayak   

---
## Kullanılan Model

- **Model**: YOLOv9-c.pt
- **Görsel Girdi Boyutu**: 640x640   
- **Epoch Sayısı**: 300 epoch  
- **Platform**: Google Colab üzerinde eğitilmiştir.

---

## Model Performansı Sonuçları

| Metrik            | Değer   |
|-------------------|---------|
| **mAP@0.5**       | 0.9546  |
| **mAP@0.5:0.95**  | 0.7097  |
| **Precision**     | 0.9339  |
| **Recall**        | 0.9214  |

### Nesne Sınıfları Bazında Sonuçlar

| Nesne      | mAP   | Precision | Recall |
|------------|-------|-----------|--------|
| İnsan      | 0.950 | 0.952     | 0.915  |
| Tahta      | 0.994 | 0.984     | 0.994  |
| Bot        | 0.969 | 0.844     | 0.962  |
| Şamandıra  | 0.866 | 0.933     | 0.670  |
| Yelkenli   | 0.995 | 0.948     | 1.000  |
| Kayak      | 0.987 | 0.937     | 0.973  |

---

