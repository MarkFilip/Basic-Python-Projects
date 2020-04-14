import os       #Necessary to access files
import time     #Necessary to convert time to a date


def file_fullPath(path,file_name):
    """
        Joins the directory and the file path
        to get the absolute file path
    """
    full_path = os.path.join(path,file_name)
    return full_path

def file_date_modified(full_path):
    """
        Gets the time the file was last modified
        initially in seconds since epoch and then
        converts it to a date that is understandable
    """
    date_mod = os.path.getmtime(full_path)
    time_obj = time.localtime(date_mod)    #Results in a tuple so elements need to be referenced
    #time_obj[3] is hours 0-24 so it must be converted to say AM or PM and stay between 1-12
    if time_obj[3] > 12:
        date_mod = ("{}/{}/{}\t {}:{} PM".format(time_obj[1],time_obj[2],time_obj[0],(time_obj[3]-12),time_obj[4]))
    elif time_obj[3] == 12:
        date_mod = ("{}/{}/{}\t 12:{} PM".format(time_obj[1],time_obj[2],time_obj[0],time_obj[4]))
    elif time_obj[3] == 0:
        date_mod = ("{}/{}/{}\t 12:{} AM".format(time_obj[1],time_obj[2],time_obj[0],time_obj[4]))
    else:
        date_mod = ("{}/{}/{}\t {}:{} AM".format(time_obj[1],time_obj[2],time_obj[0],time_obj[3],time_obj[4]))
    return date_mod


if __name__ == "__main__":

    
    dir_path = 'C:\\Users\\markf\\OneDrive\\Desktop\\Tech Academy\\The-Tech-Academy-Basic-Python-Projects\\First Drill'

    file_list = os.listdir(dir_path)
    # cycle through each file and then prints
    # the file path and date last modified if 
    # it is a .txt file

    for i in file_list:
        if i.endswith('.txt') == True:
            full_path = file_fullPath(dir_path,i)
            print("\nFile path:\n")
            print(full_path)
            date_mod = file_date_modified(full_path)
            print("\nDate last modified (MM/DD/YYYY):\n")
            print(date_mod)
            
        
