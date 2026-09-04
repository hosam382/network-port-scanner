import socket
import sys
from datetime import datetime

# أداة فحص المنافذ البسيطة (Port Scanner) للأغراض التعليمية والأمنية
def scan_target():
    target = input("أدخل عنوان الهدف أو الـ IP للفحص: ")
    print("-" * 50)
    print(جاري فحص الهدف: {target})
    print(وقت بدء الفحص: {str(datetime.now())})
    print("-" * 50)

    try:
        # فحص المنافذ الأساسية الشائعة (مثل المنافذ من 1 إلى 100)
        for port in range(1, 100):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            
            # محاولة الاتصال بالمنفذ
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"المنفذ {port} : مفتوح (Open)")
            s.close()
            
    except KeyboardInterrupt:
        print("\nتم إيقاف الفحص بواسطة المستخدم.")
        sys.exit()
    except socket.gaierror:
        print("\nتعذر العثور على عنوان المضيف.")
        sys.exit()
    except socket.error:
        print("\nتعذر الاتصال بالخادم.")
        sys.exit()

if __name__ == "__main__":
    scan_target()
