from customtkinter import *
from tkinter import messagebox
from PIL import Image
import os

#masukan gambar
delete_image = CTkImage(Image.open(os.path.join("TA\\images\\delete.png")), size=(20, 20))
edit_image = CTkImage(Image.open(os.path.join("TA\\images\\edit.png")), size=(20, 20))

# Perulangan utama Main Window
n = 1
for n in range(n):
    set_appearance_mode("dark")
    Main = CTk(fg_color="black")
    Main.minsize (width=700, height=400)
    Main.title("Notes App")

    class Notes_App:
        def __init__(self, master):
            self.Main = master

            #tampilan awal aplikasi
            frame = CTkFrame(self.Main, fg_color="transparent", height=50)
            frame.pack(pady=10, fill='x')
            
            tombol = CTkButton(master=frame, text='+', command=self.tambah_note)
            tombol.pack(side='right', padx=20)

            Judul_aplikasi = CTkLabel(master=frame, text="NOTE APP", text_color='white', font=('poppins', 30, 'bold'))
            Judul_aplikasi.pack(side='left', padx=20)

            self.framecatatan =  CTkScrollableFrame(master=self.Main, fg_color='transparent', height=300)
            self.framecatatan.pack(padx=20,pady=2,fill='both')

        def tambah_note(self):
            #window tambahkan catatan
            window_tulis = CTkToplevel(fg_color='black')
            window_tulis.title("Note")
            window_tulis.minsize(width=400, height=300)
            
            #setter catatan
            judul_catatan = CTkEntry(master=window_tulis, placeholder_text="Judul", fg_color='transparent', font=('poppins', 14, 'bold'))
            judul_catatan.pack(fill="x", anchor='n', pady=20, padx=20)

            labelkonten = CTkLabel(master=window_tulis, text='catatan')
            labelkonten.place(x=25, y=50)
            konten = CTkTextbox(master=window_tulis, fg_color='transparent', font=('poppins', 14), border_color='white', border_width=1)
            konten.pack( padx=20, pady=10, fill=BOTH)


        #fungsi menambahkan catatan (save)
            def save_file():
                #getter
                judulnya = judul_catatan.get()
                isikonten = konten.get('0.0', END)
                if isikonten == "" or judulnya == "":
                    messagebox.showerror(title='error', message='data tidak lengkap')
                else:
                    newnote = CTkFrame(master=self.framecatatan, fg_color='grey', height=100)
                    newnote.pack(fill='x', pady=10)

                    framejudul = CTkFrame(master=newnote, fg_color='transparent', height=12)
                    framejudul.pack(fill='x', padx=5)

                    frameisi = CTkFrame(master=newnote, fg_color='transparent', height=36)
                    frameisi.pack(fill='x', padx=5)

                    jdul = CTkLabel(master=framejudul, text_color='black', text=judul_catatan.get(), font=('poppins', 14, 'bold'))
                    jdul.pack(side='left', padx=3)
                    isi = CTkLabel(master=frameisi, text_color='black', text=konten.get('0.0', END), justify='left')
                    isi.pack(side='left', padx=3)
                    window_tulis.destroy()

                # fungsi menghapus note
                def hapus_note():
                    newnote.destroy()

                tombol_delete = CTkButton(master=frameisi, image=delete_image, text='', fg_color='transparent', command=hapus_note, width=20, height=20)
                tombol_delete.pack(anchor='se')

                # fungsi update note
                def update_note():
                    window_tulis = CTkToplevel(fg_color='black')
                    window_tulis.title("Edit Note")
                    window_tulis.minsize(width=400, height=300)
                    window_tulis.focus()

                    judul_catatan = CTkEntry(master=window_tulis, placeholder_text="Judul", fg_color='transparent', font=('poppins', 14, 'bold'))
                    judul_catatan.pack(fill="x", anchor='n', pady=20, padx=20)
                    judul_catatan.insert(0, jdul.cget(attribute_name='text'))

                    labelkonten = CTkLabel(master=window_tulis, text='catatan')
                    labelkonten.place(x=25, y=50)
                    konten = CTkTextbox(master=window_tulis, fg_color='transparent', font=('poppins', 14), border_color='white', border_width=1)
                    konten.pack(padx=20, pady=10, fill=BOTH)
                    konten.insert('0.0', isi.cget(attribute_name='text'))

                    def apply_update():
                        new_title = judul_catatan.get()
                        new_content = konten.get('1.0', 'end')

                        jdul.configure(text=new_title)
                        isi.configure(text=new_content)
                        window_tulis.destroy()

                    tombol_update = CTkButton(master=window_tulis, text='apply update', command=apply_update)
                    tombol_update.pack(side='bottom', fill='x', padx=25, pady=10)

                tombol_edit = CTkButton(master=frameisi, image=edit_image, text='', fg_color='transparent', command=update_note, width=20, height=20)
                tombol_edit.pack(anchor='se')

                

            def close():
                window_tulis.destroy()
            
                
            frame_tombol = CTkFrame(master=window_tulis, height=60, fg_color='transparent')
            frame_tombol.pack( side='bottom', padx=10, pady=10)
                
            tombol_cancel = CTkButton(master=frame_tombol, text='cancel', command=close)
            tombol_cancel.pack(side='left',fill='x', padx=25)
            tombol_save = CTkButton(master=frame_tombol, text='save', command=save_file)
            tombol_save.pack(side='left',fill='x', padx=25)
            window_tulis.focus()
                
                
    
Notes_App(Main)
Main.mainloop()