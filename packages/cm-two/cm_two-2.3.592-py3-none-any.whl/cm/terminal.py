import timeit
import traceback
from tkinter import *
from tkinter import ttk
import _thread as thread
from glob import glob
import datetime, threading, time
from cm.configs import config as s
from cm.widgets.drop_down_combobox import AutocompleteCombobox, AutocompleteComboboxCarNumber
from PIL import ImageFilter, Image, ImageTk
from traceback import format_exc
from time import sleep
import cm.styles.color_solutions as cs
from cm.styles import fonts
from cm.styles import element_sizes as el_sizes
from collections.abc import Iterable
from cm.gcore_interaction import db_functions
import pyautogui


class Terminal:
    """Супер-класс для всех остальных модулей-окон (статистика, диспуты и проч)"""

    def __init__(self, root, settings, operator, can):
        self.name = 'root'
        self.operator = operator
        self.root = root
        self.fgsm_gate_open = None
        self.w = settings.screenwidth
        self.h = settings.screenheight
        self.screencenter = self.w / 2
        self.screenmiddle = (self.screencenter, self.h / 2)
        self.font = '"Montserrat SemiBold" 11'
        self.title = ''  # Название окна, должно быть предопределено
        self.settings = settings
        self.rootdir = self.settings.rootdir
        self.screensize = '{}x{}'.format(self.w, self.h)
        self.can = can
        self.textcolor = '#BABABA'
        self.clockLaunched = False
        self.dayDisputs = {}
        self.poligonsList = []
        self.ifDisputs = 0
        self.hiden_widgets = []
        self.errors = []
        self.trash = []
        self.messagewas = False
        self.abort_round_btn = self.get_create_btn(settings.abort_round[0])
        self.mutex = thread.allocate_lock()
        self.cickling = True
        self.weightlist = [0]
        self.userRole = 'moder'
        self.orupState = False
        self.abort_all_errors_shown()
        self.blockImgDrawn = False
        self.orupMode = 'enter'
        self.listname = []
        self.gate_arrow_imgs = {}
        self.win_widgets = []
        self.blurDrawn = False
        self.car_choose_mode = 'auto'
        self.car_detected_source = None
        self.carnum_was = ''
        self.car_protocol = None
        self.sent_car_number = None
        self.trail_win_drawn = False
        self.weight_too_little = False
        self.blured_masks = {}
        self.cam_zoom = False
        self.root.wm_title("Gravity")
        self.orup_imgs = []

    def carnumCallback(self, P):
        '''Вызывается каждый раз, когда в поле для ввода гос номера на
		въездном ОРУП случается событие типа write'''
        boolean = False
        if P == "":
            # Нужно для того, что бы можно было стирать ввод
            return True
        else:
            if len(P) > 9:
                # Некорректная длина номера, не позволять длину больше 9
                return False
            for p in P:
                if p in s.allowed_carnum_symbols or str.isdigit(p) or p == "":
                    # Проверить вводимый символ на факт нахождения в списке допустимых
                    boolean = True
                else:
                    boolean = False
            return boolean

    def launchingOperations(self):
        threading.Thread(target=self.checking_thread).start()
        self.operator.ar_qdk.capture_cm_launched()

    def creating_canvas(self, master, bg):
        self.can.delete('maincanv', 'statusel', 'win', 'tree')
        obj = self.getAttrByName(bg)
        self.can.create_image(obj[1], obj[2], image=obj[3],
                              anchor=NW, tag='maincanv')

    def drawSlices(self, mode='def'):
        '''Рисует слоя (градиент,фонт) и накладывает их друг на друга'''
        if mode == 'AuthWin':
            # obj = self.getAttrByName('gradient')
            self.drawWin('maincanv', 'logo', 'login', 'password')
            # self.can.create_image(obj[1], obj[2], image=obj[3],
            #                      anchor=NW, tag='maincanv')
        elif mode == 'shadow':
            obj = self.getAttrByName('shadow')
            self.can.create_image(obj[1], obj[2], image=obj[3],
                                  anchor=NW, tag='maincanv')
        else:
            #	obj = self.getAttrByName('frontscreen')
            self.drawWin('maincanv', 'toolbar')

    def getAttrByName(self, name):
        '''Получить объект из settings, по его имени в строковом виде'''
        obj = 'self.settings.%s' % name
        obj = eval(obj)
        return obj

    def getCurUsr(self):
        curUsr = self.operator.authWin.currentUser
        return curUsr

    def update_window(self):
        self.blockwin.destroy()
        self.operator.open_main()

    #def draw_blur(self):
    #    from ctypes import windll
    #    from BlurWindow.blurWindow import blur
    #    hWnd = windll.user32.GetForegroundWindow()
    #    blur(hWnd)

    def initBlockImg(self, name, btnsname, slice='shadow', mode='new',
                     seconds=[], hide_widgets=[], picture=None, **kwargs):

        if self.blockImgDrawn:
            return
        self.blockImgDrawn = True
        self.can.delete('clockel')
        self.drawBlurScreen()
        self.can.delete(self.settings.exit_gate, self.settings.entry_gate,
                        'statusel', 'car_icon')
        if picture:
            threading.Thread(target=self.operator.draw_auto_exit_pic,
                             args=(picture,)).start()
        self.drawBlockImg(name=name)
        addBtns = self.getAttrByName(btnsname)
        self.buttons_creation(buttons=addBtns, tagname='tempBtn')
        self.hiden_widgets = self.hiden_widgets + hide_widgets + self.created_buttons
        try:
            self.hiden_widgets += self.operator.toolbar_btns
        except:
            pass
        try:
            self.hiden_widgets.append(self.usersComboBox)
            self.hiden_widgets.append(self.loginEntry)
        except:
            pass
        self.hide_widgets(self.hiden_widgets)
        try:
            self.tree.lower()
        except:
            print(format_exc())
        self.operator.turn_cams(False)
        self.abort_round_btn.lower()

    def hide_zoomed_cam(self, root_calback=False):
        for cam in self.operator.cameras_info:
            if cam['enable'] and self.operator.get_cam_cm_enable(cam):
                cam["video_worker_inst"].hide_callback(
                    root_calback=root_calback)
                cam['zoomed'] = False

    def cam_zoom_callback(self, cam_type=None):
        # self.can.delete('tree')
        if self.operator.current == 'MainPage':
            self.operator.currentPage.tree.lower()
        self.cam_zoom = True
        self.operator.currentPage.abort_round_btn.lower()
        for cam in self.operator.cameras_info:
            if cam['type'] == cam_type:
                cam['zoomed'] = True
            else:
                self.operator.turn_cams(False, cam['type'])

    def cam_hide_callback(self, cam_type=None):
        self.cam_zoom = False
        #if self.operator.current == 'MainPage':
        #    self.operator.currentPage.abort_round_btn.lift()
        #    self.operator.currentPage.tree.lift()
        #    for cam in self.operator.cameras_info:
       #         if cam['type'] == cam_type:
        #            cam['zoomed'] = False
        #        else:
        #            self.operator.turn_cams(True, cam['type'])

    def drawBlockImg(self, name, master='def'):
        image = self.getAttrByName(name)
        if master == 'def':
            master = self.can
        master.create_image(image[1], image[2], image=image[3], tag='blockimg')

    def drawBlurScreen(self):
        '''Рисует заблюренный фон'''
        screenshot = pyautogui.screenshot()
        screenshot = screenshot.filter(ImageFilter.BLUR)
        mask = ImageTk.PhotoImage(screenshot)
        self.bluredScreen = self.can.create_image(self.screenmiddle,
                                                  image=mask,
                                                  tags=('blurScreen',))
        self.blurDrawn = mask

    def destroyBlockImg(self, mode='total'):
        self.can.delete('blockimg', 'shadow', 'errorbackground', 'tempBtn')
        self.show_widgets()
        self.unbindORUP()
        self.operator.escape_button_operator()
        try:
            self.tree.lift()
            self.can.itemconfigure(self.bluredScreen, state='hidden')
        except:
            pass
        self.can.delete('blurScreen')
        self.hiden_widgets = []
        if self.operator.current == 'MainPage' or self.operator.current == 'ManualGateControl':
            self.draw_gate_arrows()
        if mode != 'block_flag_fix':
            self.blockImgDrawn = False
        self.show_time()
        self.operator.statPage.place_amount_info(
            self.operator.statPage.weight_sum,
            self.operator.statPage.records_amount,
            tag='amount_info')
        self.abort_round_btn.lift()
        if self.operator.current == 'MainPage':
            self.operator.draw_road_anim()
            if not self.cam_zoom:
                self.operator.turn_cams(True)
        self.weight_too_little = False

    def create_main_buttons(self):
        self.operator.toolbar_btns = self.buttons_creation(
            buttons=self.settings.toolBarBtns, tagname='btn')

    def buttons_creation(self, buttons='def', tagname='btn'):
        ''' Функция создания кнопок'''
        self.can.delete(tagname)
        all_buttons = []
        if tagname == 'winBtn':
            self.created_buttons = []
        if buttons == 'def':
            buttons = self.buttons
            if self.name != 'AuthWin':
                buttons += [self.settings.exitBtn, self.settings.lockBtn,
                            self.settings.minimize_btn]
        for obj in buttons:
            button = self.get_create_btn(obj)
            self.can.create_window(obj[1], obj[2], window=button, tag=tagname)
            if tagname == 'winBtn':
                self.created_buttons.append(button)
            all_buttons.append(button)
        return all_buttons

    def minimize_window(self):
        """ Свернуть программу """
        self.root.wm_state('iconic')

    def get_create_btn(self, obj):
        button = ttk.Button(self.root, command=lambda image=obj, self=self,
                                                      operator=self.operator: eval(
            obj[3]),
                            padding='0 0 0 0', takefocus=False)
        button['cursor'] = 'hand2'
        button['image'] = obj[4]
        button.bind("<Enter>", lambda event, button=button,
                                      image=obj: self.btn_enter(button, image))
        button.bind("<Leave>", lambda event, button=button,
                                      image=obj: self.btn_leave(button, image))
        button['width'] = 0
        if obj[0].strip() == 'notifUs':
            self.notif_btn = button
        try:
            button['style'] = obj[7]
        except:
            pass
        return button

    def btn_enter(self, button, image):
        try:
            button['image'] = image[8]
        except:
            pass

    def btn_leave(self, button, image):
        try:
            button['image'] = image[4]
        except:
            pass

    def getDaysBetween(self, end, numdays):
        date_list = [end - datetime.timedelta(days=x) for x in range(numdays)]
        return date_list

    def start_clock(self):
        thread = threading.Thread(target=self.show_time_cycle, args=(),
                                  daemon=True)
        thread.start()

    def show_time_cycle(self):
        olddate = datetime.datetime(1997, 8, 24)
        while True:
            date = datetime.datetime.now()
            diff = (date - olddate).total_seconds()
            if self.operator.current != 'AuthWin' and diff > 59 and self.operator.currentPage.blockImgDrawn == False:
                olddate = self.show_time()
                time.sleep(1)
            else:
                # print('Не удалось нарисовать время, diff', diff)
                time.sleep(3)

    def show_time(self):
        date = datetime.datetime.now()
        datestr = date.strftime('%d %b')
        timestr = date.strftime('%H:%M')
        self.can.delete('clockel')
        if self.operator.currentPage.blockImgDrawn == False:
            self.can.create_text(self.settings.w / 18.841379310344827,
                                 self.h / 10.971428571428572,
                                 text=datestr, font=fonts.time_font,
                                 fill=self.textcolor, tag='clockel',
                                 justify='center')
            self.can.create_text(self.settings.w / 19.514285714285716,
                                 self.h / 7.68,
                                 text=timestr, font=fonts.date_font,
                                 fill=self.textcolor, tag='clockel',
                                 justify='center')
            olddate = date
        else:
            print('not false', self.operator.currentPage.blockImgDrawn)
            olddate = date
        return olddate

    def format_mainscreens(self):
        settings = self.settings
        self.format_image(settings.mainscreenpath, settings.screensize)
        self.format_image(settings.dwnldbgpath, (int(self.w / 2.56),
                                                 int(self.h / 4.267)))
        for image in glob(self.settings.slideanimpath + '\\*'):
            self.format_image(image, settings.screensize)

    def checking_thread(self):
        '''Проверяет сосотяние весов каждую секунду и отрисовывает при наличии обновлений'''
        while True:
            if ((self.operator.current == 'MainPage' or self.operator.current == 'ManualGateControl') and not
                self.operator.currentPage.blockImgDrawn and self.operator.if_show_weight):
                self.can.delete('kgel')
                self.draw_weight(weight=self.get_new_weight())
                time.sleep(0.5)
            try:
                if self.operator.currentPage.trail_win_drawn:
                    self.can.delete('kgel')
                    self.draw_weight(pos=(self.w/2, self.h/2+20),
                                     font=fonts.weight_body_font)
                    time.sleep(0.5)
                elif self.operator.currentPage.weight_too_little:
                    self.can.delete('kgel')
                    self.draw_weight(pos=(self.w/2-67, self.h/2-157),
                                     font=fonts.weight_too_little_font)
                    time.sleep(0.5)
            except AttributeError:
                pass
            time.sleep(0.1)

    def get_new_weight(self):
        weight = self.operator.wr.weigth
        new_state = weight + ' кг'
        return new_state

    # print('not equal!')
    # print('here')
    # else: pass

    def drawing(self, canimg='backscreen'):
        ''' Родовая функция заполнения экрана (кнопки,холст,фокусировка)
		Кнопки уникальны для каждого окна, и должны быть предопределены'''
        self.can.delete('maincanv', 'tree', 'picker', 'tempBtn')

    def bindArrows(self):
        if not self.settings.mirrored:
            left_button = self.operator.currentPage.orupActExit
            right_button = self.operator.currentPage.orupAct
        else:
            left_button = self.operator.currentPage.orupAct
            right_button = self.operator.currentPage.orupActExit
        self.root.bind('<Left>', lambda event: left_button())
        self.root.bind('<Right>', lambda event: right_button())

    def unbindArrows(self):
        self.root.unbind('<Left>')
        self.root.unbind('<Right>')

    def drawWin(self, tag='win', *names):
        for arg in names:
            obj = self.getAttrByName(arg)
            self.can.create_image(obj[1], obj[2], image=obj[3], tag=tag)

    def drawObj(self, *names):
        for arg in names:
            obj = self.getAttrByName(arg)
            self.can.create_window(obj[0], obj[1], window=obj[2])

    def drawToolbar(self):
        objects = [self.settings.toolbar]
        for obj in objects:
            self.can.create_image(obj[1], obj[2], image=obj[3], tag='toolbar')

    def format_image(self, imagepath, size):
        imgobj = Image.open(imagepath).resize(size, Image.ANTIALIAS)
        imgobj.save(imagepath)

    def draw_block_win(self, name):
        self.operator.current = name
        if name == 'chatwin':
            xsize = self.settings.bwS
            ysize = self.settings.bhS
            buttons = self.settings.chatBtns
        self.blockwin = Canvas(self.root, highlightthickness=0)
        img = self.settings.chatwin
        self.blockwin.create_image(img[1], img[2], image=img[3])
        self.blockwin.config(width=xsize, height=ysize)
        self.can.create_window(self.screenmiddle, window=self.blockwin)

    def draw_weight(self, pos=None, weight=None, font=None):
        """ Рисует вес """
        if not pos:
            pos = self.settings.weight_show_posses
        if not weight:
            weight = self.get_new_weight()
        if not font:
            font = fonts.weight_font
        self.can.create_text(pos,
                             font=font, text=weight,
                             fill='#BABABA',
                             tags=('statusel', 'kgel'))
        return weight

    def openWin(self):
        self.can.delete('winBtn')
        self.operator.open_new_page(self)
        self.blurDrawn = False
        self.win_widgets = []
        self.drawing()
        self.draw_picker()
        self.can.tag_raise('clockel')
        self.operator.get_gcore_health_monitor()
        self.operator.ar_qdk.catch_window_switch(self.operator.current)

    def draw_picker(self, ):
        self.can.delete('picker')
        try:
            self.can.create_image(self.btn_name[1], self.btn_name[2],
                                  image=self.settings.picker, tag='picker')
        except AttributeError:
            pass

    def getEntry(self, w=30, h=1, bg='#272727', fill='#BABABA'):
        var = StringVar(self.root)
        newEntry = Entry(self.root, bd=0, width=w, textvariable=var, bg=bg,
                         fg=fill, font=fonts.general_entry_font,
                         disabledbackground=bg, disabledforeground=fill,
                         highlightthickness=0)
        return newEntry

    def getText(self, w=50, h=5, bg='#272727', fill='#BABABA',
                font=fonts.orup_font, *args, **kwargs):
        newText = Text(self.root, bd=0, width=w, height=h, bg=bg, fg=fill,
                       font=fonts.general_text_font)
        return newText

    def getOptionMenu(self, deff, listname, w=30, h=0, bg='#272727',
                      fg='#BABABA',
                      varname='self.deffValue', mode='deff', tracecomm='',
                      font=fonts.general_optionmenu_font):
        com1 = '{} = StringVar(self.root)'.format(varname)
        com2 = '{}.set(deff)'.format(varname)
        exec(com1)
        exec(com2)
        option_menu = OptionMenu(self.root, eval(varname), *listname)
        option_menu.config(indicatoron=0, font=font, bg=bg, width=w,
                           height=h, fg=fg, highlightthickness=0,
                           highlightbackground='blue', highlightcolor='red',
                           anchor='nw', relief='flat')
        option_menu['borderwidth'] = 0
        option_menu["highlightthickness"] = 0
        option_menu["menu"].config(bg='#3D3D3D', fg='#E2E2E2',
                                   activebackground=cs.orup_active_color,
                                   font=fonts.orup_font, relief='flat',
                                   borderwidth=0)
        option_menu['menu']['borderwidth'] = 0
        if mode == 'trace':
            self.chosenTrashCat = eval(varname).get()
            eval(varname).trace("w", tracecomm)
        return option_menu

    def big_orup_exit(self, carnum='', carrier='Физлицо', trash_type='Прочее',
                      trash_cat='Прочее', call_method='manual',
                      car_protocol='NEG', course='OUT'):
        # Создает большой ОРУП при нажатии на кнопку на малой ОРУП
        self.destroyORUP(mode='total')
        self.orupAct(carnum, carrier, trash_type, trash_cat, call_method,
                     car_protocol, course=course)

    def set_window_normal(self, state='zoomed', **kwargs):
        if self.root.wm_state() == 'iconic':
            self.root.wm_state(state)

    def orupAct(self, carnum='', contragent='Физлицо', trashType='Прочее',
                trashCat='ПО', call_method='manual', client='Физлицо',
                car_protocol='tails', course='IN', polygon=None, source=None,
                pol_object=None, last_tare=None,
                car_read_client_id=None):
        self.car_detected_source = source
        self.orup_imgs = []
        if self.operator.fgsm:
            self.operator.if_show_weight = False
        self.hide_zoomed_cam()
        if course == 'IN':
            gate_name = 'entry'
        else:
            gate_name = 'exit'
        if self.operator.fgsm:
            self.fgsm_gate_open = gate_name
            self.operator.ar_qdk.operate_gate_manual_control(
                operation='open',
                gate_name=gate_name,
                smart_auto_close=True)
        self.operator.get_gcore_status()
        self.set_window_normal()
        # self.can.delete('clockel')
        self.orupState = True
        self.carnum_was = carnum
        self.initBlockImg('orupWinUs', 'orupEnterBtns')
        self.car_course = course
        self.posEntrys(carnum, trashType, trashCat, contragent,
                       call_method=call_method,
                       polygon=polygon, client=client, object=pol_object,
                       last_tare=last_tare,
                       car_read_client_id=car_read_client_id)
        if carnum and call_method == "auto" and source == 'rfid':
            self.carnum['state'] = 'disabled'
        self.turn_on_request_last_event()
        self.root.bind('<Return>', lambda event: self.initOrupAct())
        self.root.bind('<Escape>',
                       lambda event: self.destroyORUP(mode="decline"))
        self.root.bind("<Double-Button-1>",
                       lambda event: self.clear_optionmenu(event))
        self.root.bind("<Button-1>",
                       lambda event: self.select_optionmenu(event))
        self.unbindArrows()
        if course == 'IN':
            self.operator.turn_cams(True, 'cad_gross')
        else:
            self.operator.turn_cams(True, 'auto_exit')
        self.operator.ar_qdk.execute_method('capture_orup_opened',
                                            orup_name="Брутто")

    def orupActExit(self, carnum='deff', call_method="manual", course='OUT',
                    with_pic=False):
        self.hide_zoomed_cam()
        #self.destroyORUP(mode='total')
        self.operator.get_gcore_status()
        self.carnum_was = carnum
        self.set_window_normal()
        self.can.delete('clockel')
        self.course = course
        self.car_course = course
        self.exCarIndex = 0
        self.orupState = True
        if with_pic:
            self.initBlockImg(name='orupWinExAE', btnsname='orupExitBtnsAE',
                              picture=with_pic)
        else:
            self.initBlockImg(name='orupWinEx', btnsname='orupExitBtns')
        self.posExitInt(carnum, call_method, with_pic=with_pic)
        self.root.bind('<Return>', lambda event: self.launchExitProtocol())
        self.root.bind('<Escape>',
                       lambda event: self.destroyORUP(mode="decline"))
        self.root.bind('<Up>', lambda event: self.arrowUp())
        self.root.bind('<Down>', lambda event: self.arrowDown())
        self.unbindArrows()
        self.operator.turn_cams(True, 'auto_exit')
        self.operator.ar_qdk.execute_method('capture_orup_opened',
                                            orup_name="Тара")

    def arrowDown(self):
        if self.exCarIndex < len(self.exCarNums) - 1:
            self.exCarIndex = + 1
        else:
            self.exCarIndex = 0
        self.carNumVar.set(self.exCarNums[self.exCarIndex])

    def arrowUp(self):
        if self.exCarIndex > 0:
            self.exCarIndex = self.exCarIndex - 1
        else:
            self.exCarIndex = len(self.exCarNums) - 1

        self.carNumVar.set(self.exCarNums[self.exCarIndex])

    def posExitInt(self, car_num, callback_method, spec_protocols='exit',
                   with_pic=None):
        # Разместить виджеты на выездном ОРУП
        self.car_choose_mode = callback_method
        self.full_car_info = self.get_cars_inside_full_info()
        self.exCarNums = [car['car_number'] for car in self.full_car_info]
        self.carNumVar = StringVar()
        height = self.h / 2.320
        if with_pic:
            height = self.h / 1.372
        if self.exCarNums != None and len(self.exCarNums):
            self.escOrupOpt = self.getOptionMenu(deff=self.exCarNums[0],
                                                 listname=self.exCarNums,
                                                 w=el_sizes.option_menus[
                                                     'choose_car'][
                                                     self.screensize]['width'],
                                                 bg=cs.orup_bg_color,
                                                 varname='self.carNumVar',
                                                 mode='trace',
                                                 tracecomm=self.orup_tare_set_no_exit)
            if with_pic:
                for car_num in self.exCarNums:
                    if car_num[0].isdigit():
                        self.carNumVar.set(car_num)
            self.can.create_window(self.w / 1.85, height,
                                   window=self.escOrupOpt, tag='orupentry')
        if callback_method == 'auto' and not with_pic:
            self.escOrupOpt = self.getOptionMenu(deff=car_num,
                                                 listname=[car_num, ],
                                                 w=el_sizes.option_menus[
                                                     'choose_car'][
                                                     self.screensize]['width'],
                                                 bg=cs.orup_bg_color,
                                                 varname='self.carNumVar')
            self.carNumVar.set(car_num)
            self.escOrupOpt['state'] = 'disabled'
            self.can.create_window(self.w / 1.85, height,
                                   window=self.escOrupOpt, tag='orupentry')
        self.commEx = self.getText(h=1,
                                   w=el_sizes.text_boxes['orup_exit_comm'][
                                       self.screensize]['width'],
                                   bg=cs.orup_bg_color, font=fonts.orup_font)
        height = self.h / 2.025
        if with_pic:
            height = self.h / 1.272
        self.can.create_window(self.w / 1.795, height,
                               window=self.commEx,
                               tag='orupentry')
        self.pos_orup_protocols(spec_protocols, with_pic=with_pic)
        self.orup_tare_set_no_exit()

    def orup_tare_set_no_exit(self, *args, **kwargs):
        car_number = self.carNumVar.get()
        for car in self.full_car_info:
            if car['car_number'] == car_number:
                no_exit = car['no_exit']
                try:
                    self.commEx.delete('1.0', END)
                    self.commEx.insert(1.0, car['full_notes'])
                    self.no_exit_var.set(no_exit)
                except:
                    self.no_exit_var.set(0)
                    print(format_exc())

    def get_cars_inside(self):
        return [car['car_number'] for car in self.operator.unfinished_records
                if not car['time_out']]

    def get_cars_inside_full_info(self):
        return [car for car in self.operator.unfinished_records
                if not car['time_out']]

    def launchExitProtocol(self, mode='redbgEx'):
        self.operator.get_gcore_status()
        carnum = self.carNumVar.get()
        data_dict = {}
        data_dict['ar_status'] = self.operator.gcore_status
        data_dict['car_number'] = carnum
        data_dict['have_rfid'] = self.check_car_rfid(carnum)
        data_dict['weight_data'] = int(self.operator.wr.weigth)
        data_dict['photo_object'] = self.settings.redbgEx[3]
        data_dict['car_protocol'] = self.operator.fetch_car_protocol(carnum)
        data_dict['course'] = self.course
        data_dict['have_brutto'] = self.operator.fetch_if_record_init(carnum)
        data_dict['choose_mode'] = self.car_choose_mode
        data_dict['photo_object'] = self.settings.redbgEx[3]
        data_dict['comment'] = self.commEx.get("1.0", 'end-1c')
        if not self.escOrupOpt:
            return
        response = self.operator.orup_error_manager.check_orup_errors(
            orup='tara',
            xpos=self.settings.redbgEx[1],
            ypos=self.settings.redbgEx[2],
            **data_dict)
        if not response:
            self.start_car_protocol(orup_mode=self.settings.orup_exit_comm)

    def start_car_protocol(self, orup_mode, carnum=None):
        self.operator.status_ready = False
        info = self.get_entrys_info(orup_mode)
        if self.car_course != None:
            info['course'] = self.car_course
        if carnum != None:
            info['carnum'] = carnum
        self.operator.ar_qdk.start_car_protocol(info)
        self.operator.ar_qdk.catch_orup_accept(car_number=info['carnum'])
        self.operator.orup_blacklist_del(car_num=info['carnum'])
        self.destroyORUP(mode='total')

    def get_entrys_info(self, orup):
        # Получить данные из полей ввода ОРУП (въезд или выезд определяется по перменной orup)
        if orup == self.settings.orup_enter_comm:
            info = self.get_orup_entry_ids()
        else:
            info = self.get_ex_entrys_info()
        info['car_choose_mode'] = self.car_choose_mode
        try:
            info['no_exit'] = bool(self.no_exit_var.get())
        except:
            info['no_exit'] = False
        try:
            info['auto_tare'] = self.last_tare_var.get()
        except:
            info['auto_tare'] = False
        info['orup_mode'] = orup
        return info

    def get_orup_entry_ids(self):
        # Получить ID тех данных, что представлены были в ОРУП
        info = self.get_orup_entry_reprs()  # Сначала полные имена
        # Потом начинаем преоброзовывать, вставляя их ID
        info['carrier'] = self.operator.get_client_id(info['carrier'])
        info['trash_cat'] = self.operator.get_trash_cat_id(info['trash_cat'])
        info['trash_type'] = self.operator.get_trash_type_id(
            info['trash_type'])
        info['source'] = self.car_detected_source
        info['operator'] = self.operator.get_user_id(info['operator'])
        info['polygon_platform'] = self.operator.get_polygon_platform_id(
            info['polygon_platform'])
        info['trailer'] = self.trailer_var.get()
        info['client'] = self.operator.get_client_id(info['client'])
        info['polygon_object'] = self.operator.get_polygon_object_id(
            info['polygon_object'])
        return info

    def get_orup_entry_reprs(self):
        """ Получить данные из полей ввода въездного оруп"""
        info = {}
        info['carnum'] = self.carnum.get()
        info['carrier'] = self.contragentCombo.get()
        info['client'] = self.clientOm.get()
        info['trash_cat'] = self.trashCatOm.get()
        info['trash_type'] = self.trashTypeOm.get()
        info['operator'] = self.operator.authWin.currentUser
        info['polygon_platform'] = self.platform_choose_var.get()
        info['polygon_object'] = self.objectOm.get()
        info['comm'] = self.comm.get("1.0", 'end-1c')
        info['course'] = 'IN'
        info['carnum_was'] = self.carnum_was
        return info

    def get_ex_entrys_info(self):
        # Получить данные из всех полей ввода выездного ОРУП
        info = {}
        info['course'] = 'OUT'
        info['carnum'] = self.carNumVar.get()
        info['comm'] = self.commEx.get("1.0", 'end-1c')
        return info

    def turn_on_request_last_event(self):
        """ Включить запрос данных о последнем заезде машины, если вбили гос.номер """
        self.orupCarNumVar.trace_add('write', self.car_number_change_reaction)
        # Привязать функцию реакции софта на ввод гос. номера
        vcmd = self.root.register(self.carnumCallback)
        self.carnum.validatecommand = (vcmd, '%P')

    def client_change_reaction(self, *args):
        client_id = self.operator.get_client_id(self.clientOm.get())
        if client_id:
            self.get_contragent_seal(client_id, contragent_type='client')

    def carrier_change_reaction(self, *args):
        client_id = self.operator.get_client_id(self.orup_carrier_var.get())
        if client_id:
            self.get_contragent_seal(client_id, contragent_type='carrier')

    def get_contragent_seal(self, client_id, contragent_type):
        self.operator.ar_qdk.execute_method('get_client_seal_pic',
                                            client_id=client_id,
                                            contragent_type=contragent_type)

    def car_number_change_reaction(self, *args):
        # Функция реакции программы на совершение действий типа write в combobox для ввода гос.номера
        carnum = self.orupCarNumVar.get()
        value = len(carnum)
        self.orupCarNumVar.set(carnum.upper())
        if value < 8:
            # Сделать красную обводку
            self.carnum['style'] = 'orupIncorrect.TCombobox'
        else:
            # Оставить обычное оформление
            self.carnum['style'] = 'orup.TCombobox'
        if value >= 8:  # and carnum != self.sent_car_number:
            # Если длина гос. номер корректная, и запрос get_last_event по этому номеру еще не отправлялся - отправить
            self.operator.ar_qdk.get_last_event(
                auto_id=self.operator.get_auto_id(carnum))
            self.sent_car_number = carnum

    def create_danger_text(self, text):
        self.can.delete('danger_text')
        self.can.create_text(self.w / 2,
                             self.h / 20,
                             text=text,
                             fill='white',
                             font=fonts.loading_status_font,
                             tags=('danger_text',))

    def check_gcore_health(self, health_monitor, *args, **kwargs):
        """ Проверяет health_monitor, представляющий из себя словарь вида
        {'Состояние камеры': {'status':False, 'info': 'Обрыв связи'}, 'ФТП': {'status':True, 'info': 'Все в порядке'}},
        Если встречает status=False, меняет иконку окна нотификаций на красную. Если же все хорошо - на обычную."""
        incorrect = self.if_incorrect_status(health_monitor)
        if incorrect:
            self.set_notif_alert()
        else:
            self.unset_notif_alert()
        if not health_monitor['Контроллер СКУД']['status']:
            self.create_danger_text(
                'СКУД НЕ ДОСТУПЕН! ПОЗВОНИТЕ В ТЕХНИЧЕСКУЮ ПОДДЕРЖКУ!', )

    def if_incorrect_status(self, health_monitor, *args, **kwargs):
        """ Перебирает все элементы системы и чекает их статус. Возвращает True, если хотя бы один элемент не работает
        """
        status = [info['status'] for info in list(health_monitor.values())]
        if False in status:
            return True

    def set_notif_alert(self):
        """ Сделать иконку окна нотификаций красной (что-то не так в health_monitor)
        """
        try:
            self.settings.toolBarBtns.append(self.settings.notifIconAlert)
            self.settings.toolBarBtns.remove(self.settings.notifBtn)
        except:
            print(traceback.format_exc())
            pass

    def unset_notif_alert(self):
        """ Сделать иконку окна нотификаций красной (что-то не так в health_monitor)
        """
        try:
            self.settings.toolBarBtns.append(self.settings.notifBtn)
            self.settings.toolBarBtns.remove(self.settings.notifIconAlert)
        except:
            print(traceback.format_exc())
            pass

    def posEntrys(self, carnum, trashtype, trashcat, contragent='', client='',
                  notes='', object='',
                  spec_protocols='entry', call_method='auto',
                  polygon=None, last_tare=None, car_read_client_id=None):
        self.car_choose_mode = call_method
        # Вставить поля для выбора перевозчика, ввода гос.номера, выбора кат. груза и вида груза, и ввода комментария
        self.create_orup_carrier()
        self.create_orup_carnum(carnum)
        #self.entry_set_value(self.carnum, carnum)
        self.create_orup_tc()
        self.create_orup_tt()
        self.create_orup_object()
        self.create_orup_client()
        self.create_orup_platform_choose(polygon)
        self.posObjects()
        self.create_orup_comm(notes)
        # Попробовать вставить в поля переданные данные, если не получится - вставить маску
        self.try_set_attr_all(trashcat, trashtype, contragent, client, object, carnum)
        if car_read_client_id:
            client_name = self.operator.get_client_repr(car_read_client_id)
            self.clientOm.set(client_name)
            self.clientOm.configure(state='disable')
        # Заблокировать поля на редактирование, если есть необходимость
        # self.block_entrys(car_protocol, trashcat, trashtype, contragent)
        # Вставить чек-боксы для выбора "Длинномер|Поломка", если есть необходимость
        self.pos_orup_protocols(spec_protocols)
        if spec_protocols:
            self.pos_trailer()
            self.pos_last_tare(not last_tare and call_method == 'auto')

    def create_orup_comm(self, notes):
        self.comm = self.getText(h=1, w=
        el_sizes.text_boxes['orup_entry_comm'][self.screensize]['width'],
                                 bg=cs.orup_bg_color, font=fonts.orup_font)
        self.comm.insert(1.0, notes)
        self.can.create_window(self.w / 1.78, self.h / 1.5, window=self.comm,
                               tag='orupentry')

    def create_orup_carrier(self):
        # Создать комбобокс на въездном ОРУП для ввода названия перевозчика
        self.orup_carrier_var = StringVar()
        self.contragentCombo = self.create_orup_combobox(
            self.w / 1.78, self.h / 2.7, textvariable=self.orup_carrier_var)
        self.orup_carrier_var.trace_add('write', self.carrier_change_reaction)
        self.contragentCombo.set_completion_list(
            self.operator.get_clients_reprs())

    def create_orup_platform_choose(self, polygon):
        # Создать комбобокс на въездном ОРУП для ввода названия организации, принимающей груз
        polygon_platforms = self.operator.get_polygon_platforms_reprs()  # Получить repr значнеия организаций
        self.platform_choose_var = StringVar()
        self.platform_choose_combo = self.create_orup_combobox(self.w / 1.78,
                                                               self.h / 2.33,
                                                               textvariable=self.platform_choose_var)
        self.platform_choose_combo.set_completion_list(polygon_platforms)
        if polygon == None:
            self.platform_choose_combo.set(polygon_platforms[0])
        else:
            self.platform_choose_combo.set(polygon)
        self.platform_choose_var.trace_add('write', self.posObjects)

    def create_orup_tt(self):
        # Создать комбобокс на въездном ОРУП для ввода вида груза (trash type)
        self.trashTypeOm = self.create_orup_combobox(self.w / 1.78,
                                                     self.h / 1.65,
                                                     tags=('orupentry',
                                                           'trashTypeOm',))
        self.trashTypeOm.set('Выберите вид груза')

    def create_orup_object(self):
        # Создать комбобокс на въездном ОРУП для ввода вида груза (trash type)
        self.objectOm = self.create_orup_combobox(self.w / 1.78,
                                                  self.h / 2.05,
                                                  tags=('orupentry',
                                                        'objectOm',))
        self.objectOm.set('Выберите объект')

    def create_orup_client(self, default='Выберит клиента (плательщика)'):
        self.orup_client_var = StringVar()
        self.orup_client_var.trace_add('write', self.client_change_reaction)
        self.clientOm = self.create_orup_combobox(self.w / 1.78, self.h / 3.2,
                                                  tags=('orupentry',
                                                        'clientOm',),
                                                  textvariable=self.orup_client_var)
        self.clientOm.set_completion_list(
            self.operator.get_clients_reprs())
        self.clientOm.set(default)

    def create_orup_combobox(self, xpos, ypos, width=29, height=3,
                             tags=('orupentry',), *args, **kwargs):
        # Универсальный конструктор для создания полей на въездном ОРУП
        some_cb = self.create_combobox(self.root, xpos, ypos, tags=tags,
                                       width=
                                       el_sizes.comboboxes['orup.general'][
                                           self.screensize]['width'],
                                       height=
                                       el_sizes.comboboxes['orup.general'][
                                           self.screensize]['height'],
                                       foreground=cs.orup_fg_color,
                                       font=fonts.orup_font, *args, **kwargs)
        self.configure_combobox(some_cb)
        return some_cb

    def create_combobox(self, root, xpos, ypos, tags, combo_car_number=None,
                        *args, **kwargs):
        # Универсальный конструктор создания и размещения всяких Combobox
        if combo_car_number:
            some_cb = AutocompleteComboboxCarNumber(root)
        else:
            some_cb = AutocompleteCombobox(root)
        some_cb.config(*args, **kwargs)
        self.can.create_window(xpos, ypos, window=some_cb, tag=tags)
        return some_cb

    def create_orup_carnum(self, request_last_event=False):
        # Создать комбобокс на въездном ОРУП для ввода гос. номера
        self.orupCarNumVar = StringVar()
        self.carnum = self.create_orup_combobox(self.w / 1.78, self.h / 3.88,
                                                validate='all',
                                                textvariable=self.orupCarNumVar,
                                                combo_car_number=True)
        self.carnum.set_completion_list(self.operator.get_auto_reprs())

    def create_orup_tc(self):
        # Создать комбобокс на въездном ОРУП для выбора категории груза
        self.trashCatVar = StringVar()
        self.trashCatOm = self.create_orup_combobox(self.w / 1.78,
                                                    self.h / 1.825,
                                                    textvariable=self.trashCatVar)
        self.trashCatVar.trace_add('write', self.posTrashTypes)
        self.trashCatOm.set_completion_list(
            self.operator.get_trash_cats_reprs())

    def posTrashTypes(self, a='a', b='b', c='c', d='d', e='e'):
        self.chosenTrashCat = self.trashCatOm.get()
        if self.chosenTrashCat == '':
            trashtypes = ['Выберите вид груза', ]
        else:
            try:
                trashtypes = self.operator.trash_cat_type_map[self.chosenTrashCat].copy()
            except KeyError:
                trashtypes = []
            try:
                trashtypes += self.operator.trash_cat_type_map[None]
            except KeyError:
                pass
        self.trashTypeOm.set_completion_list(trashtypes)
        if self.chosenTrashCat.strip() == 'ТКО':
            self.trashTypeOm.set('4 класс')
            self.trash_cat_tko_react()
        else:
            self.contragentCombo.set_completion_list(
                self.operator.get_clients_reprs())
            self.clientOm.set_completion_list(
                self.operator.get_clients_reprs())
            self.trashTypeOm.set('Прочее')
        try:
            if self.chosenTrashCat.strip() in ('Прочее', 'ПО'):
                self.last_tare_check.configure(state='normal')
            else:
                self.last_tare_check.configure(state='disabled')
                self.last_tare_var.set(0)
        except AttributeError:
            pass

    def trash_cat_tko_react(self):
        """ Реакция на выбор ТКО """
        client = self.orup_client_var.get()
        carrier = self.orup_carrier_var.get()
        print(self.operator.region_operators, self.operator.tko_carriers)
        # Проверяем, выбранный перевозчик - перевозчик ТКО?
        self.clientOm.set_completion_list(self.operator.region_operators)
        self.contragentCombo.set_completion_list(self.operator.tko_carriers)
        try:
            if not self.check_client_attribute(client, "region_operator"):
                if len(self.operator.region_operators) == 1:
                    self.orup_client_var.set(self.operator.region_operators[0])
                else:
                    self.orup_client_var.set("Выберите регионального оператора")
        except KeyError:
            if len(self.operator.region_operators) == 1:
                self.orup_client_var.set(self.operator.tko_carriers[0])
            else:
                self.orup_client_var.set("Выберите регионального оператора")
        # Проверяем, выбранный клиент - РО?
        try:
            if not self.check_client_attribute(carrier, "tko_carrier"):
                self.orup_carrier_var.set("Выберите ТКО перевозчика")
        except KeyError:
            self.orup_carrier_var.set("Выберите ТКО перевозчика")

    def check_client_attribute(self, client, attribute):
        if self.operator.general_tables_dict['clients'][client][attribute]:
            return self.operator.general_tables_dict['clients'][client]

    def posObjects(self, a='a', b='b', c='c', d='d', e='e'):
        self.chosenPlatform = self.platform_choose_var.get()
        if self.chosenPlatform == '':
            objects = ['Выберите объект размещения', ]
        else:
            try:
                objects = db_functions.get_trashtypes_by_trashcat_repr(
                    self.operator.general_tables_dict,
                    'pol_objects',
                    'duo_pol_owners', self.chosenPlatform,
                    map_table='platform_pol_objects_mapping',
                    map_cat_column='platform_id',
                    map_type_column='object_id')
            except KeyError:
                objects = []
        self.objectOm.set_completion_list(objects)
        try:
            self.objectOm.set(objects[0])
        except:
            self.objectOm.set('Выберите объект размещения')

    def try_set_attr_all(self, trashcat, trashtype, carrier, client, object, carnum):
        # Попытка вставить данные, переданные в ОРУП в соответствующие окна, если не получится, вставляется сообщение
        # ошибки
        if carnum:
            self.carnum.set(carnum)
        self.try_set_attr(self.trashCatOm, trashcat,
                          self.operator.get_trash_cats_reprs(),
                          'Выберите категорию груза')
        self.try_set_attr(self.trashTypeOm, trashtype,
                          self.operator.get_trash_types_reprs(),
                          'Выберите вид груза')
        self.try_set_attr(self.contragentCombo, carrier,
                          self.operator.get_clients_reprs(),
                          'Выберите перевозчика')
        self.try_set_attr(self.clientOm, client,
                          self.operator.get_clients_reprs(),
                          'Выберите клиента (плательщика)')
        self.try_set_attr(self.objectOm, object,
                          self.operator.get_table_reprs('pol_objects'),
                          'Выберите объект размещения')

    def block_entry_set_value(self, entry, value):
        # Вставляет в поле значение по умолчанию и запрещает редактирование
        self.entry_set_value(entry, value)
        entry['state'] = 'disabled'

    def entry_set_value(self, entry, value):
        entry.delete(0, END)
        if value:
            entry.insert(0, value)

    def pos_orup_protocols(self, mode, with_pic=None):
        if mode:
            self.no_exit_var = IntVar(value=0)
            self.no_exit_var_check = ttk.Checkbutton(variable=self.no_exit_var)
            self.no_exit_var_check['style'] = 'check_orup.TCheckbutton'
            if mode == 'entry':
                xpos_polomka = self.w / 2.17
                ypos = self.h / 1.4
            else:
                xpos_polomka = self.w / 2.055
                ypos = self.h / 1.8
                if with_pic:
                    ypos = self.h / 1.17
            self.can.create_window(xpos_polomka, ypos,
                                   window=self.no_exit_var_check,
                                   tag='orupentry')

    def trace_trailer_checkbox_change(self, *args):
        self.no_exit_var.set(0)
        self.last_tare_var.set(0)
        if self.trailer_var.get():
            self.no_exit_var_check['state'] ='disabled'
            self.last_tare_check['state'] ='disabled'
        else:
            self.no_exit_var_check['state'] ='normal'
            self.last_tare_check['state'] ='normal'


    def pos_trailer(self):
        self.trailer_var = IntVar(value=0)
        self.trailer_var.trace_add('write', self.trace_trailer_checkbox_change)
        self.trailer_check = ttk.Checkbutton(variable=self.trailer_var,
                                             style='check_orup.TCheckbutton')
        #self.trailer_check['style'] = 'check_orup.TCheckbutton'
        xpos_polomka = self.w / 2.17
        ypos = self.h / 1.33
        self.can.create_window(xpos_polomka, ypos,
                               window=self.trailer_check,
                               tag='orupentry')

    def pos_last_tare(self, disabled):
        self.last_tare_var = IntVar(value=0)
        if disabled:
            state = "disabled"
        else:
            state = "normal"
        self.last_tare_check = ttk.Checkbutton(variable=self.last_tare_var,
                                               state=state)
        self.last_tare_check['style'] = 'check_orup.TCheckbutton'
        xpos_polomka = self.w / 1.775
        ypos = self.h / 1.4
        self.can.create_window(xpos_polomka, ypos,
                               window=self.last_tare_check,
                               tag='orupentry')

    def configure_combobox(self, om):
        om.master.option_add('*TCombobox*Listbox.background', '#3D3D3D')
        om.master.option_add('*TCombobox*Listbox.foreground', '#E2E2E2')
        om.master.option_add('*TCombobox*Listbox.selectBackground',
                             cs.orup_active_color)
        om.master.option_add('*TCombobox*Listbox.font', fonts.orup_font)
        om['height'] = 15
        om['style'] = 'orup.TCombobox'

    def clear_optionmenu(self,
                         event):  # that you must include the event as an arg, even if you don't use it.
        if 'combobox' in str(event.widget):
            try:
                event.widget.clear()
            except:
                print(traceback.format_exc())
        return None

    def select_optionmenu(self,
                          event):  # that you must include the event as an arg, even if you don't use it.
        if 'combobox' in str(event.widget):
            event.widget.select_range(0, END)
        return None

    def get_btn_by_name(self, btn_name_png, btns_list):
        for btn in btns_list:
            if btn[0] == btn_name_png:
                return btn[7]

    def try_set_attr(self, optionmenu, attr, admitted, fail_message='Укажите'):
        # Пытается присовить optionmenu значение attr, если attr принадлежит множеству admitted. Если же нет
        # присваивает fail_message):
        if attr in admitted:
            optionmenu.set(attr)
        else:
            optionmenu.set(fail_message)

    def checkOrupCarnum(self):
        if len(self.orupCarNumVar.get()) < 8:
            return True

    def checkOrupContragent(self):
        insert = self.contragentCombo.get()
        if insert not in self.operator.contragentsList:
            return True

    def checkRfid(self, carnum):
        for car in self.operator.terminal.carlist:
            if carnum == car[0] and car[5] == 'rfid':
                print('have a contact!')
                return True

    def initOrupAct(self, mode='redbg'):
        carnum = self.orupCarNumVar.get()
        if self.operator.fgsm:
            self.operator.if_show_weight = False
        self.car_protocol = self.operator.fetch_car_protocol(carnum)
        data_dict = {}
        data_dict['car_number'] = carnum
        data_dict['car_protocol'] = self.car_protocol
        data_dict['ar_status'] = self.operator.gcore_status
        data_dict['course'] = self.car_course
        data_dict['chosen_trash_cat'] = self.trashCatOm.get()
        data_dict['type_name'] = self.trashTypeOm.get()
        data_dict['weight_data'] = int(self.operator.wr.weigth)
        data_dict['carrier_name'] = self.contragentCombo.get()
        data_dict['client_name'] = self.clientOm.get()
        data_dict['have_brutto'] = self.operator.fetch_if_record_init(carnum)
        data_dict['have_rfid'] = self.check_car_rfid(carnum)
        data_dict['choose_mode'] = self.car_choose_mode
        data_dict['source'] = self.car_detected_source
        data_dict['photo_object'] = self.settings.redbg[3]
        data_dict['platform_name'] = self.platform_choose_var.get()
        data_dict['object_name'] = self.objectOm.get()
        data_dict['trailer'] = self.trailer_var.get()
        data_dict['comment'] = self.comm.get("1.0", 'end-1c')
        response = self.operator.orup_error_manager.check_orup_errors(
            orup='brutto',
            xpos=self.settings.redbg[1],
            ypos=self.settings.redbg[2],
            clients=self.operator.general_tables_dict['clients'],
            **data_dict)
        # if response and response['description'] == \
        #    'Попытка ручного пропуска машины с меткой или картой':
        #    ...
        if not response:
            self.start_car_protocol(orup_mode=self.settings.orup_enter_comm)

    def delay_starting_weight_time(self):
        self.operator.if_show_weight = False
        time.sleep(1.5)
        self.operator.if_show_weight = True

    def check_car_rfid(self, carnum):
        try:
            rfid = self.operator.general_tables_dict[s.auto_table][carnum][
                'identifier']
        except KeyError:
            rfid = None
        return rfid

    def check_scale_errors(self):
        if int(self.operator.wr.weigth) % 10 != 0:
            return True

    def check_absence_error(self, string_var, listname):
        # Проверяет значение переменной string_var на факт нахождения в списке listname
        # Возвращает True, если string_name НЕ присутствует в listname
        insert = string_var.get()
        if insert.lower() not in [x.lower() for x in listname]:
            return True

    def destroyORUP(self, mode='deff'):
        self.can.delete('orupentry', 'errorwin')
        self.orupState = False
        self.destroyBlockImg(mode)
        self.car_course = None
        self.car_protocol = None
        self.abort_all_errors_shown()
        if mode == 'decline':
            if self.operator.fgsm and self.fgsm_gate_open:
                self.operator.ar_qdk.operate_gate_manual_control(
                    operation='close',
                    gate_name=self.fgsm_gate_open)
                self.fgsm_gate_open = None
            self.operator.ar_qdk.catch_orup_decline(car_number=self.carnum_was)
            try:
                self.operator.orup_blacklist_increment(self.carnum_was)
            except KeyError:
                self.operator.orup_blacklist_new_car(self.carnum_was)
        self.rebind_btns_after_orup_close()
        if self.operator.fgsm:
            threading.Thread(target=self.delay_starting_weight_time).start()

    def abort_all_errors_shown(self):
        self.bruttoErrorShown = False
        self.rfidErrorShown = False
        self.debtErrorShown = False
        self.car_again_error_shown = False

    def rebind_btns_after_orup_close(self):
        pass

    def unbindORUP(self):
        self.root.unbind('<Return>')
        self.root.unbind('<Escape>')
        self.root.unbind('<UP>')
        self.root.unbind('<DOWN>')
        self.bindArrows()

    def page_close_operations(self):
        pass

    def hide_widgets(self, widgets):
        if not isinstance(widgets, Iterable):
            widgets = [widgets]
        for widget in widgets:
            widget.lower()

    def show_widgets(self, widgets='deff'):
        if widgets == 'deff':
            widgets = self.hiden_widgets
        if not isinstance(widgets, Iterable):
            widgets = [widgets]
        for widget in widgets:
            widget.lift()

    def get_attr_and_draw(self, attr, *args, **kwargs):
        obj = self.getAttrByName(attr)
        imgobj = self.can.create_image(obj[1], obj[2], image=obj[3], *args,
                                       **kwargs)
        return imgobj

    def draw_gate_arrows(self):
        self.draw_set_arrow(self.settings.exit_gate)
        self.draw_set_arrow(self.settings.entry_gate)

    def open_entry_gate_operation_start(self):
        threading.Thread(target=self.rotate_gate_arrow, args=(
            self.settings.entry_gate, 'open', 'OUT', 1, 80)).start()


    def open_exit_gate_operation_start(self):
        threading.Thread(target=self.rotate_gate_arrow, args=(
            self.settings.exit_gate, 'open', 'OUT', 1, 80)).start()

    # threading.Thread(target=self.rotate_gate_arrow, args=(self.settings.entry_gate, 'open', 'IN', -1, -80)).start()

    def close_entry_gate_operation_start(self):
        threading.Thread(target=self.rotate_gate_arrow, args=(
            self.settings.entry_gate, 'close', 'OUT', -1, 0)).start()

    def close_exit_gate_operation_start(self):
        threading.Thread(target=self.rotate_gate_arrow, args=(
            self.settings.exit_gate, 'close', 'OUT', -1, 0)).start()

    def rotate_gate_arrow(self, arrow_attr, pos, course, step=8, endpos=80,
                          sleeptime=0.010):
        arrow_info = self.operator.road_anim_info[arrow_attr]
        while arrow_info['busy']:
            pass
        else:
            arrow_info['busy'] = True
        while arrow_info['pos'] != endpos:
            self.can.delete(arrow_attr)
            if (self.operator.current == 'MainPage' or self.operator.current == 'ManualGateControl') and \
                    self.operator.currentPage.blockImgDrawn == False:
                self.draw_set_arrow(arrow_attr)
            arrow_info['pos'] += step
            sleep(sleeptime)
        arrow_info['busy'] = False

    def drawExitWin(self, name='exitwin', slice='shadow', btnsname='exitBtns',
                    *seconds, **kwargs):
        if self.blockImgDrawn == False:
            self.initBlockImg(name=name, btnsname=btnsname, mode='new')

    def draw_set_arrow(self, arrow_attr):
        arrow_info = self.operator.road_anim_info[arrow_attr]
        image = Image.open(self.settings.imgsysdir + 'gate_arrow.png')
        start = 0
        end = image.height
        obj = self.getAttrByName(arrow_attr)
        tags = ['maincanv'] + [arrow_attr]
        # print('Установка стрел', self.operator.road_anim_info)
        self.can.delete(arrow_attr)
        tkimage = ImageTk.PhotoImage(
            image.rotate(arrow_info['pos'], expand=True, center=(start, end)))
        self.can.create_image(obj[1], obj[2], image=tkimage, tags=tags)
        self.operator.road_anim_info[arrow_attr]['img'] = tkimage
        self.operator.road_anim_info[arrow_attr]['img_obg'] = image

    def block_gravity(self):
        self.operator.status_ready = False
        self.can.delete('winBtn', 'btn', 'tree')
        self.drawWin('win', 'lock_screen')
        self.can.create_text(self.w / 2, self.h / 2,
                             text='ВНИМАНИЕ!\nСистема заблокирована!'
                                  '\nПоскольку Вы попытались взесить брутто,'
                                  '\nне закрыв старый заезд!\nСвяжитесь с региональным оператором\nдля дальнейших инструкций...',
                             font=fonts.time_font,
                             fill=self.textcolor,
                             justify='center')
        # self.can.update()
        self.root.quit()
        while True:
            sleep(60)
