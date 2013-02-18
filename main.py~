#! /usr/bin/python
# -*- coding: utf-8 -*-


import sys,codecs,subprocess,readline,re,string
import negative,make_sentence,syori,struc_analyze,parallel,modifier,make_clause
from types import *

## 辞書の定義
info_dic = {"main":"none","Ga":"none","Wo":"none","Ni":"none","He":"none","To":"none","Kara":"none","Yori":"none","De":"none","Time":"none","Predict":"none","Modi":"none"}

"""
# 節ごとの分析結果を格納するクラス
#一番最初に、c_infoクラスが呼び出されて、次にそれを継承したkihon_info、最後に２つを継承したmorp_infoが呼び出される
class c_info:
    #初期化メソッドに文節単位の情報を格納
    def __init__(self,c_dependency,position,parallel_p_num,parallel_c_num,c_clause_type):
        self.c_dep = c_dependency
        self.position = position
        self.p_p_num = parallel_p_num
        self.p_c_nun = parallel_c_num
        self.c_c_type = c_clause_type

class morp:
    def __init__(self,input_morp,reg_morp_form,pos,dom,cat):
        self.input_morp
        self.reg_morp_form
        self.pos
        self.dom
        self.cat
"""

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

#修飾語と格の関係を構築する関数
def make_case_set(info_dic):

    #stackは文中に存在する修飾語と格をとりあえず保存するリスト
    stack = []
    #case_set_listは修飾語と格の組を保存するリスト
    case_set_list =[]
    #checked_listは処理を終えた語を保存するリスト。whileの終了条件用に作成
    checked_list = []
    #index_listは入力文の語の並びを保存しておくリスト
    index_list = []
    #mod_index_listは修飾語のみを保存しておくリスト。（修飾語だけ先に処理したいから）
    modi_index_list = []
    #set_dicは修飾語と格のセットを保存する辞書。keyは格の名前or述語,valueがセット（リスト）
    set_dic = {}

    #add all words from info_dic to stack
    for one in info_dic:
        if not info_dic[one] == 'none':
            stack.append(info_dic[one])
            index_list.append(info_dic[one].order)
            
            if info_dic[one].pos == 'modi':
                modi_index_list.append(info_dic[one].order)
                #code for check
                #print "modifier address in memory",info_dic[one]
                #print "word for one is:",info_dic[one].morpheme
                #print "dependency of it modi is:",info_dic[one].dependency
    modi_index_list.sort()

    #以下、コメントアウト中。上の記述で代用できている
    """
    for one in stack:
        if one.pos == "modi":
            modi_index_list.append(info_dic[one].order)
            # code for check
            print "modifier address in memory",one
            print "word for one is:",one.morpheme
            print "dependency of it modi is:",one.dependency
    modi_index_list.sort()
    """
    #print "modi_list is:",modi_index_list

    #初回のみ修飾語のindex listであるmodi_index_listの一番最初を指定
    if not len(modi_index_list) == 0:
        next_w = modi_index_list[0]
    else:
        next_w = index_list[0]
    
    while not len(checked_list) == len(stack):
        
        for one in stack:
            if next_w == one.order:
                checking_word = one
                break
        
        #-----------------------------------------------------------------
        #code for check
        #print "---------------------------------------"
        #print "stack is",stack
        #print index_list
        #print "next_w is",next_w
        #print "checking_word is",checking_word
        #print "pos of above word is",checking_word.pos
        #-----------------------------------------------------------------

        if checking_word.pos == "modi":
            #print "modi route is succeeful"
            case_set_list.append(checking_word)
            index_list.remove(next_w)
            modi_index_list.remove(next_w)

            next_w = checking_word.dependency
            checked_list.append(checking_word)

        if checking_word.pos == "case":
            case_set_list.append(checking_word)
            checked_list.append(checking_word)
            index_list.remove(next_w)
            #ここで、modifierとcaseの順番を逆にしておく
            case_set_list.reverse()

            case_name = checking_word.case_analiyzed

            set_dic.setdefault(case_name,case_set_list)
        
            case_set_list = []
            #もし、まだ修飾語リストが空でなかったら（他の格にかかる修飾語が存在する場合）
            if not len(modi_index_list) == 0: 
                next_w = modi_index_list[0]
            else:
                if not len(index_list) == 0:
                    next_w = index_list[0]
                else:
                    pass
                
        if checking_word.pos == "predict":
            case_set_list.append(checking_word)
            checked_list.append(checking_word)
            if next_w in index_list:
                index_list.remove(next_w)

            predict_name = checking_word.case_analiyzed
            set_dic.setdefault(predict_name,case_set_list)

            case_set_list = []
            #もし、まだ修飾語リストが空でなかったら（他の格にかかる修飾語が存在する場合）
            if not len(modi_index_list) == 0:
                next_w = modi_index_list[0]
            else:
                if not len(index_list) == 0:
                    next_w = index_list[0]
                else:
                    pass

    return set_dic


