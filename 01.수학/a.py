def solution(m, musicinfos):
    find_list = []
    replace_note = {'A#':'a','C#':'c','D#':'d','F#':'f','G#':'g'}
    
    for i in replace_note:
        if i in m:
            m = m.replace(i, replace_note[i])
    print(m)
    
    for info in musicinfos:
        start_time, end_time, title, body, = info.split(",")
        
        start_hour, start_miniutes = map(int,start_time.split(":"))
        end_hour, end_miniutes = map(int, end_time.split(":"))
        
        play_time = (end_hour-start_hour)*60 + (end_miniutes-start_miniutes)
        
        body_lenght = len(body)
        full_body = ""
        for i in range(play_time):
            full_body = full_body + body[i%body_lenght]
        
        for i in replace_note:
            if i in full_body:
                full_body = full_body.replace(i, replace_note[i])
        
        find_song = []
        if m in full_body:
            find_song.append(title)
            find_song.append(play_time)
            find_list.append(find_song)
    
    print(find_list)
    max_time = 0
    max_title = ""
    for title, time in find_list:
        if int(time) > int(max_time):
            max_time = time
            max_title = title
    print(max_title)
    
    if len(find_list) == 0:
        return "(None)"
    else:
        return max_title

print(solution(		"ABC#", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))