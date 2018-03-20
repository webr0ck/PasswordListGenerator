# -*- coding: utf-8 -*-
import math
import itertools
import re
import argparse
from termcolor import colored

def read_file(filename):
    f = open(filename,'r')
    result = []
    for string in f:
        string = string.rstrip()
        result.append(string)
    f.close()
    return result

def myprint(text,verbosity,level,error=0):
    if int(verbosity)>=int(level):
        if int(error)==0:
            print colored(text,'yellow')    
        else:
            print colored(text,'red') 
def createParser ():
    parser = argparse.ArgumentParser()
    parser.add_argument ('-с','--config', default='main.cfg', help='use another config file')
    parser.add_argument ('-p','--passwords',help='List of words what you whant to use')
    parser.add_argument ('-o','--output', default='passwords_list.txt', help='Output for list of password')
    return parser  

def words_concat(words_list):
    exit()
    

def read_config(file):
    param_list={}
    f_read=open(file,'r') 
    section_name = ''
    section_name_new=''
    for line in f_read:
        line=line.rstrip()
        if line[0]=='[':
            try:
                section_name_new=re.match(r'\[.*\]',line).group()
            except Exception as e:
                print "No section name. Big Error. Please use section name like [your section name]"
                print e
                continue
            if section_name_new:
                section_name=section_name_new
                section_name=section_name[1:-1]
                continue
        if section_name:
            param_name=''
            param = ''
            try:
                param_name=re.match(r'.*(?=\=)',line).group()
            except Exception as e:
                print 'Error while read param name'
                print e
            try:
                param=re.search(r'(?<=\=).*',line).group()
            except Exception as e:
                print 'Error while read param'
                print e
            updater_param_list=param_list.get(section_name)
            param=param.strip()
            param_name=param_name.strip()
            if isinstance(updater_param_list,dict):
                updater_param_list[param_name]=param
            else:
                updater_param_list={}
                updater_param_list.update({param_name:param})
            param_list.update({section_name:updater_param_list})
    f_read.close()    
    return param_list

def get_delimeter_mass(mass):
    i=0
    result=[]
    new_list_permutations = list(itertools.product(mass,repeat=len(mass)-1))
    for list_ in new_list_permutations:
        for el in mass:
            i=0
            new1=[]
            j=0
            k=0
            while k<len(mass):
                if k!=i:
                    new1.append(list_[j])
                    j+=1
                else:
                    new1.append(el)
                k+=1
                if len(new1)>len(mass):
                    break

            result.append(new1)
            i+=1 
    return result    


def main():
    global wordlist, col_combinations, param_list,verbosity
    verbosity = 0
    
    myprint('start',verbosity,0)
    parser=createParser()
    parser_params=parser.parse_args()
    config  = parser_params.config
    output  = parser_params.output
    use_hardcoded = False 
    default_paassword_list = ['WIFI','WPA','PSK','Company_name']
    max_words_on_pass = 6
    
    try:
        param_list=read_config(config)
    except:
        use_hardcoded = True
    if use_hardcoded==False:
        main = param_list.get('main')
        getdelimiters = main.get('delimiters')
        max_words_on_pass = main.get('max_words_on_pass')
        wordlist_file = main.get('wordlist_file')
        delimiters = getdelimiters.split(',')
        try:
            wordlist=read_file(wordlist_file)
        except:
            wordlist = default_paassword_list

    else:
        myprint('Use Hardcoded paramas',verbosity,0,1)
        getdelimiters = ['-','_','.','',' ']
        wordlist = default_paassword_list
        delimiters = getdelimiters
    
    
    myprint('Output file: '+output,verbosity,0)
    
    result = list(itertools.permutations(wordlist))
    result =[]
    for L in range(2, len(wordlist)+1):
            result.extend(list(itertools.combinations(wordlist, L)))

    delimiters_comb = get_delimeter_mass(delimiters)

    output_file=open(output,'w')
    pass_list=[]
    if len(delimiters_comb)>len(result):
        for delimiters_list in delimiters_comb:
            i=0
            
            
            for list_ in result:
                j=0
                k=0
                my_string=''
                while (j<max_words_on_pass):
                    
                    if i!=0 and j!=i:
                        my_string=my_string+list_[0]
                    else:

                        if j==0:
                            my_string=list_[0]
                            j+=1
                            continue
                        else:

                            my_string+=delimiters_list[k]+list_[j]
                            k+=1
                            j+=1
                    if k==len(delimiters_list) or j==len(list_):
                            output_file.write(my_string + '\n')
                            pass_list.append(my_string)
                            break
            pass_list.append(my_string)                            
            output_file.write(my_string + '\n')
            i+=1
    
    else:
        for list_ in result:
            i=0
            
            
            for delimiters_list in delimiters_comb:
                j=0
                k=0
                my_string=''
                print list_

                while (j<max_words_on_pass):
                    
                    if i!=0 and j==0:
                        my_string=my_string+list_[0]
                    else:

                        if j==0:
                            my_string=list_[0]
                            j+=1
                            continue
                        else:
                            my_string+=delimiters_list[k]+list_[j]
                            k+=1
                    j+=1
                    if k==len(delimiters_list) or j==len(list_):
                            output_file.write(my_string + '\n')
                            pass_list.append(my_string)
                            break
                print "here "+my_string
                output_file.write(my_string + '\n')
                pass_list.append(my_string)
                i+=1
        
 
    output_file.close()
    myprint('Number of passwords '+str(len(pass_list)),verbosity,0)
    myprint('Exit',verbosity,0)




if __name__ == '__main__':
        main()