def add_negative(set_dic,negative):
    predict_list = set_dic["Predict"]
    
    dep = 'n'
    per='n'
    pos='negative'
    cat='n'
    dom='n'
    case='n'
    case_ana='n'
    order='n'

    if negative == "willness":
        reg = "ない（意思）"
        morp = "ない（意思）"

    if negative == "posess":
        reg = "ない（両手）"
        morp = "ない（両手）"

    if negative == "perfect":
        reg = "ない（未完了）"
        morp = "ない（未完了）"

    if negative == "impossible":
        reg = "無理"
        morp = "無理"

    if negative == "experience":
        reg = "。。。"
        morp = "。。。"

    if negative == "need":
        reg = "不必要"
        morp = "不必要"
        
    negative_info = info(dep,per,reg,morp,pos,cat,dom,case,case_ana,order)
    predict_list.append(negative_info)
    
    set_dic["Predict"] = predict_list


    return set_dic
    



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
    #returns 0 if not negation, returns 1 if negation
    negative_value = negative.find_negation(clause_list,clause_num,clause)
    
    if negative_value == 0:
        negative_choice = ""
    else:
        negative_choice = negative.negation(clause_list,clause_num,clause)

    #文の構文に関する情報。返ってくるのはハッシュマップ
    struc_dic = struc_analyze.structure_analyzer(clause_list,clause_num,clause)
    #文の情報を抽出。返ってくるのはリスト
    out_list = syori.Syori(clause_list,clause_num,clause,negative_choice)
    #節が複数節なのか？単節なのか？を判断する。返ってくるのは二値。yes or no
    clause_check_result = make_clause.clause_check(out_list)
    
    #そもそもif分けする必要はどこにもないので、そのうち修正すること
    if clause_check_result == "yes":
        out_list = make_clause.make_clause_set(out_list)
    #別に記述せんでもいいが、明文化しておけばわかりやすいじゃん
    if clause_check_result == "no":
        out_list = make_clause.make_clause_set(out_list)
    print "======================================="
    print "result of make clause:",out_list
    print "======================================="
    out_list,orig_index_list = parallel.heiretsu(out_list)

    print "======================================="
    out_list,orig_index_list = modifier.modi(out_list,orig_index_list)

    print "======================================="
    print "after make modifier list:",out_list
    print "======================================="
    print "structure information is:",struc_dic
    print "======================================="
    out_list = parallel.c_heiretsu(out_list)



    print "-----------------------------------"
    print "Is clause multi or not?:",clause_check_result
    

    '''
    set_dic = make_case_set(info_dic)
    if not negative_choice == "":
        set_dic = add_negative(set_dic,negative_choice)
        
    print "--------------------------"
    print "About structure information"
    print struc_dic
    print "--------------------------"
    print "About case dictionary information"
    print set_dic
    print "--------------------------"

    make_sentence.sentence_rule(set_dic,struc_dic)
        
    #print set_dic
    #print info_dic

    '''

    return out_list,struc_dic


if __name__ == '__main__':

    sentence = raw_input("文を入力してネ☆\n※必ず文末に句点かクエスチョンマークで終了してください。\n")
    info_dic,struc_dic = knp_tab(sentence)
