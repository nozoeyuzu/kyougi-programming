# 特殊な計算
# 説明
# solution 関数には文字列 s が引数として与えられています。
# () 内の足し算は左辺と右辺を文字列結合した値、() 内の引き算は左辺と右辺を反転して文字列結合した値になります。

# ※ 文字列結合して得られた文字列が 0 埋めになっている場合は、0 を取り除いた値になります。

# "02" = 2
# "010" = 10
# ※ 計算式の途中で文字列が 0 埋めになっている場合も 0 を取り除いた値を使用し次の計算を行います。

# (0 + 2) = 2
# 説明：(0 + 2) の場合、文字列結合をして 02 となり、0 を取り除き、 答えは 2 になります。

# (0 - 2) = 20
# 説明：(0 - 2) の場合、左辺と右辺を逆に文字列結合して 20 となるため、答えは 20 になります。

# (0 + 2 - 1) = (2 - 1) = 12
# 説明：(0 + 2 - 0) の場合、0 と 2 を文字列結合をして 02 となるため、計算式は (2 - 1) になります。2 - 1 も括弧内かつ、引き算なので左辺と右辺を逆に文字列結合して、答えは 12 になります。
# 計算の順番は四則演算の順番のルールに従い、()の中 → 足し算・引き算の順番で計算します。
# solution 関数の戻り値として、計算結果を文字列で返すプログラムを作成してください。

# 例
# 例1:
# 入力: "(1 +2)-3"
# 出力: "9"
# 説明: 1括弧内の 1 + 2 を文字列結合して 12 - 3 になり、 12 - 3 は括弧外なので減算して答えは 9 になります。
# 例2:
# 入力: "(1 +2)+ (1 - 2)"
# 出力: "33"
# 説明: 括弧内の 1 + 2 と 1 - 2を + は左辺と右辺をそのまま文字列結合、 - は左辺と右辺を逆にして文字列結合して 12 + 21 になり、 12 + 21 は括弧外なので加算して答えは 33 になります。
# 例3:
# 入力: "((0 + 0) - 1)"
# 出力: "10"
# 説明: 括弧内の 0 + 0 を文字列結合して 00 になるので 0 を取り除き (0 - 1) になり、 0 - 1 は括弧内かつ減算なので左辺と右辺を逆に文字列結合して答えは 10 になります。
# 例4:
# 入力: "(5 - (5 + 1)) - 5"
# 出力: "510"
# 説明: 括弧内の 5 + 1 を文字列結合して (5 - 51) - 5 になり、5 - 51 を左辺と右辺を逆に文字列結合して 515 - 5 になります。 515 - 5 は括弧外なので減算して答えは 510 になります。
# 例5:
# 入力: "1+ ((2 -3) + 4 - 1 +3)"
# 出力: "13244"
# 説明: 括弧内の 2 - 3 を左辺と右辺を逆に文字列結合して 1 + (32 + 4 - 1 + 3) になり、 さらに括弧内を順番に計算して 1 + 13243 になります。1 + 13243 は括弧外なので加算して答えは 13244 になります。
# 前提
# s に含まれる文字は、0~9 の数字文字と、(, ), +, -, (半角スペース) のみです。
# s は有効な式です。
# + は単項演算として使用されません (+1 と +(2 + 3) は無効です)。
# - は単項演算として使用されます (-1と-(2 + 3)が有効です)。
# 入力に ​​2 つの連続する演算子はありません。

# def solution(s):
#     s = s.replace(' ', '')
#     while '(' in s:
#        start = -1
#        for i in range(len(s)):
#             if s[i] == '(':
#                start = i
#             elif s[i] == ')':
#                 exp = s[start+1:i]

#                 result = ''
#                 current = ''
#                 op = None

#                 for j, c in enumerate(exp):
#                     if c in '+-' and j > 0 and exp[j-1].isdigit():
#                         if result == '':
#                             result = current
#                         else:
#                             if op =='+':
#                                 result = result + current
#                             else:
#                                 result = current + result
#                             result = result.lstrip('0') or '0'
#                         current = ''
#                         op = c
#                     else:
#                         current += c

#                 if current:
#                     if result == '':
#                         result = current
#                     else:
#                         if op == '+':
#                             result = result + current
#                         else:
#                             result = current + result
#                 result = result.lstrip('0') or '0'
#                 s = s[:start] + result + s[i+1:]
#                 break
#     return str(eval(s))

# LRUCacheクラスの実装
# 説明
# LRU（Least Recently Used）キャッシュのデータ構造をクラスを用いて設計します。

# LRUとは、最近最も使われなかったデータをキャッシュから削除するキャッシュアルゴリズムを指します。
# 今回の利用頻度の更新タイミングは、getやputがcallされたときに順序を更新するものとします。
# 以下の仕様に従って、LRUCache クラスを実装してください。

# コンストラクタ
# LRUCache(int limit)
# 正の整数である limit を引数に取り初期化します。
# メソッド
# int get(string key)
# キーが存在すれば、そのキーに紐づくキャッシュの値を返します。もし存在しなければ、-1を返してください。
# このメソッドがコールされた場合、利用頻度を更新します。
# void put(string key, int value)
# キーが存在する場合は、キーに紐づくキャッシュの値を更新します。もし存在しない場合は、新しくキーと値のペアをキャッシュに追加します。
# このときに、コンストラクタで与えられた limit を超える場合、 最も最近使われなかったキーを 削除します。
# このメソッドがコールされた場合、利用頻度を更新します。
# 例
# 例1
# 入力: ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[3], ["a", 1], ["b", 2], ["a"], ["c", 3],  ["b"], ["d", 4], ["a"], ["c"], ["d"]]
# 出力: [null, null, null, 1, null, 2, null, -1, 3, 4]
# 解説:
# LRUCache lRUCache = new LRUCache(3);
# lRUCache.put("a", 1);  // {"a"=1}
# lRUCache.put("b", 2);  // {"a"=1, "b"=2}
# lRUCache.get("a");     // return 1
# lRUCache.put("c", 3);  // {"c"=3, "a"=1, "b"=2}
# lRUCache.get("b");     // return 2
# lRUCache.put("d", 4);  // {"d"=4, "c"=3, "b"=2}
# lRUCache.get("a");     // return -1
# lRUCache.get("c");     // return 3
# lRUCache.get("d");     // return 4
# 制約
# 1 <= limit <= 3000
# 0 <= value <= 10^5
# get と put は最大で、2 * 10^5 回呼ばれます。

# class LRUCache:
#     def __init__(self, limit):
#         self.limit = limit
#         self.cache = {}
#         self.order = []
    
#     def put(self, key, value):
#         if key in self.cache:
#             self.order.remove(key)
#         elif len(self.cache) >= self.limit:
#             oldest_key = self.order.pop(0)
#             del self.cache[oldest_key]

#         self.cache[key] = value
#         self.order.append(key)
    
#     def get(self, key):
#         if key in self.cache:
#             self.order.remove(key)
#             self.order.append(key)
#             return self.cache[key]
#         else:
#             return -1
    