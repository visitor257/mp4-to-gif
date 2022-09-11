import tkinter.filedialog
from tkinter import *
from moviepy.editor import *
import os
#from time import sleep


def mp4_to_gif():
    for i in select_items:
        i.place_forget()
    for i in video_data_items:
        i.place_forget()
    for i in converting_items:
        ix, iy, iw, ih = converting_items[i]
        put(i, ix, iy, iw, ih)
    root.after(100,convertion_start)
    #print("1")
def convertion_start():
    data_mp4_path, data_gif_path, data_size_w, data_size_h, data_fps=(mp4_path.get(),gif_path.get(),int(res_w.get()),int(res_h.get()),int(fps_entry.get()))
    gif=VideoFileClip(data_mp4_path).resize((data_size_w, data_size_h))
    gif.write_gif(data_gif_path, fps=data_fps)
    for i in converting_items:
        i.place_forget()
    put(con_done,win_w/2-100,win_h/2-25,200,50)
    root.after(2000,con_d)
def con_d():
    con_done.place_forget()
    for i in select_items:
        ix, iy, iw, ih = select_items[i]
        put(i, ix, iy, iw, ih)
    for i in video_data_items:
        ix, iy, iw, ih = video_data_items[i]
        put(i, ix, iy, iw, ih)


def mp4_data_show(mp4_loc):
    global fps_entry
    v=VideoFileClip(mp4_loc)
    vw,vh=v.size
    res_w_text.set(str(vw))
    res_h_text.set(str(vh))
    vfps=v.fps
    fps_entry_text.set(str(int(vfps)))
    fps_entry=Spinbox(root,from_=1,to=int(vfps),textvariable=fps_entry_text)
    v.close()


def put(item,x,y,w,h):
    item.place(x=x,y=y,width=w,height=h)


def mp4_select():
    path=tkinter.filedialog.askopenfilename(filetypes=[("MP4文件", ".mp4")])
    if not path or path=="":
        pass
    elif os.path.splitext(path)[-1]!=".mp4":
        tkinter.messagebox.showwarning("注意","文件不是mp4文件")
    else:
        mp4_path_text.set(path)
        mp4_data_show(path)
        for i in video_data_items:
            ix, iy, iw, ih = video_data_items[i]
            put(i, ix, iy, iw, ih)

def mp4_watch_show():
    path=mp4_path.get()
    if not path or path=="":
        tkinter.messagebox.showwarning("注意","未选择mp4文件")
    elif os.path.splitext(path)[-1]!=".mp4":
        tkinter.messagebox.showwarning("注意","文件不是mp4文件")
    else:
        os.startfile(path)

def gif_select():
    path=tkinter.filedialog.asksaveasfilename(initialfile='output',filetypes=[("GIF文件", ".gif")])
    if path and os.path.splitext(path)[-1]!=".gif":
        path+=".gif"
    #print(path)
    if not path or path=="":
        pass
    elif os.path.splitext(path)[-1]!=".gif":
        tkinter.messagebox.showwarning("注意","文件不是gif文件")
    else:
        gif_path_text.set(path)

def start_convert():
    path_mp4=mp4_path.get()
    path_gif=gif_path.get()
    if (not path_mp4 or path_mp4=="") and (not path_gif or path_gif==""):
        tkinter.messagebox.showwarning("注意","未选择mp4文件和gif输出路径")
    elif not path_mp4 or path_mp4=="":
        tkinter.messagebox.showwarning("注意","未选择mp4文件")
    elif not path_gif or path_gif=="":
        tkinter.messagebox.showwarning("注意","未选择gif输出路径")
    elif os.path.splitext(path_mp4)[-1]!=".mp4":
        tkinter.messagebox.showwarning("注意","mp4文件有误")
    elif os.path.splitext(path_gif)[-1]!=".gif":
        tkinter.messagebox.showwarning("注意","输出文件不是gif文件")
    else:
        mp4_to_gif()
        #mp4_to_gif(path_mp4,path_gif,int(res_w.get()),int(res_h.get()),int(fps_entry.get()))
        #print("pass")


win_w=640
win_h=360

root = Tk()
root.title("mp4转gif")
root.geometry(f"{win_w}x{win_h}")
# var = StringVar()
# e = Entry(root, textvariable=var)
# var.set("hello")
# put(e,win_w/2,win_h/2,100,50)
# e.place(win_w/2,win_h/2,100,50)

