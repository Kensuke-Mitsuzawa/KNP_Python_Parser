#! /usr/bin/python
# -*- coding:utf-8 -*-


import re,string

class info:
    def __init__(self,c_dependency,c_position,parallel_p_num,parallel_c_num,c_clause_type,c_counter,c_kazu,k_dependency,predicate,main_case,tense,case_relation,kaiseki_case,morp,main,case_check,predicate_check,clause_type,clause_func,k_position,para_check,para_type,modify_type,modify_check,per,k_counter,k_kazu,input_morp,reg_morp_form,pos,dom,cat,nms):
        """
        文節、基本句、形態素の情報が格納されている
        基本句ごとの情報を格納する
        """
        
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
        self.nms = nms

def Syori(clause_list,clause_num,clause,negative_choice):
    """
    clause_listは節ごとに切った解析結果、clause_numは節の数、clauseは各節が何行分の情報を持っているか？リスト
    
    """
    #print "--------------------"

    #nmsはいつも空白文字（この関数では使わない）
    nms = ""

    #関数の出力となる配列。入力文と同じ並び順にしている
    out_list = []

    #カウンターの設置
    counter = 0

    #語の並び情報(order)
    order = 0

    #文節用の語の並び情報
    bnst_order = 0
    
    #基本句用の語の並び情報
    kihon_order = 0

    #処理の都合上、一時的にハッシュマップを格納する配列
    tmp_dic_list = []

    #--------------------------------------
    #ここで新しい節を読みおなし
    for value in clause:

        if counter == 0:
            start_pos = 1
            end_pos = value

        else:
            start_pos = end_pos + 1
            end_pos = end_pos + value

        counter += 1

        #クラスと同じハッシュマップを先に定義しておく
        bnst_dic = {"c_dep":[],"c_position":[],"parallel_type":[],"parallel_p_num":[],"parallel_c_num":[],"c_clause_type":[],"c_counter":"","c_kazu":"","k_dep":[],"predicate":[],"main_case":[],"tense":[],"case_relation":[],"kaiseki_case":[],"morp":[],"main":"","case_check":"","predicate_check":"","clause_type":[],"k_position":"","para_check":"","para_type":[],"modify_type":[],"modify_check":"","per":"","k_counter":"","k_kazu":"","clause_func":[],"input_morp":[],"reg_morp_form":[],"pos":[],"dom":[],"cat":[]}
        #形態素区別用のindex
        m_index = 0

        #基本句の正規化表現を保存しておく変数（重要）
        reg_marker = ""

        #形態素解析の正規化表現を保存しておく変数（重要）
        reg_marker_morp = ""

        #--------------------------------------
        #ここから*から*の範囲（文節の範囲）で情報を抽出していく
        #情報の抽出を正規表現でしていく
        for i in range(start_pos,end_pos + 1):
            sentence = clause_list[i]

            #--------------------------------------
            #文節の単位で情報の抽出
            if not re.findall(r"\* \dD|\* \dP|\* -\dD|\* \dP",sentence) == []:
                #--------------------------------------------------
                #並列構造に関する記述
                #<並キ:名>は並列構造の存在を示すタグ ただ、:名　が何を示すのか？は不明
                if not re.findall(r"<並キ:.*?>",sentence) == []:
                    parallel_type = "".join((re.findall(r"<並列タイプ:.*?>",sentence))).replace("<並列タイプ:","").strip(">")
                    bnst_dic["parallel_type"] = parallel_type
                    
                    #並列の句がいくつ続いているのか？
                    parallel_p_num = "".join((re.findall(r"<並結句数:.*?>",sentence))).replace("<並結句数:","").strip(">")
                    bnst_dic["parallel_p_num"] = parallel_p_num

                    #並列の文節がいくつ続いているのか？
                    parallel_c_num = "".join((re.findall(r"<並結文節数:.*?>",sentence))).replace("<並結文節数:","").strip(">")
                    bnst_dic["parallel_c_num"] = parallel_c_num


                if not re.findall(r"\* \dD|\* -\dD|\* \dP|\* -\dP",sentence) == []:
                    bnst_dependency = re.findall(r"\* \d|\* -\d",sentence)
                    bnst_dic["c_dep"] = int(("".join(bnst_dependency)).strip("* "))
                
                #--------------------------------------------------
                #文節の系列に関する記述
                bnst_dic["c_position"] = bnst_order
                #--------------------------------------------------
                #節の種類に関する記述
                c_clause_type = ""
                if not re.findall(r"<主節>",sentence) == []:
                    c_clause_type = "".join(re.findall(r"<主節>",sentence)).translate(string.maketrans("",""),"<>")  
                if not re.findall(r"<連用節>",sentence) == []:
                     c_clause_type = "".join(re.findall(r"<連用節>",sentence)).translate(string.maketrans("",""),"<>")
                if not re.findall(r"<連体節>",sentence) == []:
                    c_clause_type = "".join(re.findall(r"<連体節>",sentence)).translate(string.maketrans("",""),"<>")
                     
                bnst_dic["c_clause_type"] = c_clause_type

                #--------------------------------------------------
                #数量に関係する記述（基本句と共通）
                bnst_dic["c_counter"] = "".join(re.findall(r"<カウンタ:.*?>",sentence)).replace("<カウンタ:","").strip(">")

                if not re.findall(r"<数量>",sentence) == []:
                    bnst_dic["c_kazu"] = "yes"
                
                #文節用の並び番号を＋１
                bnst_order += 1


                """
                # def __init__(self,c_dependency,position,parallel_p_num,parallel_c_num,c_clause_type):
                #c_infoクラスに移していく
                clause_info = c_info(bnst_dic["dep"],bnst_dic["position"],bnst_dic["parallel_p_num"],bnst_dic["parallel_c_num"],bnst_dic["c_clause_type"])

                """
            #--------------------------------------
            #基本句単位での情報をパーズしていく
            if not re.findall(r"\+ \dD|\+ \dP|\+ -\dD|\+ -\dP",sentence) == []:
                

                bnst_dic["k_dep"] = []
                bnst_dic["predicate"] = []
                bnst_dic["main_case"] = []
                bnst_dic["tense"] = []
                bnst_dic["case_relation"] = []
                bnst_dic["kaiseki_case"] = []
                bnst_dic["morp"] = []
                bnst_dic["main"] = ""
                bnst_dic["case_check"] = ""
                bnst_dic["predicate_check"] = ""
                bnst_dic["clause_type"] = []
                bnst_dic["k_position"] = ""
                bnst_dic["para_check"] = ""
                bnst_dic["para_type"] = []
                bnst_dic["modify_type"] = []
                bnst_dic["modify_check"] = ""
                bnst_dic["per"] = ""
                bnst_dic["clause_func"] = []
                
                #kihon_key_name = "kihon" + str(order)
                kihon_key_name = "kihon"
 
                #----------------------------------------------------
                #述語情報の獲得はここら辺がひっかかるはず
                predicate = []
                if not re.findall(r"<状態述語>",sentence) == []:
                    predicate = re.findall(r"<状態述語>",sentence)
                if not re.findall(r"<動態述語>",sentence) == []:
                    predicate = re.findall(r"<動態述語>",sentence)
                if not re.findall(r"<体言止>",sentence) == []:
                    predicate = re.findall(r"<体言止>",sentence)
                
                predicate = "".join(predicate).translate(string.maketrans("",""),"<>")
                bnst_dic["predicate"] = predicate
                
                if not predicate == "":
                    bnst_dic["predicate_check"] = "yes"

                #動詞の時制について
                if not re.findall(r"<時制.*?>",sentence) == []:
                    t_c = "".join(re.findall(r"<時制.*?>",sentence))
                    tense = t_c.replace("時制-","").translate(string.maketrans("",""),"<>")
                
                    bnst_dic["tense"] = tense
                

                #述語に対する主題格
                #なんか、いつも<主題格:一人称優位>な気がするんだが...
                main_case = re.findall(r"<主題格:.*?>",sentence)
                main_case = "".join(main_case).replace("<主題格:","").strip(">")

                bnst_dic["main_case"] = main_case
                #<文末>タグについて
                position_t = re.findall(r"<文末>",sentence)
                
                #IDについて
                #ID = re.findall(r"<ID:.*?>",sentence)
                #品詞について
                #pos = re.findall(r"<助詞>",sentence)

                #体言か用言か
                #taigen = re.findall(r"<体言>",sentence)
                #yougen = re.findall(r"<用言:.*?>",sentence)


                #----------------------------------------------------
                #並列構造に関する記述（アルファ版）
                if not re.findall(r"<並キ:.*?>",sentence) == []:
                    bnst_dic["para_check"] = "yes"
                    bnst_dic["para_type"] = "".join(re.findall(r"<並列タイプ:.*?>",sentence)).replace("<並列タイプ:","").strip(">")


                #----------------------------------------------------
                #節の種類に関する記述
                clause_type = ""
                if not re.findall(r"<主節>",sentence) == []:
                    clause_type = "".join(re.findall(r"<主節>",sentence)).translate(string.maketrans("",""),"<>")  
                if not re.findall(r"<連用節>",sentence) == []:
                     clause_type = "".join(re.findall(r"<連用節>",sentence)).translate(string.maketrans("",""),"<>")
                if not re.findall(r"<連体節>",sentence) == []:
                    clause_type = "".join(re.findall(r"<連体節>",sentence)).translate(string.maketrans("",""),"<>")
                     
                bnst_dic["clause_type"] = clause_type
                #--------------------------------------------------
                #数量に関係する記述（文節と共通）
                bnst_dic["k_counter"] = "".join(re.findall(r"<カウンタ:.*?>",sentence)).replace("<カウンタ:","").strip(">")

                if not re.findall(r"<数量>",sentence) == []:
                    bnst_dic["k_kazu"] = "yes"
                
                
                #----------------------------------------------------
                #修飾のタイプに関する記述
                #以下の３パターンについてはいずれも単に「修飾」とみなしてよい（手話の文法では）

                #その語が形容詞で用言の場合
                modify_type = ""
                if not re.findall(r"<用言:形>",sentence) == []:
                    modify_type = "".join(re.findall(r"<用言:形>",sentence)).translate(string.maketrans("",""),"<>")
                #「おおきくて」のような場合、形容詞でなく、連体詞となる
                if not re.findall(r"<連体修飾>",sentence) == []:
                    modify_type = "".join(re.findall(r"<連体修飾>",sentence)).translate(string.maketrans("",""),"<>")
                    
                #別に条件は「副詞」だけでもいいんだろうが、念のため
                if not re.findall(r"<副詞>",sentence) == [] and not re.findall(r"<修飾>",sentence) == []:
                    modify_type = "副詞"
                
                #一応、チェックを入れておく
                if not modify_type == "":
                    bnst_dic["modify_check"] = "yes"

                bnst_dic["modify_type"] = modify_type
                

                #節機能に関する記述
                bnst_dic["clause_func"] = "".join(re.findall(r"<節機能-.*?>",sentence)).replace("<節機能-","").strip(">")
                
                #----------------------------------------------------
                #パラメータが複数の状態を取りうるものは以下に記述
                #モダリティ情報リスト
                modality_list = []
                #
                #respect_list = []
                #格関係リスト
                case_relation_list = []
                i_tmp_list = []
                i_tmp_list = sentence.split("<")

                for para in i_tmp_list:
                    para = para.replace(">","")
                    if not re.findall(r"モダリティ",para) == []:
                        para = para.replace("モダリティ-","")
                        modality_list.append(para)
                             
                    if not re.findall(r"敬語:.*",para) == []:
                        para = para.replace("敬語:","")
                        respect = para
                 
                    if not re.findall(r"格関係.*",para) == []:
                        para = re.sub(r"格関係\d:","",para)
                        case_relation_list.append(para)

                        bnst_dic["case_relation"] = case_relation_list

                    if not re.findall(r"解析格:.*",para) == []:
                        kaiseki_case = para.replace("解析格:","").strip("\n")
                        
                        bnst_dic["kaiseki_case"] = kaiseki_case

                #----------------------------------------------------
                #格に関する情報の獲得
                if not re.findall(r"<格要素>",sentence) == []:
                    bnst_dic["case_check"] = "yes"
                    
                #格解析については上の方で記述しているので省略

                #主題表現をとってくる 述語のところでチェックできるから、別にいらない気もするが..
                #とりあえず、以下の記述であれば、主格　かつ　私　→一人称　となるから間違いではないだろう
                if not re.findall(r"<主題表現>",sentence) == []:
                    bnst_dic["main"] = "yes"

                    if not re.findall(r"私",sentence) == []:
                        bnst_dic["per"] = 1

                    if not re.findall(r"あなた",sentence) == []:
                        bnst_dic["per"] = 2

                    if not bnst_dic["per"] == 1 and not bnst_dic["per"] == 2:
                        bnst_dic["per"] = 3
                    

                #文頭タグにたいして
                #position_t = re.findall(r"<文頭>",sentence)
                #人称について
                #person = re.findall(r"<.*人称?>",sentence)
                #格要素(述語の箇所にも現れることがある)
                
                #品詞については述語の箇所で記述しているので省略
                #用言か体言かは述語の箇所で記述しているので省略

                #--------------------------------------
                #正規化表記を拾う
                reg_exp = re.findall(r"(<正規化代表表記:.*?>)",sentence)
                if not reg_exp == []:
                    split_list = []
                    split_list = "".join(reg_exp).split("/")
                    split_list[0] = (split_list[0]).replace("<正規化代表表記:","")
                    split_list[1] = (split_list[1]).replace(">","")
                    bnst_dic["morp"] = split_list
                
                    #形態素。これを形態素の抽出部に渡す
                    reg_marker = re.findall(r"(<正規化代表表記:.*?>)",sentence)
                    
                #--------------------------------------
                #基本句単位でのかかりうけ情報を獲得
                if not re.findall(r"\+ \dD|\+ -\dD|\+ \dP|\+ -\dP",sentence) == []:
                    bnst_dic["k_dep"] = re.findall(r"\+ \d|\+ -\d",sentence)
                    bnst_dic["k_dep"] = int(("".join(bnst_dic["k_dep"])).strip("+ "))

                #--------------------------------------
                #基本句の並び情報をハッシュマップに登録する
                #基本句の並び情報を＋1
                bnst_dic["k_position"] = kihon_order
                kihon_order += 1
                #--------------------------------------
                #文節単位のハッシュに基本句のハッシュマップを登録
                #bnst_dic.setdefault(kihon_key_name,kihon_dic)

            #--------------------------------------
            #形態素情報    
            if re.findall(r"\+ \dD|\+ \dP|\+ -\dD|\+ -\dP",sentence) == [] and re.findall(r"\* \dD|\* \dP|\* -\dD|\* -\dP",sentence) == []:

                bnst_dic["input_morp"] = ''
                bnst_dic["reg_morp_form"] = ''
                bnst_dic["pos"] = []
                bnst_dic["dom"] = []
                bnst_dic["cat"] = []
                m_tmp_list = []
                m_tmp_list =  sentence.split(" ")
                
                bnst_dic["input_morp"] = m_tmp_list[0]
                bnst_dic["reg_morp_form"] = m_tmp_list[2]
                bnst_dic["pos"] = m_tmp_list[3]

                reg_marker_morp = re.findall(r"(<正規化代表表記:.*?>)",sentence)
                
                bnst_dic["dom"] = "".join(re.findall(r"<ドメイン:.*?>",sentence)).replace("<ドメイン:","").strip(">")
                bnst_dic["cat"] = "".join(re.findall(r"<カテゴリ:.*?>",sentence)).replace("<カテゴリ:","").strip(">")

                #文節単位のハッシュに形態素のハッシュを登録
                #bnst_dic.setdefault(m_key_name,morp_tmp_dic)
                m_index += 1
                

            #この状態で、文節から基本句（１つ）、形態素（基本句の正規化形態素に対応する形態素ひとつ）の情報をtmp_dic_listに格納できるはず
            """
            この部分はチェック用に書いただけ
            print '---------------------'
            print 'sentence is:',sentence
            print bnst_dic["input_morp"]
            print "reg_marker_morp","".join(reg_marker_morp)
            print "reg_marker","".join(reg_marker)
            print "position",bnst_dic["k_position"]
            """

            if reg_marker == reg_marker_morp and not reg_marker == "" and not reg_marker_morp == "":

                #直接、配列tmp_dic_listに追加をすると、問題が生じる。一度、aという辞書にしてやることで、この問題は解決できる
                a = dict(bnst_dic)
                tmp_dic_list.append(a)
                reg_marker = ""
                reg_marker_morp = ""
                
                    

            """
            #ここで毎回、クラスに情報を移していくとうまくいくだろう。
            #あと修正ポイント、ここですべて統合したクラスに書き込んでいってもたぶん、うまくいく。形態素から文節までの構造はすべて、bnst_dicに集約されている
            #基本句と形態素は辞書のキー、固定してやる
            #冗長だが、一度ハッシュマップから変数に代入してから、インスタンスを作成（ぼくのわかりやすさ優先）
            #iがend_posに一致するときのみ以下を実行する。
            #こうすると、スパースな情報が防げる
            #--------------------------------------------

            #形態素情報にずれがある状態。形態素の部分をリストにするなり、ちゃんと工夫する必要あり
            if i == end_pos:


                #文節に関する情報
                c_dependency = bnst_dic["dep"]
                c_position = bnst_dic["position"]
                parallel_p_num = bnst_dic["parallel_p_num"]
                parallel_c_num = bnst_dic["parallel_c_num"]
                c_clause_type = bnst_dic["c_clause_type"]
                #--------------------------------------------
                #基本句に関する情報
                k_dependency = kihon_dic["dep"]
                predicate = kihon_dic["predicate"]
                main_case = kihon_dic["main_case"]
                tense = kihon_dic["tense"]
                case_relation = kihon_dic["case_relation"]
                kaiseki_case = kihon_dic["kaiseki_case"]
                morp = kihon_dic["morp"]
                main = kihon_dic["main"]
                case_check = kihon_dic["case_check"]
                predicate_check = kihon_dic["predicate_check"]
                clause_type = kihon_dic["clause_type"]
                clause_func = kihon_dic["clause_func"]
                k_position = kihon_dic["position"]
                para_check = kihon_dic["para_check"]
                para_type = kihon_dic["para_type"]
                modify_type = kihon_dic["modify_type"]
                modify_check = kihon_dic["modify_check"]
                per = kihon_dic["per"]
                #--------------------------------------------
                #形態素に関する情報
                input_morp = morp_tmp_dic["input_morp"]
                reg_morp_form = morp_tmp_dic["reg_morp_form"]
                pos = morp_tmp_dic["pos"]
                dom = morp_tmp_dic["dom"]
                cat = morp_tmp_dic["cat"]

                 #一応、ネーミングは形態素から文節まで。という意味
                m_k_c_info = info(c_dependency,c_position,parallel_p_num,parallel_c_num,c_clause_type,k_dependency,predicate,main_case,tense,case_relation,kaiseki_case,morp,main,case_check,predicate_check,clause_type,clause_func,k_position,para_check,para_type,modify_type,modify_check,per,input_morp,reg_morp_form,pos,dom,cat)


                #クラスに移し替えたら、入力文の順にリストに追加していく
                out_list.append(m_k_c_info)
                """
            """
            以下、クラスをいじる時に使うだろうと（思われるメモ）
            morp_tmp_dic = {"input_morp":[],"reg_morp_form":[],"pos":[],"dom":[],"cat":[]}

            kihon_dic = {"dep":[],"predicate":[],"main_case":[],"tense":[],"case_relation":[],"kaiseki_case":[],"morp":[],"main":"","case_check":"","predicate_check":"","clause_type":[],"position":"","para_check":"","para_type":[],"modify_type":[],"modify_check":"","per":""}
            参考、クラスは以下のとおり
            def __init__(self,c_dependency,c_position,parallel_p_num,parallel_c_num,c_clause_type,k_dependency,predicate,main_case,tense,case_relation,kaiseki_case,morp,main,case_check,predicate_check,clause_type,k_position,para_check,para_type,modify_type,modify_check,per,input_morp,reg_morp_form,pos,dom,cat):

            info = info(bnst_dic["c_dep"],bnst_dic["c_position"],bnst_dic["parallel_p_num"],bnst_dic["parallel_c_num"],bnst_dic["c_clause_type"],bnst_dic[],)
            """

        #語の並び情報orderを＋１しておく
        #print "word position is",order
        order += 1
        #*から*までの情報を抽出する（文節単位での情報を抽出する）for文はここでおしまい
        #--------------------------------------
    
    #節ごとに切ってるfor文はここでおしまい
    #--------------------------------------
    
    #ここからtmp_dic_listの内容をクラスに移して、それをさらにout_listに移す
    #本質的にデータのないように違いは何もないけど、インスタンスにした方が扱いやすい
    #--------------------------------------------
    #文節と基本句に関する情報をインスタンスに移していく
    #文節に関する情報

    for one_dic in tmp_dic_list:
        c_dependency = one_dic["c_dep"]
        c_position = one_dic["c_position"]
        parallel_p_num = one_dic["parallel_p_num"]
        parallel_c_num = one_dic["parallel_c_num"]
        c_clause_type = one_dic["c_clause_type"]
        c_counter = one_dic["c_counter"]
        c_kazu = one_dic["c_kazu"]
        #--------------------------------------------
        #基本句に関する情報
        k_dependency = one_dic["k_dep"]
        predicate = one_dic["predicate"]
        main_case = one_dic["main_case"]
        tense = one_dic["tense"]
        case_relation = one_dic["case_relation"]
        kaiseki_case = one_dic["kaiseki_case"]
        morp = one_dic["morp"]
        main = one_dic["main"]
        case_check = one_dic["case_check"]
        predicate_check = one_dic["predicate_check"]
        clause_type = one_dic["clause_type"]
        clause_func = one_dic["clause_func"]
        k_position = one_dic["k_position"]
        para_check = one_dic["para_check"]
        para_type = one_dic["para_type"]
        modify_type = one_dic["modify_type"]
        modify_check = one_dic["modify_check"]
        per = one_dic["per"]
        k_counter = one_dic["k_counter"]
        k_kazu = one_dic["k_kazu"]
        #--------------------------------------------
        #形態素に関する情報
        input_morp = one_dic["input_morp"]
        reg_morp_form = one_dic["reg_morp_form"]
        pos = one_dic["pos"]
        dom = one_dic["dom"]
        cat = one_dic["cat"]
        
        #一応、ネーミングは形態素から文節まで。という意味
        m_k_c_info = info(c_dependency,c_position,parallel_p_num,parallel_c_num,c_clause_type,c_counter,c_kazu,k_dependency,predicate,main_case,tense,case_relation,kaiseki_case,morp,main,case_check,predicate_check,clause_type,clause_func,k_position,para_check,para_type,modify_type,modify_check,per,k_counter,k_kazu,input_morp,reg_morp_form,pos,dom,cat,nms)

        #クラスに移し替えたら、入力文の順にリストに追加していく
        out_list.append(m_k_c_info)
        
    #移し替えfor文はここで終了
    #--------------------------------------------
    


    #--------------------------------------
    #ここから、出力チェック用の記述
    print "About OutPut list"
    print "Contents of list is:",out_list
    for one in out_list:
        print "---------------------------------------"
        print "input_morpheme is:",one.input_morp
        print "regular morpheme is:",one.reg_morp_form
        print "pos is:",one.pos
        print "tense is:",one.tense
        print "bnst clause type is:",one.c_clause_type
        print "kihon clause type is:",one.clause_type
        print "kihon next dependenct number:",one.k_dep
        print "kihon position number:",one.k_position
        print "kihon clause function is:",one.clause_func
        print "mofifier or not:",one.modify_check
        print "case or not:",one.case_check
        print "main case is:",one.main_case
        print "main:",one.main
        print "predicate or not:",one.predicate_check
        print "kaiseki case:",one.kaiseki_case
        print "case relation is:",one.case_relation
        for one_one in one.case_relation:
            print one_one
        print "para_check is:",one.para_check
        print "para range(kihon pharase) is:",one.p_p_num
        print "para range(clause) is \n*note* includes this node and dependent node:",one.p_c_num
        print "para type is:",one.para_type
        print "counter check(kihon)",one.k_kazu
        print "counter type(kihon)",one.k_counter
    #--------------------------------------            

    return out_list
