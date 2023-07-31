import os
import subprocess

from mpris2 import get_players_uri


def meta_scrape (meta_name):
    #meta_name_full = meta_name_const + meta_name
    pos_start_1 = metadata.find(meta_name) + len(meta_name) + 1
    pos_start_1_trimm = metadata[pos_start_1:]
    pos_start_2 = pos_start_1_trimm.find("'") + 1
    meta1 = pos_start_1_trimm[pos_start_2:]
    pos_finish = meta1.find("'")
    meta = meta1[:pos_finish]

    return(meta)


try : 
    uri = next(get_players_uri())


    from mpris2 import Player

    player = Player(dbus_interface_info={'dbus_uri': uri})

    metadata = str(player.Metadata)
#meta_name_const = 'xesam:'


    result = []


    atributes = ["title","artist","artUrl","album"]

    for i in atributes:
        result.append(meta_scrape(i))



#lenght_atr = 'mpris:lenght'
    length_atr = "mpris:length'): dbus.UInt64("
    length_pos_start = metadata.find(length_atr) + len(length_atr)
    length_meta1 = metadata[length_pos_start:]
    length_pos_finish = length_meta1.find(",")
    length_meta = int(length_meta1[:length_pos_finish])

    result.append(length_meta)
#lenght_meta_final = int(lenght_meta) / 1000000

#print(f'{lenght_meta_final}s ({lenght_meta} raw)')


    curr_length = int(player.Position)

    result.append(curr_length)
#curr_lenght_s = int(curr_lenght) / 1000000
#print(f'{curr_lenght_s}s ({curr_lenght} raw)')

    percentage = (curr_length/length_meta)*100

    result.append(percentage)
#print(f'{(curr_lenght_s/meta_final)*100}%')


    playback = str(player.PlaybackStatus)

    result.append(playback)


    space = ''
    for i in range(len(result[7])-2):
        space = space + ' '

    result.append(space)
    
    """
    playstate = ['Playing','Paused','Stopped']
    playicon = [' ',' ',' ']

    for o in playstate:
        if result[7] == playstate[o]:
            result.append(playicon[o])#result[9]
    """

    state_icon = [['Playing','󰐊  '],['Paused','󰏤  '],['Stopped','󰓛  ']]
    for o in range(len(state_icon)):
        if result[7] == state_icon[o][0]:
            result.append(state_icon[o][1])
    

    top_lenght = len(str(result[7])+" "+"│ "+str(result[0])+" "+" "+str(result[1]))
    bot1_lenght = len("   "+str(result[8])+"│ "+str(result[3]))
    max_lenght = max(top_lenght,bot1_lenght)
    
    result.append(max_lenght)
    
    





    for u in result:
        print(u)

    # 󰩮

    os.system(f'dunstify -a MusicPlayer24 -h string:x-canonical-private-synchronous:title "{result[7]+" "}{"│ "+result[0]+" "}-{" "+result[1]}" "{"   "+result[8]+"│ "+result[3]}\n " -h int:value:{result[6]} -i "/home/nito/.local/share/icons/temp/test.jpg" -r 1424')
    #os.system(f'dunstify -a MusicPlayer24 -h string:x-canonical-private-synchronous:title "{result[7]+" "}{"│ "+result[0]+" "}-{" "+result[1]}" "{" "+result[8]+"│ "+result[3]}" -i "/home/nito/.local/share/icons/temp/test.jpg" -r 1424')
    #os.system(f'dunstify -a MusicPlayer24 -h string:x-canonical-private-synchronous:title " " "{result[9]}" -h int:value:{result[6]} -r 1425')

#os.system(f'dunstify -a MusicPlayer24 {result[0]} -h int:value:{result[6]} -r 1424')

except:
    #print("no audio player now")
    os.system('dunstify -a MusicPlayer24 "No music player active at the moment" -i "/home/nito/.local/share/icons/nomusic.png"')
#print(metadata)


#song_name 
