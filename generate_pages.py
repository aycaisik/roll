import os
import json

base_html = """<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title} | Roll Event Lab</title>
    <link rel="stylesheet" href="css.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
</head>
<body>
    <nav class="navbar">
        <div class="container">
            <a href="index.html" class="logo">ROLL<span>EVENT LAB</span></a>
            <ul class="nav-links">
                <li><a href="index.html#anasayfa">Ana Sayfa</a></li>
                <li><a href="index.html#hizmetler">Hizmetlerimiz</a></li>
                <li><a href="index.html#portfolyo">Portfolyo</a></li>
                <li><a href="biz-kimiz.html">Biz Kimiz</a></li>
                <li><a href="index.html#iletisim">İletişim</a></li>
            </ul>
            <div class="hamburger">
                <span></span>
                <span></span>
                <span></span>
            </div>
        </div>
    </nav>

    <main class="service-detail-page">
        <section class="service-detail-hero" style="background-image: url('{hero_img}');">
            <div class="hero-content">
                <h1>{title}</h1>
                <p>{hero_desc}</p>
            </div>
        </section>

        <section class="service-sub-sections">
            <div class="container">
                {sub_sections}
            </div>
        </section>
    </main>

    <footer class="footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <a href="index.html" class="logo">ROLL<span>EVENT LAB</span></a>
                    <p>Etkinliklerinize profesyonel dokunuş.</p>
                </div>
                <div class="footer-social">
                    <p class="footer-social-title">Sosyal medya hesaplarımız</p>
                    <div class="footer-social-links">
                        <a class="social-link" href="https://www.instagram.com/rolleventlab/" target="_blank" rel="noopener noreferrer" aria-label="Instagram">
                            <svg viewBox="0 0 24 24"><path d="M7 2h10a5 5 0 0 1 5 5v10a5 5 0 0 1-5 5H7a5 5 0 0 1-5-5V7a5 5 0 0 1 5-5zm10 2H7a3 3 0 0 0-3 3v10a3 3 0 0 0 3 3h10a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3zm-5 4a5 5 0 1 1 0 10 5 5 0 0 1 0-10zm0 2a3 3 0 1 0 0 6 3 3 0 0 0 0-6zm5.5-.9a1.1 1.1 0 1 1 0 2.2 1.1 1.1 0 0 1 0-2.2z" fill="#fff"/></svg>
                        </a>
                        <a class="social-link" href="https://www.youtube.com/@mabollaplus" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
                            <svg viewBox="0 0 24 24"><path d="M21.6 7.2a3 3 0 0 0-2.1-2.1C17.6 4.6 12 4.6 12 4.6s-5.6 0-7.5.5A3 3 0 0 0 2.4 7.2 31.7 31.7 0 0 0 2 12a31.7 31.7 0 0 0 .4 4.8 3 3 0 0 0 2.1 2.1c1.9.5 7.5.5 7.5.5s5.6 0 7.5-.5a3 3 0 0 0 2.1-2.1A31.7 31.7 0 0 0 22 12a31.7 31.7 0 0 0-.4-4.8zM10 15.5v-7l6 3.5-6 3.5z" fill="#fff"/></svg>
                        </a>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 Roll Event Lab. Tüm hakları saklıdır.</p>
            </div>
        </div>
    </footer>
    <script src="js.js"></script>
</body>
</html>"""

def make_sub_sections(items):
    out = []
    for item in items:
        html = f"""
                <div class="sub-service-row">
                    <div class="sub-service-image">
                        <img src="{item['img']}" alt="{item['title']}" loading="lazy">
                    </div>
                    <div class="sub-service-text">
                        <h2>{item['title']}</h2>
                        <p>{item['desc']}</p>
                    </div>
                </div>"""
        out.append(html)
    return "".join(out)

