# Que me cuadre dropeoa baten bakarrik, edo () tarte bat egotie desafine eta afinetako
# Haizezkoak separeu turnotan deskantsuek eukitzeko (bat hasieran, bat amaieran)
# Potente hasi, potente amaitzu eta dinamika bitzartien (bai hasteko bai amaitzeko kantak ultra kontroleta egonbidie, hobienetariko sonetan dabienak izenbidie, eta berdiñe deskantsue baño ariñau eta gerokoak)
# Zentzu historiko apurbet kantan kokapenagaz, istori bat kontetie
# Tonalidadien arteko antzekotasune kanta batetik bestera, eta segiduen eitzeko kasuen iñor ez egotie konpromissed
# Bai Helen bai edonorentzat bi kanta fisikoki potente segiduen ekidin
# Nun joten dogunan arabera aukeratu kantak eta ordena
# Generoan arteko kongruentzi bai barietatie
# Tenpoan arteko bai antzekotasun bai kontrastie, depende lo que interese

song_list = 'atarata.txt'

def song_info(song_list):
    '''
    This function takes the list of songs the band is familiar with as an input and converts it to a dictionary 
    where the key is the name of the song and the values are relevant information in order to decide the order
    in which the songs will be played.
    '''
    song_dict = {}
    file = open(song_list, "r")
    for line in file:
        words = line.strip('\n').split('-')
        name = words.pop(0)
        song_dict[name] = words
    file.close()
    return song_dict

def rep_time(song_dict, set_time = 0):
    '''
    This function gathers the dictionary with the song list information, as well as the time that the set will endure
    written in hours. It will output a matrix with all the combinations of the song orders that get close to that time 
    while being under it. It will also score positively the lists that are around 10 minutes under. Over set_time times
    as well as under 30 min combinations will be discarted.
    '''
    times = []
    current_tot_time = 0
    for song in song_dict:
        times.append(song_dict[song][3])
    for time in times:
        if time == '':
            continue
        else:
            elem = time.split("'")
            current_tot_time += ((int(elem[0])*60 + int(elem[1]))/60)/60
    return current_tot_time
    

def key_relation():
    cq_maj = ['C', 'G', 'D', 'A', 'E', 'B', 'F#', 'Db', 'Ab', 'Eb', 'Bb', 'F']  # Circulo de quintas mayor
    cq_min = ['Am', 'Em', 'Bm', 'F#m', 'Dbm', 'Abm', 'Ebm', 'Bbm', 'Fm', 'Cm', 'Gm', 'Dm']  # Circulo de quintas menor
    return True

song_dict = song_info(song_list)
print(rep_time(song_dict, 0))

