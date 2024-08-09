import pyautogui,keyboard,win32gui,win32con,os,ctypes,time,threading,multiprocessing,dearpygui.dearpygui as pg

    #some shit to make pygui work lol
pg.create_context()
    #until here

with pg.window(autosize=True,no_move=True,no_title_bar=True,tag="PWINDOW"):
    pg.add_text("           Please select how many Cookies you are buying.")
    pg.add_text("1 = Just one! | 2 = A half-dozen! (6) | 3 = Get me a dozen! (12)")
    pg.add_slider_int(min_value=1,default_value=1,max_value=3,tag="option")
    pg.add_button(label="Start",tag="btn1")
    print(pg.get_item_state("btn1"))

    #pygui cleanup
pg.create_viewport(title="0xb0's Skyblock Scripts",width=500,height=100,resizable=False,always_on_top=True,clear_color=(25,25,26,255))
pg.setup_dearpygui()
pg.show_viewport()
pg.set_primary_window("PWINDOW", True)
pg.start_dearpygui()
pg.destroy_context()
    #ends here