pages = [
    {
        "filename": "kurumsal-etkinlikler.html",
        "title": "Kurumsal Etkinlikler",
        "hero_desc": "Markaların ve kurumların ihtiyaçlarına özel, kurumsal kimliğinizi yansıtan profesyonel organizasyonlar tasarlıyoruz.",
        "hero_img": "images/kurumsal-hero.jpg",
        "items": [
            {"title": "Şirket Etkinlikleri", "desc": "Şirketinizin vizyonunu ön plana çıkaran, çalışan motivasyonunu artıran yaratıcı ve yenilikçi kurum içi etkinlikler düzenliyoruz.", "img": "images/sirket-etkinlikleri.jpg"},
            {"title": "Lansman", "desc": "Yeni ürün veya hizmetlerinizi hedef kitlenizle en etkili yoldan buluşturmanız için akılda kalıcı lansman projeleri tasarlıyoruz.", "img": "images/lansman.jpg"},
            {"title": "Gala", "desc": "Zarif ve kusursuz detaylarla planlanmış, kurumsal prestijinize yakışır büyüleyici gala geceleri organize ediyoruz.", "img": "images/gala.jpg"},
            {"title": "Ödül Töreni", "desc": "Başarıların görkemli bir atmosferde kutlandığı, profesyonel sahne şovlarıyla desteklenmiş anlamlı ödül törenleri hazırlıyoruz.", "img": "images/odul-toreni.jpg"},
            {"title": "Bayii Toplantısı", "desc": "İş ortaklarınızla verimli vakit geçirirken, eğlencenin ve kurumsal hedeflerin dengelendiği toplantı ve organizasyonlar sunuyoruz.", "img": "images/bayii-toplantisi.jpg"}
        ]
    },
    {
        "filename": "ozel-gunler.html",
        "title": "Özel Günler",
        "hero_desc": "Hayatınızın en özel anlarını, her detayı sizin için düşünülmüş estetik ve akılda kalıcı etkinliklerle tasarlıyoruz.",
        "hero_img": "images/ozel-gunler-hero.jpg",
        "items": [
            {"title": "Nişan", "desc": "Evliliğe giden bu ilk ve en samimi adımınızda, hayallerinizdeki konsepti en ince detayına kadar uyguluyoruz.", "img": "images/nisan.jpg"},
            {"title": "Düğün", "desc": "Sizin hikayenizi anlatan konseptlerle, misafirlerinize ve size ömür boyu unutulmaz fotoğraflar bırakacak görkemli düğün organizasyonları yapıyoruz.", "img": "images/dugun.jpg"},
            {"title": "Bekarlığa Veda", "desc": "Düğün öncesi stresinizi atıp doyasıya eğleneceğiniz size ve arkadaşlarınıza özel konsept partiler.", "img": "images/bekarliga-veda.jpg"},
            {"title": "After Party", "desc": "Gece hiç bitmesin diyenlere, müzik ve dans dolu, enerjinin tavan yaptığı unutulmaz After Party organizasyonları.", "img": "images/after-party.jpg"},
            {"title": "Özel Davet", "desc": "Sevdiklerinizi şık ve zarif bir ortamda misafir edebileceğiniz butik veya geniş çaplı kurumsal veya bireysel özel davetler.", "img": "images/ozel-davet.jpg"},
            {"title": "Doğum Günü", "desc": "Yaş almanın en eğlenceli ve coşkulu anlarını yansıtan sıradışı konseptteki sürpriz doğum günü partileri.", "img": "images/dogum-gunu.jpg"}
        ]
    },
    {
        "filename": "konser-festival.html",
        "title": "Konser & Festival Etkinlikleri",
        "hero_desc": "Geniş katılımlı etkinliklerde sahne, teknik ekip ve etkinlik akışını güçlü organizasyon altyapımızla profesyonelce yönetiyoruz.",
        "hero_img": "images/konser-hero.jpg",
        "items": [
            {"title": "Konser", "desc": "Sahne kurulumundan sanatçı yönetimine, ses ve ışık prodüksiyonundan seyirci güvenliğine kadar konser organizasyonunu A'dan Z'ye planlıyoruz.", "img": "images/konser.jpg"},
            {"title": "Festival", "desc": "Binlerce kişinin katıldığı dev açık hava organizasyonlarını başarıyla koordine ederek katılımcılara benzersiz bir deneyim yaşatıyoruz.", "img": "images/festival.jpg"},
            {"title": "Kültür & Sanat Etkinlikleri", "desc": "Toplumsal ve sanatsal değerlere katkı sunan vizyoner kültür projelerinde mekan ve vizyon yönetimi.", "img": "images/kultur-sanat.jpg"}
        ]
    },
    {
        "filename": "mekan-danismanligi.html",
        "title": "Mekan Organizasyon Danışmanlığı",
        "hero_desc": "Etkinlik mekanlarının konsept, operasyon ve organizasyon süreçlerini profesyonel bakış açısıyla planlıyor, mekanın potansiyelini en iyi şekilde değerlendiren çözümler sunuyoruz.",
        "hero_img": "images/danismanlik-hero.jpg",
        "items": [
            {"title": "Mekan Analizi & Vizyon", "desc": "Etkinlik mekanınızın potansiyelini doğru okuyor, hangi kitleye ve konseptlere hitap edeceğini belirleyerek gelir modelleri kurguluyoruz.", "img": "images/mekan-analizi.jpg"},
            {"title": "Operasyonel Planlama", "desc": "Giriş çıkış senaryoları, güvenlik ağı, kulis ve bekleme alanları gibi mekanın pratik olarak işleyişini eksiksiz şekilde haritalandırıyoruz.", "img": "images/operasyonel-planlama.jpg"}
        ]
    },
    {
        "filename": "konsept-tasarim.html",
        "title": "Konsept Tasarım",
        "hero_desc": "Etkinliğinizin ruhuna uygun özgün konseptler geliştiriyor; dekorasyon, sahne tasarımı, renk paleti ve görsel detaylarla bütüncül bir atmosfer oluşturuyoruz.",
        "hero_img": "images/konsept-hero.jpg",
        "items": [
            {"title": "Tema Yaratımı", "desc": "Amacınıza veya etkinliğin ana fikrine en uygun ve vurucu temayı belirleyerek ziyaretçilerin ilk saniyede etkilenmesini sağlıyoruz.", "img": "images/tema-yaratimi.jpg"},
            {"title": "Görsel ve Dekoratif İcra", "desc": "Mekan süslemesinden dijital panolara kadar kurduğumuz renk skalasından çıkmadan bütüncül ve stilize bir dekorasyon uyguluyoruz.", "img": "images/gorsel-icra.jpg"}
        ]
    },
    {
        "filename": "produksiyon.html",
        "title": "Prodüksiyon",
        "hero_desc": "Etkinlikleriniz için profesyonel teknik altyapı ve prodüksiyon hizmetleri sunuyoruz. Ses, ışık, sahne, görsel tasarım ve teknik ekip koordinasyonunu eksiksiz yönetiyoruz.",
        "hero_img": "images/produksiyon-hero.jpg",
        "items": [
            {"title": "Ses & Işık Tasarımı", "desc": "Etkinliğin büyüklüğüne ve dinamiğine uygun endüstri standartlarında modern teknik cihazlarla mükemmel görsel/işitsel uyum yaşatıyoruz.", "img": "images/ses-isik.jpg"},
            {"title": "Teknik Ekip Yönetimi", "desc": "Etkinlik esnasında krizlere mahal vermeyecek şekilde uzman teknisyenlerimizle sahne arkası yönetimini üstleniyoruz.", "img": "images/teknik-ekip.jpg"},
            {"title": "Sahne & LED Ekran Çözümleri", "desc": "Sanatçı, panelist veya gösterilerin izleyicilerle görsel bağını maksimuma çıkaracak etkileyici dev ekran ve podyum kurulumları.", "img": "images/sahne.jpg"}
        ]
    }
]

for page in pages:
    subs_html = make_sub_sections(page["items"])
    final_html = base_html.format(
        title=page["title"],
        hero_desc=page["hero_desc"],
        hero_img=page["hero_img"],
        sub_sections=subs_html
    )
    with open(page["filename"], "w", encoding="utf-8") as f:
        f.write(final_html)
    print("Created", page["filename"])
