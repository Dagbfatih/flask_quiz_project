from src.server.models.exam import Exam
from src.server.models.question import Question
from src.server.configs.db import db
from src.server.core.seeders import BaseSeeder


class ExamSeeder(BaseSeeder.BaseSeeder):
    @staticmethod
    def seed():
        # Create an exam with fixed values
        exam = Exam(
            name="Web and Networking Fundamentals Quiz",
            description="This quiz tests fundamental concepts of web development and networking.",
        )
        db.session.add(exam)
        db.session.commit()

        # Manually define questions
        questions = [
            Question(
                question_text="Tarayıcı (Chrome veya Edge gibi) bir web sitesini nereden çözümlemeye başlar?",
                choice_a="styles.css",
                choice_b="app.js",
                choice_c="index.html",
                choice_d="server.py",
                correct_answer="C",
                exam_id=exam.id,
            ),
            Question(
                question_text="Bir web sitesi oluştururken en önemli husus nedir?",
                choice_a="Sitenin çok fazla animasyon içermesi",
                choice_b="Kullanıcı dostu ve kolay kullanılabilir tasarım",
                choice_c="Sayfanın arka plan renginin dikkat çekici olması",
                choice_d="Sadece masaüstü cihazlar için uyumlu olması",
                correct_answer="B",
                exam_id=exam.id,
            ),
            Question(
                question_text="Bir web sitesi ilk açıldığında neden bazen yavaş yüklenir?",
                choice_a="İnternetin sabahları daha yavaş çalışması nedeniyle",
                choice_b="Sunucuya çok fazla kişinin aynı anda bağlanması nedeniyle",
                choice_c="Bilgisayarın saatine bağlı olarak değişir",
                choice_d="Tarayıcının yeni sekmeler açmasını beklemesi gerekir",
                correct_answer="B",
                exam_id=exam.id,
            ),
            Question(
                question_text="Bir web sitesine girdiğinde ‘404 Hatası’ görürsen ne anlama gelir?",
                choice_a="Sayfanın başarıyla yüklendiğini",
                choice_b="İnternet bağlantının kesildiğini",
                choice_c="Aradığın sayfanın mevcut olmadığını",
                choice_d="Web sitesinin bakımda olduğunu",
                correct_answer="C",
                exam_id=exam.id,
            ),
            Question(
                question_text="Tarayıcına bir web sitesi adresi yazıp enter’a bastığında, ilk olarak hangi işlem gerçekleşir?",
                choice_a="Sunucu sayfanın içeriğini hemen gönderir",
                choice_b="Tarayıcı, DNS sunucusundan sitenin IP adresini öğrenir",
                choice_c="Tarayıcı sayfanın resimlerini indirir",
                choice_d="Bilgisayar, internet hızını kontrol eder",
                correct_answer="B",
                exam_id=exam.id,
            ),
            Question(
                question_text="Web sitelerinin ‘https’ ile başlaması ne anlama gelir?",
                choice_a="Site içinde kullanılan tüm görsellerin yüksek kaliteli olduğunu",
                choice_b="Kullanıcı verilerinin güvenli bir şekilde şifrelendiğini",
                choice_c="Sitenin daha hızlı yüklendiğini",
                choice_d="Tarayıcının siteyi önceden kaydettiğini",
                correct_answer="B",
                exam_id=exam.id,
            ),
            Question(
                question_text="Bir web sitesinde gezinirken, bilgilerinin güvende olup olmadığını nasıl anlayabilirsin?",
                choice_a="Adres çubuğunda kilit simgesi olup olmadığına bakarak",
                choice_b="Web sitesinin tasarımına göre karar vererek",
                choice_c="Sitenin yüklenme süresine bakarak",
                choice_d="Sayfanın tamamen beyaz olup olmamasına göre",
                correct_answer="A",
                exam_id=exam.id,
            ),
            Question(
                question_text="Bir web sitesinin birden fazla cihazda düzgün görünmesini sağlayan teknik nedir?",
                choice_a="Responsive (Duyarlı) Tasarım",
                choice_b="Yüksek Çözünürlüklü Mod",
                choice_c="Tarayıcı Önbellekleme",
                choice_d="Sayfa Kaydırma Optimizasyonu",
                correct_answer="A",
                exam_id=exam.id,
            ),
        ]

        # Insert questions into the database
        db.session.bulk_save_objects(questions)
        db.session.commit()

        print("Manually seeded exam and questions successfully!")
