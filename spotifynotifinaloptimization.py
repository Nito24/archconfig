from os import system as run_cmd
from os import listdir as listdirectory

from mpris2 import get_players_uri


def meta_scrape (meta_name, start, end):
    pos_start_1 = metadata.find(meta_name) + len(meta_name) + 1
    pos_start_1_trimm = metadata[pos_start_1:]
    pos_start_2 = pos_start_1_trimm.find(start) + 1
    meta1 = pos_start_1_trimm[pos_start_2:]
    pos_finish = meta1.find(end)
    meta = meta1[:pos_finish]
    
    return meta



def bottom_bar (total_lenght, icon, curr_time, total_time):    
    curr_time_m = '{:.0f}'.format(((curr_time/1000000)//60))

    curr_time_s = '{:.0f}'.format(((curr_time/1000000)%60))
    curr_time_s2 = '{:02d}'.format(int(curr_time_s))

    total_time_m = '{:.0f}'.format(((total_time/1000000)//60))

    total_time_s = '{:.0f}'.format(((total_time/1000000)%60))
    total_time_s2 = '{:02d}'.format(int(total_time_s))

    
    curr_time_str = str(curr_time_m) + ':' + str(curr_time_s2) + ' '
    total_time_str = ' ' + str(total_time_m) + ':' + str(total_time_s2)

    line = ''
    if total_lenght > 44:
        for i in range(total_lenght-len(curr_time_str + total_time_str)-4):
            line = line + '─'
        line = '├' + line + '┤'

    else:
        for i in range(17+len(curr_time_str + total_time_str)-4):
            line = line + '─'
        line = '├' + line + '┤' 
    
    return ('   ' + icon + ' ' + curr_time_str + line + total_time_str)
    


def down_icon (url, artist, album):
    bar = (url[::-1]).find('/')
    name = url[len(url)-bar:]
    
    icon_name = 'icon_' + artist.strip(' ') + '_' + album.strip(' ')
    
    available_icons = listdirectory('/home/nito/.local/share/icons/temp')

    if (icon_name + '.jpg') not in available_icons:
        run_cmd(f"cd /home/nito/.local/share/icons/temp/ ; wget -q {url} ; mv {name} '{icon_name}.jpg'")
    
    return('/home/nito/.local/share/icons/temp/' + f"{icon_name}.jpg")

    

# If player is running
try :
    #print([uri for uri in get_players_uri()])
    uri = 'org.mpris.MediaPlayer2.spotify' #hard set to spotify player, improvements coming to support more players
    
    from mpris2 import Player

    player = Player(dbus_interface_info={'dbus_uri': uri})

    metadata = str(player.Metadata)


    result = [] # Title, artist, artURL, album, totaltime, currentime, percentage, playbackstatus, 2ndlinespace(playback), playbackicon, maxlenght, iconpath 


    atributes = ["title","artist","artUrl","album"]
    
    #print(metadata)

    for i in atributes:
        met = meta_scrape(i, "'", "'")
        if '"' in met:
            result.append((meta_scrape(i, '"', '"')).replace("'",'’'))
        else:
            result.append(met)
        #result.append(meta_scrape(i, "'", "'"))

    
    result.append(int(meta_scrape("mpris:length","(",",")))


    curr_length = int(player.Position)
    result.append(curr_length)

    percentage = (curr_length/result[4])*100
    result.append(percentage)


    playback = str(player.PlaybackStatus)

    result.append(playback)


    space = ''
    for i in range(len(result[7])-2):
        space = space + ' '

    result.append(space)
    
    state_icon = [['Playing','󰐊  '],['Paused','󰏤  '],['Stopped','󰓛  ']]
    for o in range(len(state_icon)):
        if result[7] == state_icon[o][0]:
            result.append(state_icon[o][1])
    

    top_lenght = len(str(result[7])+str(result[0])+str(result[1]))+5    
    bot1_lenght = len(str(result[8])+str(result[3]))+5
    max_lenght = max(top_lenght,bot1_lenght)
    
    result.append(max_lenght)
    
    bot = bottom_bar(max_lenght, result[9], result[5], result[4])

    result.append(down_icon(result[2], result[1], result[3]))
    run_cmd(f"""dunstify -a MusicPlayer24 -h string:x-canonical-private-synchronous:title '{result[7]+' '}│ {result[0]} -{' '+result[1]}' '{'   '+result[8]+'│ '+result[3]}\n\n{bot}' -h int:value:{result[6]} -i '{result[11]}' -r 1424""")


# No music player detected
except Exception as error:
    run_cmd('dunstify -a MusicPlayer24 "No music player active at the moment" -i "/home/nito/.local/share/icons/nomusic.png"')
    print(error)
