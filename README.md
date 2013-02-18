# KNP Parser written by Python

***
####概要
KNPは日本語解析器なので、日本語で書きます。
日本語解析器のKNPの結果を見やすいように整形＋必要（と思われる）情報を取って来てくれるスクリプトです。KNPの-tabオプションを利用しています。
 
別の目的で作成していたので、コードの内容は荒書きですが、動きます。

***

####必要な物

juman **JUMAN Ver.7.0**   
<http://nlp.ist.i.kyoto-u.ac.jp/index.php?cmd=read&page=JUMAN&alias%5B%5D=%E6%97%A5%E6%9C%AC%E8%AA%9E%E5%BD%A2%E6%85%8B%E7%B4%A0%E8%A7%A3%E6%9E%90%E3%82%B7%E3%82%B9%E3%83%86%E3%83%A0JUMAN>

KNP **KNP Ver.4.0.1**   
 <http://nlp.ist.i.kyoto-u.ac.jp/index.php?KNP>

古いバージョンのjumanだと文字コードの都合上、動作しません。

***
####動かし方

KNPやJUMANを標準とは違う所にインストールした場合

main.pyの１０１行目〜１０７行目の部分を書き換えてください。
書き換え先は自分の環境でKNPとJUMANのパスが通っている所です。

例:/usr/local/binにjumanのパスが通っている場合   
    juman = subprocess.Popen(['/usr/local/bin/juman'],   
に書き換える。

***
####使い方

python main.py

を実行すると、日本語を打つように言うので、日本語打ってください。

***
####見方

例えば「私は朝、運動をします。」と入力すると、下の様に表示されます。

<pre><code>
私は朝、運動に出かける。
-----------------------------
Number of Clauses is 4
List of lines in each clause [4, 4, 4, 3]
About OutPut list
Contents of list is: [<syori.info instance at 0x10d581b00>, <syori.info instance at 0x10d581b48>, <syori.info instance at 0x10d581b90>, <syori.info instance at 0x10d581bd8>]
---------------------------------------
input_morpheme is: 私
regular morpheme is: 私
pos is: 名詞
tense is: []
bnst clause type is: 
kihon clause type is: 
kihon next dependenct number: 3
kihon position number: 0
kihon clause function is: 
mofifier or not: 
case or not: yes
main case is: 
main: yes
predicate or not: 
kaiseki case: ガ
case relation is: []
para_check is: 
para range(kihon pharase) is: []
para range(clause) is 
*note* includes this node and dependent node: []
para type is: []
counter check(kihon) 
counter type(kihon) 
---------------------------------------
input_morpheme is: 朝
regular morpheme is: 朝
pos is: 名詞
tense is: []
bnst clause type is: 
kihon clause type is: 
kihon next dependenct number: 3
kihon position number: 1
kihon clause function is: 
mofifier or not: 
case or not: yes
main case is: 
main: 
predicate or not: 
kaiseki case: 時間
case relation is: []
para_check is: yes
para range(kihon pharase) is: 
para range(clause) is 
*note* includes this node and dependent node: 
para type is: ？
counter check(kihon) 
counter type(kihon) 
---------------------------------------
input_morpheme is: 運動
regular morpheme is: 運動
pos is: 名詞
tense is: []
bnst clause type is: 連用節
kihon clause type is: 連用節
kihon next dependenct number: 3
kihon position number: 2
kihon clause function is: 
mofifier or not: 
case or not: 
main case is: 
main: 
predicate or not: yes
kaiseki case: []
case relation is: ['\xe6\x99\x82\xe9\x96\x93:\xe6\x9c\x9d']
時間:朝
para_check is: 
para range(kihon pharase) is: []
para range(clause) is 
*note* includes this node and dependent node: []
para type is: []
counter check(kihon) 
counter type(kihon) 
---------------------------------------
input_morpheme is: 出かける
regular morpheme is: 出かける
pos is: 動詞
tense is: 未来
bnst clause type is: 主節
kihon clause type is: 主節
kihon next dependenct number: -1
kihon position number: 3
kihon clause function is: 
mofifier or not: 
case or not: yes
main case is: 一人称優位
main: 
predicate or not: yes
kaiseki case: []
case relation is: ['\xe3\x82\xac:\xe7\xa7\x81']
ガ:私
para_check is: 
para range(kihon pharase) is: []
para range(clause) is 
*note* includes this node and dependent node: []
para type is: []
counter check(kihon) 
counter type(kihon) 
</code></pre>

と表示されます。  

<pre><code>
-----------------------------
Number of Clauses is 4
List of lines in each clause [4, 4, 4, 3]
About OutPut list
Contents of list is: [<syori.info instance at 0x10d581b00>, <syori.info instance at 0x10d581b48>, <syori.info instance at 0x10d581b90>, <syori.info instance at 0x10d581bd8>]
---------------------------------------
</code></pre>

Number of Clauses is  :文節数を示します。  
List of lines in each clause :KNP -tabオプションを何行ごとに区切るのか？をしめしています。  
Contents of list is: 各句をインスタンスとして保存して、リストに格納します。その結果を表示しています。   

各句に関する情報は以下の通りです。    
<pre><code>
input_morpheme is: 私
regular morpheme is: 私
pos is: 名詞
tense is: []
bnst clause type is: 
kihon clause type is: 
kihon next dependenct number: 3
kihon position number: 0
kihon clause function is: 
mofifier or not: 
case or not: yes
main case is: 
main: yes
predicate or not: 
kaiseki case: ガ
case relation is: []
para_check is: 
para range(kihon pharase) is: []
para range(clause) is 
*note* includes this node and dependent node: []
para type is: []
counter check(kihon) 
counter type(kihon) 
</code></pre>

input_morpheme:入力されたままの形態素が表示されます   
regular_morpheme:正規化された形態素が表示されます   
pos:品詞が表示されます
tense:動詞の場合、時制が表示   
bnst clause type:文節の機能を表示   
kihon caluse type:基本句の機能を表示（大体は文節の機能と同じ）   
kihon next dependent number:基本句が次にかかるのは何番目の句か？    
kihon position number:基本句の番号   
modifier or not:修飾語かどうか   
case or not:格かどうか        
main case is:（基本句が述語のときのみ）主格は何か？    
main:（基本句が）主格かどうか？    
predicate or not:述語かどうか？    
kaiseki case:（格の場合）何格の役割か？     
case relation is:（述語の時）他の格との関係    
para_check:並列のチェック    
para range(kihon pharase) is:（基本句単位で）何句にわたって並列しているか？   
para range(clause) is 
*note* includes this node and dependent node:（文節単位で）何句にわたって並列しているか？    
para type is:並列のタイプは何か？     
counter check(kihon):数詞の場合にチェックが入る     
counter type(kihon) :数詞はどのタイプか？   


*述語や修飾語や格の取り扱いは益岡文法体系によります。

***
####コードの挙動

上の様に１句ずつ情報を取得して、インスタンスとします。そして、リストに格納します。out_listがそのリストです。