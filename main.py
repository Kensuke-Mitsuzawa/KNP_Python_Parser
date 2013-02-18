#! /usr/bin/python
# -*- coding: utf-8 -*-


import sys,codecs,subprocess,readline,re,string
import syori
from types import *

## 辞書の定義
info_dic = {"main":"none","Ga":"none","Wo":"none","Ni":"none","He":"none","To":"none","Kara":"none","Yori":"none","De":"none","Time":"none","Predict":"none","Modi":"none"}

#文節、基本句、形態素の情報が格納されている
#基本句ごとの情報を格納する
class info:
    def __init__(self,c_dependency,c_position,parallel_p_num,parallel_c_num,c_clause_type,c_counter,c_kazu,k_dependency,predicate,main_case,tense,case_relation,kaiseki_case,morp,main,case_check,predicate_check,clause_type,clause_func,k_position,para_check,para_type,modify_type,modify_check,per,k_counter,k_kazu,input_morp,reg_morp_form,pos,dom,cat):
        
        self.c_dep = c_dependency
        self.c_position = c_position
        self.p_p_num = parallel_p_num
        self.p_c_num = parallel_c_num
        self.c_clause_type = c_clause_type
        self.c_counter = c_counter
        self.c_kazu = c_kazu
        self.k_dep = k_dependency
        self.predicate = predicate
        self.main_case = main_case
        self.tense = tense
        self.case_relation = case_relation
        self.kaiseki_case = kaiseki_case
        self.morp = morp
        self.main = main
        self.case_check = case_check
        self.predicate_check = predicate_check
        self.clause_type = clause_type
        self.clause_func = clause_func
        self.k_position = k_position
        self.para_check = para_check
        self.para_type = para_type
        self.modify_type = modify_type
        self.modify_check = modify_check
        self.per = per
        self.k_counter = k_counter
        self.k_kazu = k_kazu
        self.input_morp = input_morp
        self.reg_morp_form = reg_morp_form
        self.pos = pos
        self.dom = dom
        self.cat = cat


def clause_count(tmp_list):
## 節の数と各節が何行文の情報を持っているのか調べる関数    

    ## clause_numは節の数,リストclauseは各節が何行の情報を持っているか。
    clause_num = 0
    clause = []
    c_num = -1

    print "-----------------------------"

    for tmp in tmp_list:
 
       
        if tmp == "*":   
            ## 前の節が何行分の情報を持っていたか。リストに追加する
            clause.append(c_num)
            
            ## c_numの数を初期化
            c_num = 1
            
            ## clause_numの数をひとつ増やす
            clause_num += 1
            
        ## 処理の都合上、最後の節はカウントできないので、無理やりだけど、こうする 
        elif tmp == "EOS\n":
            
            ## EOSの前には。、？！の記号しかないと仮定して-1する
            c_num = c_num - 1
            clause.append(c_num)

        else:            
            c_num += 1

    clause.pop(0)
    print "Number of Clauses is",clause_num
    print "List of lines in each clause",clause

    return clause_num,clause


def knp_tab(sentence):

    tmp_list = []
    clause_list = []

    echo = subprocess.Popen(['echo',sentence],
                            stdout=subprocess.PIPE,
                            )


    juman = subprocess.Popen(['juman'], 
                             stdin=echo.stdout,
                             stdout=subprocess.PIPE,
                             )


    knp = subprocess.Popen(['knp','-case','-tab'],
                           stdin = juman.stdout,
                           stdout=subprocess.PIPE,
                           )


    end_of_pipe_tab = knp.stdout

    for line in end_of_pipe_tab:
        #print line
        line_split = line.split(" ")
        tmp_list.append(line_split[0])
        clause_list.append(line)
        
    #--------------------------------------
    #ここで各処理関数に情報を投げる
    clause_num, clause = clause_count(tmp_list)

    #文の情報を抽出。返ってくるのはリスト
    out_list = syori.Syori(clause_list,clause_num,clause)
 
if __name__ == '__main__':

    sentence = raw_input("文を入力してネ☆\n※必ず文末に句点かクエスチョンマークで終了してください。\n")
    knp_tab(sentence)
