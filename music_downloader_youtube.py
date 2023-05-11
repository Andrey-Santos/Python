from pytube import YouTube

link = input("Enter the link of YouTube video you want to download:  ")
yt = YouTube(link) 

print("Searching audio track...")

# Filtra as streams progressivas em formato MP4, ordena por resolução e seleciona a melhor (maior) resolução
best_stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

# Faz o download da melhor stream disponível
best_stream.download()
