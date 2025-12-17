from flask import Flask, render_template, request, redirect, url_for
import csv  # استيراد مكتبة CSV

app = Flask(_name_)

# المسار الرئيسي لعرض الصفحة الرئيسية (index.html)
@app.route('/')
def home():
    return render_template('index.html')

# المسار لعرض صفحة التقديم (apply.html)
@app.route('/apply.html')
def apply_form():
    return render_template('apply.html')

# المسار الذي يستقبل البيانات من النموذج
@app.route('/submit', methods=['POST'])
def submit_application():
    if request.method == 'POST':
        # استخراج البيانات من النموذج
        full_name = request.form['fullName']
        email = request.form['email']
        phone = request.form['phone']
        faculty = request.form['faculty']
        notes = request.form['notes']

        # إنشاء قائمة تحتوي على البيانات
        data = [full_name, email, phone, faculty, notes]
        
        # حفظ البيانات في ملف CSV
        with open('applications.csv', 'a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            
            # كتابة رؤوس الأعمدة إذا كان الملف فارغًا
            if file.tell() == 0:
                header = ['Full Name', 'Email', 'Phone', 'Faculty', 'Notes']
                writer.writerow(header)
                
            # كتابة البيانات الجديدة
            writer.writerow(data)
        
        print("تم حفظ الطلب الجديد بنجاح في ملف applications.csv")
        
        return "تم إرسال طلبك بنجاح! شكراً لك."

# تشغيل التطبيق
if _name_ == '_main_':
    app.run(debug=True)