select_items={}
####  显示   mp4文件
mp4_title_text=StringVar()
mp4_title=Label(textvariable=mp4_title_text,font=("simsun",18))
mp4_title_text.set("mp4文件")
put(mp4_title,win_w*0.25-50,win_h*0.25-32,100,25)
select_items[mp4_title]=(win_w*0.25-50,win_h*0.25-32,100,25)
####   输入框   mp4路径
mp4_path_text=StringVar()
mp4_path=Entry(root,textvariable=mp4_path_text)
mp4_path_text.set("")
put(mp4_path,win_w*0.25-100,win_h*0.25,200,30)
mp4_path.config(state='readonly')
select_items[mp4_path]=(win_w*0.25-100,win_h*0.25,200,30)
####   按钮   选择mp4文件
mp4_sel=Button(root,text="选择",command=mp4_select)
put(mp4_sel,win_w*0.25-75,win_h*0.25+32,74,25)
select_items[mp4_sel]=(win_w*0.25-75,win_h*0.25+32,74,25)
####   按钮   预览mp4文件
mp4_watch=Button(root,text="预览",command=mp4_watch_show)
put(mp4_watch,win_w*0.25+1,win_h*0.25+32,74,25)
select_items[mp4_watch]=(win_w*0.25+1,win_h*0.25+32,74,25)
####   显示   转换图标
convert_text_text=StringVar()
convert_text=Label(textvariable=convert_text_text,font=("simsun",18))
convert_text_text.set("➡️")
put(convert_text,win_w*0.5-12.5,win_h*0.25,50,25)
select_items[convert_text]=(win_w*0.5-12.5,win_h*0.25,50,25)
####   显示   gif文件
gif_title_text=StringVar()
gif_title=Label(textvariable=gif_title_text,font=("simsun",18))
gif_title_text.set("gif文件")
put(gif_title,win_w*0.75-50,win_h*0.25-32,100,25)
select_items[gif_title]=(win_w*0.75-50,win_h*0.25-32,100,25)
####   输入框   gif路径
gif_path_text=StringVar()
gif_path=Entry(root,textvariable=gif_path_text)
gif_path_text.set("")
put(gif_path,win_w*0.75-100,win_h*0.25,200,30)
gif_path.config(state='readonly')
select_items[gif_path]=(win_w*0.75-100,win_h*0.25,200,30)
####   按钮   gif路径选择
gif_sel=Button(root,text="选择输出路径",command=gif_select)
put(gif_sel,win_w*0.75-75,win_h*0.25+32,150,25)
select_items[gif_sel]=(win_w*0.75-75,win_h*0.25+32,150,25)
####   按钮   开始转换
do_convert=Button(root,text="开始转换",command=start_convert)
put(do_convert,win_w*0.5-60,win_h*0.5-30,120,30)
select_items[do_convert]=(win_w*0.5-60,win_h*0.5-30,120,30)


####   视频参数
video_data_items={}
####   显示  分辨率
video_res_title=Label(text="分辨率",font=("simsun",18))
video_data_items[video_res_title]=(win_w*0.5-75,win_h*0.5+20,150,30)
####   输入框   分辨率w
res_w_text=StringVar()
res_w=Spinbox(root,from_=1,to=5000,textvariable=res_w_text)
res_w_text.set("20")
video_data_items[res_w]=(win_w*0.5-75,win_h*0.5+20+32,61,25)
####   显示   乘号
res_times=Label(text="×",font=("simsun",14))
video_data_items[res_times]=(win_w*0.5-12,win_h*0.5+20+32,24,25)
####   输入框   分辨率h
res_h_text=StringVar()
res_h=Spinbox(root,from_=1,to=5000,textvariable=res_h_text)
res_h_text.set("20")
video_data_items[res_h]=(win_w*0.5+14,win_h*0.5+20+32,61,25)
####   显示   帧率
video_fps_title=Label(text="帧率（fps）",font=("simsun",18))
video_data_items[video_fps_title]=(win_w*0.5-75,win_h*0.5+20+32+27,150,30)
####   位置信息   帧率
fps_entry_text=StringVar()
fps_entry=Spinbox(root,from_=1,to=60,textvariable=fps_entry_text)
fps_entry_text.set("60")
fps_entry_pos=(win_w*0.5-30,win_h*0.5+20+32+27+32,60,25)
video_data_items[fps_entry]=fps_entry_pos


####   转换中
converting_items={}
converting_title=Label(text="转换中...",font=("simsun",20))
converting_items[converting_title]=(win_w/2-100,win_h/2-25,200,50)
converting_info1=Label(text="（请在终端查看进度）",font=("simsun",14))
converting_items[converting_info1]=(win_w/2-100,win_h/2+27,200,25)
converting_info2=Label(text="GUI窗口可能会卡死，请不要关闭此程序",font=("simsun",16))
converting_items[converting_info2]=(win_w/2-200,win_h-27,400,25)

con_done=Label(text="转换完成",font=("simsun",20))

root.mainloop()