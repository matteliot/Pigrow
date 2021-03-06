#!/usr/bin/python
import os
s_val = "60"
c_val = "60"
g_val = "60"
b_val = "60"
x_dim = 1280
y_dim = 720
additonal_commands = "-d/dev/video0 -w"
loc_settings = "/home/pi/Pigrow/config/"
if not os.path.exists(loc_settings):
    os.makedirs(loc_settings)
loc_settings = loc_settings + "camera_settings.txt"

start_v = 10 #between 1-255
end_v = 100 #between 1-255
skip_v = 10 #ten represents value increase by ten

try:
    with open(loc_settings, "r") as f:
        for line in f:
            s_item = line.split("=")
            if s_item[0] == "s_val":
                s_val = s_item[1].split("\n")[0]
            elif s_item[0] == "c_val":
                c_val = s_item[1].split("\n")[0]
            elif s_item[0] == "g_val":
                g_val = s_item[1].split("\n")[0]
            elif s_item[0] == "b_val":
                b_val = s_item[1].split("\n")[0]
            elif s_item[0] == "x_dim":
                x_dim = s_item[1].split("\n")[0]
            elif s_item[0] == "y_dim":
                y_dim = s_item[1].split("\n")[0]
            elif s_item[0] == "additonal_commands":
                additonal_commands = s_item[1].split("\n")[0]
except:
    pass


def show_menu():
    global s_val
    global c_val
    global g_val
    global b_val
    print("----------------------------")
    print("---Camera test and config---")
    print("----------------------------")
    print("This will take a series of images with the camera")
    print("varying one of the settings to create a range from")
    print("which you can select the best configuration.")
    print("")
    print("Current settings; S = " + str(s_val) + "  C = " + str(c_val) + "  G = " + str(g_val) + "  B = " + str(b_val))
    print("  _______________________")
    print(" |Set value              |")
    print(" | 1 - Saturation        |")
    print(" | 2 - Contrast          |")
    print(" | 3 - Gain              ----------------------|")
    print(" | 4 - Brightness                              |")
    print(" |                      t - take and show test |")
    print(" |Take Range            r - range test         |")
    print(" | 5 - Saturation        ----------------------|")
    print(" | 6 - Contrast          |")
    print(" | 7 - Gain              |")
    print(" | 8 - Brightness        |")
    print(" |                       -------------")
    print(" | s - Save Config File to Disk      |")
    print(" | 0 - Delete Images       q to quit |")
    print("  ___________________________________|")
    print("")
    option = raw_input("Type the number and press return;")
    if option == "1":
        s_val = raw_input("Input value to use for Saturation..")
        show_menu()
    elif option == "2":
        c_val = raw_input("Input value to use for Contrast..")
        show_menu()
    elif option == "3":
        g_val = raw_input("Input value to use for Gain..")
        show_menu()
    elif option == "4":
        b_val = raw_input("Input value to use for Brightness..")
        show_menu()

    elif option == "5":
        print("Capturing range of Saturation images...")
        for s in range(start_v,end_v,skip_v):
            print("---Doing: sudo uvccapture "+additonal_commands +" -S"+str(s)+" -C" + c_val + " -G"+ g_val +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_s_"+str(s)+".jpg")
            os.system("sudo uvccapture "+additonal_commands +" -S"+str(s)+" -C" + c_val + " -G"+ g_val +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_s_"+str(s)+".jpg")
        print("Range captured, view and select best value..")
        os.system("gpicview test_range_s_"+str(start_v)+".jpg")
        s_val = raw_input("Input value to use for Saturation..")
        show_menu()

    elif option == "6":
        print("Capturing range of Contrast images...")
        for c in range(start_v,end_v,skip_v):
            print("---Doing: sudo uvccapture "+additonal_commands +" -S"+s_val+" -C" + str(c) + " -G"+ g_val +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_c_"+str(c)+".jpg")
            os.system("sudo uvccapture "+additonal_commands+" -S"+s_val+" -C" + str(c) + " -G"+ g_val +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_c_"+str(c)+".jpg")
        print("Range captured, view and select best value..")
        os.system("gpicview test_range_c_"+str(start_v)+".jpg")
        c_val = raw_input("Input value to use for Contrast..")
        show_menu()

    elif option == "7":
        print("Capturing range of Gain images...")
        for g in range(start_v,end_v,skip_v):
            print("---Doing: sudo uvccapture "+additonal_commands +" -S"+s_val+" -C" + c_val + " -G"+ str(g) +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_c_"+str(g)+".jpg")
            os.system("sudo uvccapture "+additonal_commands+" -S"+s_val+" -C" + c_val + " -G"+ str(g) +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_g_"+str(g)+".jpg")
        print("Range captured, view and select best value..")
        os.system("gpicview test_range_g_"+str(start_v)+".jpg")
        g_val = raw_input("Input value to use for Gain..")
        show_menu()

    elif option == "8":
        print("Capturing range of Brightness images...")
        for b in range(start_v,end_v,skip_v):
            print("---Doing: sudo uvccapture "+additonal_commands +" -S"+s_val+" -C" + c_val + " -G"+ g_val +" -B"+ str(b) +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_b_"+str(b)+".jpg")
            os.system("sudo uvccapture "+additonal_commands+" -S"+s_val+" -C" + c_val + " -G"+ g_val +" -B"+ str(b) +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_b_"+str(b)+".jpg")
        print("Range captured, view and select best value..")
        os.system("gpicview test_range_b_"+str(start_v)+".jpg")
        b_val = raw_input("Input value to use for Brightness..")
        show_menu()

    elif option == "0":
        os.system("sudo rm test_range_*.jpg")
        print("Images deleted")
        show_menu()
    elif option == "t":
        print("Using current configuration to take image...")
        os.system("sudo uvccapture "+additonal_commands+" -S"+s_val+" -C" + c_val + " -G"+ g_val +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_test.jpg")
        os.system("gpicview test_range_test.jpg")
        show_menu()

    elif option == "r":
        print("Testing stability using current configuration to take range...")
        for x in range(1,10):
            os.system("sudo uvccapture "+additonal_commands+" -S"+s_val+" -C" + c_val + " -G"+ g_val +" -B"+ b_val +" -x"+str(x_dim)+" -y"+str(y_dim)+" -v -t0 -otest_range_range_test_"+str(x)+".jpg")
        os.system("gpicview test_range_range_test_1.jpg")
        show_menu()

    elif option == "s":
        print("Saving configuration file...")
        with open(loc_settings, "w") as f:
            f.write("s_val="+s_val+"\n")
            f.write("c_val="+c_val+"\n")
            f.write("g_val="+g_val+"\n")
            f.write("b_val="+b_val+"\n")
            f.write("x_dim="+str(x_dim)+"\n")
            f.write("y_dim="+str(y_dim)+"\n")
            f.write("additonal_commands="+additonal_commands+ "\n")
        print("Config Saved")
        show_menu()
    elif option == "q" or option == "Q" or option == "":
        exit()
    else:
        print("That wasn't an option...")
        show_menu()

show_menu()

print "done"
