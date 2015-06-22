# program "Stopwatch: The Game"
# Saurabh Patel
# skpatel@syr.edu

 #import modules
import simplegui

# define global variables
current_time = 0 
width = 300
height = 300
interval = 100
position = [100,150]
result_position = [200,50]
total_attempts = 0
won = 0
result = "0/0"
timeString = "0:00:0"

def result_format(won,total_attempts):
    return "'" + str(won) + "/" + str(total_attempts) + "'"


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    minutes = time / 600
    seconds1 = (time / 100) % 6
    seconds2 = (time / 10) % 10
    milliseconds = time % 10
    # string representation of the formatted time
    message = str(minutes) + ':' + str(seconds1) + str(seconds2) + '.' + str(milliseconds)
    return message
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    timer.start()
    
def stop_button_handler():
    timer.stop()
    last_digit = int(timeString[-1:])
    global won,total_attempts
    if(last_digit == 0) :
        won = won+1
        total_attempts+=1
    else :
        total_attempts+=1
        
    
    
def reset_button_handler():
    timer.stop()
    global result, timeString,current_time
    result = "0/0"
    timeString = "0:00:0"
    current_time = 0
    

# define event handler for timer with 0.1 sec interval
def timer_event_handler():
    global current_time, timeString
    current_time = current_time +1
    timeString = format(current_time)

# define draw handler
def draw(canvas) :
    canvas.draw_text(str(timeString), position, 40, "white")
    canvas.draw_text(result_format(won,total_attempts), result_position, 36, "green")

    
# Create a frame 
frame = simplegui.create_frame("Stop Watch", width, height)
timer = simplegui.create_timer(interval, timer_event_handler)

# Register event handlers
frame.add_button("Start", start_button_handler, 200)
frame.add_button("Stop", stop_button_handler, 200)
frame.add_button("Reset", reset_button_handler, 200)


# Start the frame animation
frame.start()
frame.set_draw_handler(draw)


