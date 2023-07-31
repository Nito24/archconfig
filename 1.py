from os import system as run_cmd

from mpris2 import get_players_uri


def meta_scrape (meta_name):
    pos_start_1 = metadata.find(meta_name) + len(meta_name) + 1
    pos_start_1_trimm = metadata[pos_start_1:]
    pos_start_2 = pos_start_1_trimm.find("'") + 1
    meta1 = pos_start_1_trimm[pos_start_2:]
    pos_finish = meta1.find("'")
    meta = meta1[:pos_finish]
    
    return(meta)


def bottom_bar (total_lenght, icon, curr_time, total_time):
    in_const = '  '
    pre_result = in_const + icon + in_const + in_const
    
    curr_time_m = (curr_time/1000000)//60
    curr_time_s = (curr_time/1000000)%60
    total_time_m = (total_time/1000000)//60
    total_time_s = (total_time/1000000)%60
    
    curr_time_str = str(curr_time_m) + ':' + str(curr_time_s) + ' '
    total_time_str = ' ' + str(total_time_m) + ':' + str(total_time_s)
    
    line_character = '⎯'
    line = ''
    for i in range(len(curr_time_str + total_time_str)):
        line = line + line_character
    
    final = pre_result + curr_time + line + total_time
    
    return final


# If player is running
try : 
    uri = next(get_players_uri())
    
    from mpris2 import Player

    player = Player(dbus_interface_info={'dbus_uri': uri})

    metadata = str(player.Metadata)


    result = []


    atributes = ["title","artist","artUrl","album"]

    for i in atributes:
        result.append(meta_scrape(i))



    length_atr = "mpris:length'): dbus.UInt64("
    length_pos_start = metadata.find(length_atr) + len(length_atr)
    length_meta1 = metadata[length_pos_start:]
    length_pos_finish = length_meta1.find(",")
    length_meta = int(length_meta1[:length_pos_finish])

    result.append(length_meta)



    curr_length = int(player.Position)

    result.append(curr_length)

    percentage = (curr_length/length_meta)*100

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
    

    top_lenght = len(str(result[7])+" "+"│ "+str(result[0])+" "+" "+str(result[1]))
    bot1_lenght = len("   "+str(result[8])+"│ "+str(result[3]))
    max_lenght = max(top_lenght,bot1_lenght)
    
    result.append(max_lenght)
    
    bottom_bar (max_lenght, result[9], result[5], result[4]):

    for u in result:
        print(u)


    run_cmd(f'dunstify -a MusicPlayer24 -h string:x-canonical-private-synchronous:title "{result[7]+" "}{"│ "+result[0]+" "}-{" "+result[1]}" "{"   "+result[8]+"│ "+result[3]}\n " -h int:value:{result[6]} -i "/home/nito/.local/share/icons/temp/test.jpg" -r 1424')


# No music player detected
except:
    run_cmd('dunstify -a MusicPlayer24 "No music player active at the moment" -i "/home/nito/.local/share/icons/nomusic.png"')




