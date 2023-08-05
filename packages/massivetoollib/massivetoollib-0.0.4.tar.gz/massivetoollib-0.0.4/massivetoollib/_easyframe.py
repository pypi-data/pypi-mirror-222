from typing import Any, Literal, Iterable, AnyStr, List
import pandas as pd
import os, datetime, time
from bs4 import BeautifulSoup
Config={
    'commands':{
        'sheet':'Sheet1',
        'extension_excepted': ['xlsx', 'json', 'html', 'csv'],
        'global_data':[],
        'securename':os.path.dirname(__file__)+'/Download/MyApp-test'+ str(datetime.datetime.now())[:18].replace(' ',''),
        '__details__':{
            'frame_data':Any,
            'data_file':Any,
            'file':str,
            'page':str,
            'empty_frame':bool,
            'frame':Any
            }
    },
    '__result_':[],
}


class easyframe :
    config=Config
    __details__={}
    __result_= []
    __filt_result_ = []
    __newframe_ =[]
    def __init__(self,frame_data:Any=None, data_file:Any=None,data_page:str=None, empty_frame:bool=False) -> Any :
        self.frame_data = frame_data
        self.file = data_file
        self.page = data_page if data_page is not None else self.config['commands']['sheet']
        self.data_file = self.read_file(self.file, self.page )
        self.empty_frame = empty_frame
        self.frame__ = self.checkself()
        self.config['commands']['__details__'] = {
            'frame_data':self.frame_data,
            'data_file':self.data_file,
            'file':self.file,
            'page':self.page,
            'empty_frame':self.empty_frame,
            'frame':self.frame__,
            }
    def checkself(self)->Any:
        self.__result_ = []
        b={"Test":{"0":1, "2":2}}
        myframe = self.config['commands']['__details__']['frame_data']
        File = self.config['commands']['__details__']['data_file']
        Empty = self.config['commands']['__details__']['empty_frame']
        R=(myframe is not None and myframe or (File!=None and File or (Empty==True and self.defaultdataframe() or b)))
        self.__result_ =R
        return self.__result_
    @classmethod
    def __CC__(cls,C:Any)->Any:
        b={"Test":{"0":1, "2":2}}
        C = cls.config
        myframe = C['commands']['__details__']['frame_data']
        File = C['commands']['__details__']['data_file']
        Empty = C['commands']['__details__']['empty_frame']
        R=(myframe is not None and myframe or (File!=None and File or (Empty==True and cls.defaultdataframe() or b)))
        return R
    
    @classmethod        
    def find_extension(cls,file:str)->AnyStr:
        try:
            p=str(file)[-7:].index('.')
            ext=str(file)[-7:][(p+1):]
            return ext or None
        except:
            pass

    @classmethod
    def read_file(cls,readfile:str=None, sheet:str=None) -> Any:
        cls.__result_ = []
        page = sheet if sheet is not None else cls.config['commands']['sheet']
        if readfile:
            if os.path.exists(readfile):    
                extension = cls.find_extension(readfile)
                if extension in cls.config['commands']['extension_excepted']:
                    if extension == 'xlsx':
                        data = pd.read_excel(readfile, sheet_name=page)
                        if isinstance(data, list):
                            for i in data:
                                cls.__result_.append(pd.DataFrame(i))
                        else:
                            cls.__result_ = data
                    elif extension == 'csv':
                        data = pd.read_csv(readfile)
                        cls.__result_.append(data)
                    elif extension == 'json':
                        data = pd.read_json(readfile)
                        cls.__result_.append(data)
                        
                    elif extension == 'html':
                        cls.__result_= cls.htmlTb_to(readfile)
                    else:
                        print('some error opening this file')
                else:
                    print('Not supported file extension')
            else:
                print('file dont exist')
        else:
            print('insert one file')
        return cls.__result_
    
    @classmethod
    def htmlTb_to(cls,file_name:str) -> Any:
        html_head='<html>\n<head>\n</head>'
        html_foot='</html>'
        ii=''
        with open(file_name, 'r+') as f:
            r = f.readlines()
            f.close()
            a = ''.join(r).replace(' ','') 
            if  a.find('<html>') == True:
                ii = a  
            else:
                ii = ''.join(html_head + a + html_foot)
            t=BeautifulSoup(ii,"html.parser")
            tabs= t.findAll('table')
            th = t.find('thead')
            th_n = th.findAll('th', recursive= True)
            tb= t.find('tbody')
            tb_rows= tb.find_all('tr')
            frame={}
            count=1
            frx={}
            for c in range(0,(len(th_n) - 1)):
                kk = th_n[count].get_text()
                for ro in tb_rows:
                    td = ro.find('th')
                    tdh= td.get_text()
                    td2 = ro.findAll('td')
                    tdh2= td2[c].get_text()
                    frx[tdh]= tdh2
                frame[kk] = frx
                frx={}
                count +=1
            framejson_result = str(frame).replace('\'', '"')
            df = pd.read_json(framejson_result)
            result=(df,framejson_result)
        return result[0]
    

    @classmethod
    def defaultdataframe(cls) -> Any:
        cls.__result_ = []
        try:
            import string
            default_dataframe={}
            rows={}
            A = list(string.ascii_uppercase).copy()
            for i in A :
                default_dataframe[i]=rows
                for r in range(0,11):
                    default_dataframe[i][r]= " "
            jsondict=str(default_dataframe).replace('\'','"')
            total_info= [pd.DataFrame(default_dataframe), default_dataframe, jsondict]
            cls.__result_.append(total_info[0])
        except :
            pass
        return cls.__result_
    @classmethod
    def all_in1(cls, listdicts:Iterable) -> list:
        'imput listdicts need to be an instance of list or tuple'
        cls.__result_, result = [], []
        l = listdicts
        try:
            while len(l)>0:
                for i in l:
                    if isinstance(i, dict):
                        result.append(i)
                        l.remove(i)
                    elif isinstance(i,(list,tuple)):
                        l.extend(i)
                        l.remove(i)
                    else:
                        l.remove(i)                         
        except Exception as e:
            print('Error summing nested lists data checke if is correct type of input',e)
            pass
        finally:
            r={}
            for i in result:
                for k, v in i.items():
                    r[k] = v
            cls.__result_.append(pd.DataFrame(r))
            return cls.__result_

    @classmethod
    def filt_col(cls, filt_cols_name:Iterable=None, save:bool=False, pathx:str=None, sheet:str=None, extension:str=None, save_cols:Iterable=None)->Any :
        if len(cls.__result_) < 1:
            cls.__result_ = cls.__CC__(cls.config)
            time.sleep(0.2)
        cols = save_cols
        c = filt_cols_name
        x=None
        try:
            if type(c)==str or isinstance(c,(list,tuple)):
                for i in cls.__result_:
                    x =i.filter(items=c)
            else:
                print('Not supported input type')
            if save == True:
                cls.saveframe(x,pathx, sheet, extension, cols)
            else:
                cls.__result_.append(x)
            return x, cls.__result_
        except Exception as e:
            print('columns not founds or not correct type of input')
            pass
    @classmethod
    def new_frame(cls, newframe:Any=None, newfile:str=None, newpage:str=None,  save:bool=False, pathx:str=None, sheet:str=None, extension:str=None, column=None) -> Any:
        cols=column
        cls.__newframe_ = pd.DataFrame(newframe) if newframe is not None else (cls.read_file(newfile, newpage) if newfile is not None else print('error in new frame cretor function'))
        if save == True:
            
            cls.saveframe(cls.__newframe_, pathx, sheet, extension,cols)
        else:
            cls.__result_ = cls.__newframe_
        return cls.__result_
    @classmethod
    def write_file(cls, file:str=None, frame:Any=None, cols:Iterable=None, ind:bool=None, page:str=None)->Any: 
        inframe =cls.__CC__(cls.config)
        writepage = page if page is not None else cls.config['commands']['sheet']
        time.sleep(0.2)
        towriteframe = frame if frame is not None else inframe
        if file:
            if os.path.exists(file) :
                if isinstance(towriteframe,list):
                    for i in towriteframe:
                        r =0
                        x = cls.find_extension(file)
                        data = cls.read_file(file, sheet=page)                   
                        if x =='xlsx':
                            if isinstance(data, list):
                                for singl in data:
                                    l=pd.DataFrame(singl).values
                                    r = len(l) + 2
                                    pass
                            else:
                                l=pd.DataFrame(data).values
                                r = len(l) + 2
                                pass
                            with pd.ExcelWriter( file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                                i.to_excel( excel_writer=writer, engine='openpyxl', startrow=r, index=ind, sheet_name=writepage, columns=cols)
                        elif x =='json':
                            with open(file, 'r+') as f:
                                e = f.readlines()
                                ste= ''
                                for i in e :
                                    ste += ''.join(i)
                                js =i.to_json()
                                stj= ''.join(js)
                                nstj, nste = stj[1:], ste[:-1]
                                ff = nste+','+nstj
                                f.seek(0,0)
                                f.truncate(2)
                                f.write(ff)
                                f.close()     
                        elif x =='csv':
                            with open(file,'a') as f:
                                newcsv= i.to_csv()
                                f.write(newcsv)
                                f.close()
                        else:
                            print('not supported extension')
                else:
                    r =0
                    x = cls.find_extension(file)
                    data = cls.read_file(file, sheet=page)                   
                    if x =='xlsx':
                        if isinstance(data, list):
                            for singl in data:
                                l=pd.DataFrame(singl).values
                                r = len(l) + 2
                                pass
                        else:
                            l=pd.DataFrame(data).values
                            r = len(l) + 2
                            pass
                        with pd.ExcelWriter( file, engine='openpyxl', mode='a', if_sheet_exists='overlay') as writer:
                            towriteframe.to_excel( excel_writer=writer, engine='openpyxl', startrow=r, index=ind, sheet_name=writepage, columns=cols)
                    elif x =='json':
                        with open(file, 'r+') as f:
                            read = f.readlines()
                            ste= ''
                            for line in read :
                                ste += ''.join(line)
                            js =towriteframe.to_json()
                            stj= ''.join(js)
                            nstj, nste = stj[1:], ste[:-1]
                            ff = nste+','+nstj
                            f.seek(0,0)
                            f.truncate(2)
                            f.write(ff)
                            f.close()     
                    elif x =='csv':
                        with open(file,'a') as f:
                            newcsv= towriteframe.to_csv()
                            f.write(newcsv)
                            f.close()
                    else:
                        print('not supported extension')
        
            print('This file doesn t exist')
        else:
            pass

    @classmethod
    def saveframe(cls, frame:Any=None, savepath:str=None, sheet:str=None, exten:str=None, column:Iterable=None, save_index:bool=False) -> Any:
        inframe =cls.__CC__(cls.config)
        time.sleep(2)
        cols = column
        x= exten 
        save_df = frame if frame is not None else inframe
        save_page = sheet if sheet is not None else cls.config['commands']['sheet']
        try:
            x=((exten!=None and exten or ((exten==None and savepath!=None)  and cls.find_extension(savepath) or 'xlsx') ))
            save_path=(savepath==None and (cls.config['commands']['securename'] + '.' + x) or (cls.find_extension(savepath)==None and (savepath +'.'+ x) or savepath))
            fx= cls.find_extension(save_path)
            if os.path.exists(save_path):
                cls.write_file(save_path,save_df,cols,save_index,save_page)
            else:
                if isinstance(save_df, list):
                    for i in save_df :
                        if fx=='xlsx' :
                            i.to_excel( save_path, engine='openpyxl', index=save_index, sheet_name=save_page, columns=cols)
                        elif fx == 'json':
                            i.to_json(save_path)
                        elif fx == 'csv':
                            i.to_csv(save_path)
                else:
                    if fx=='xlsx' :
                        save_df.to_excel( save_path, engine='openpyxl', index=save_index, sheet_name=save_page, columns=cols)
                    elif fx == 'json':
                        save_df.to_json(save_path)
                    elif fx == 'csv':
                        save_df.to_csv(save_path)
        except Exception as e :
            print(e)
            pass   

    def __call__(self) -> Any:
        c = self.checkself()
        if c==None:
            c= self.__result_
        print(c,'zzzzzzzz')
        if isinstance(c,list):
            for i in c:
                print(f'{pd.DataFrame(i)}')
        else:
            print(f'{pd.DataFrame(c)}')
        return c

    def __str__(self) -> str:
        c = self.checkself()
        if c==None:
            c= self.__result_
        print(c,'zzzzzzzz')
        if isinstance(c,list):
            for i in c:
                print(f'{pd.DataFrame(i)}')
        else:
            print(f'{pd.DataFrame(c)}')


    @classmethod
    def filt_all(cls, filt_cols_name:Iterable=None, filt_row_val:Any=None, save:bool=False, pathx:str=None, sheet:str=None, extension:str=None, save_cols:Iterable=None)->Any :
        if len(cls.__result_) < 1:
            cls.__result_ = cls.__CC__(cls.config)
            time.sleep(0.2)
        print(cls.__result_,'zzzzzzzz')
        cols = save_cols
        c = filt_cols_name
        r = filt_row_val
        x=None
        F=None
        res=[]
        try:
            for df_ in cls.__result_:
                df_c = df_.filter(items=c)
                for col in c:
                    print(col)
                    for v in r:
                        print(v,'FFFFFFFFF')
                        F= df_c.loc[df_c[col]==v]
                        res.append(F)
                    print(res)
            else:
                print('Not supported input type')
            return F
        except Exception as e:
            print('columns not founds or not correct type of input')
            pass
        finally:
            print(F,'KKK')
            if save == True:
                cls.saveframe(F,pathx, sheet, extension, cols)
            return pd.DataFrame(F)

b={"A3AA": {"0": "13", "1": "13", "2": "13"}, "k": {"0": "4", "1": "4", "2": "3"}, "1": {"0": "4", "1": "4", "2": "4"}, "w": {"0": "6", "1": "6", "2": "6"}, "f": {"0": "4", "1": "4", "2": "4"}, "l": {"0": "2", "1": "2", "2": "2"}, "o": {"0": "3", "1": "3", "2": "3"}, "5": {"0": "4", "1": "4", "2": "4"}, "3": {"0": "2", "1": "2", "2": "2"}, "pp": {"0": "7", "1": "7", "2": "7"}}


print(easyframe(data_file='hh7.json').filt_all(filt_cols_name=['w','pp']))

