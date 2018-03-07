import re
import urllib

def sort_times(times):
    i = 0
    
    while i < len(times):
        if len(times[i]) == 6:
            times[i] = '0' + times[i]
        i+=1
        
    return sorted(times)

def add_twenty(time):
    time = time.split(':')
    hour = int(time[0])
    minute = int(time[1][:-2])
    minute += 20

    #keep the time in 12-hour format
    if minute > 60:
        hour += 1
        if hour > 12:
            hour -= 12
        minute -= 60
    elif minute == 60:
        hour += 1
        if hour > 12:
            hour -= 12
        minute = 0

    #we will never close earlier than 10
    if hour >= 10 and hour < 12:
        ampm = "pm"
    else:
        ampm = "am"
    close_time = format_time(hour, minute, ampm)
    
    return close_time

def format_time(hour, minute, ampm):
    hour = str(hour)
    minute = str(minute)
    
    if len(hour) == 1:
        hour = '0' + hour
    if len(minute) == 1:
        minute = '0' + minute
    
    return hour + ':' + minute + ampm

def main():
    html = urllib.urlopen("https://www.regmovies.com/theaters/regal-winter-park-village-stadium-20-rpx/C00183409869")
    htmltext = html.read()

    print htmltext
    
    times = re.findall(r'.+role="button"> (.+) PM </a>', htmltext)
    
    times = sort_times(times)

    print len(times)
    
    #remove 12pm from the list of times
    while times[-1].split(':')[0] == '12':
        times.pop(-1)

    print "The last showing is at", times[-1]
    print "Close is at", add_twenty(times[-1])

if __name__ == "__main__":
    main()
