# ゼロ値の移動
# 説明
# solution 関数にはゼロを含む int 型の配列 arr が引数として与えられました。
# solution 関数の返り値として、非ゼロ値の順番を保ったまま、 arr 内のゼロ値を末尾に移動し、結果の配列を int 型で返すプログラムを書いて下さい。
# ただしlen(arr) が大きくなったときに、計算量がなるべく抑えられるようにしてください。

# 例
# 例1:
# 入力: arr = [0,1,2,3]
# 出力: [1,2,3,0]
# 説明: 先頭の `0` を末尾に移動し、非ゼロ値である `1,2,3` の順番を保つ必要があるため
# 例2:
# 入力: arr = [4,1,0,0,5]
# 出力: [4,1,5,0,0]
# 説明: 2つ存在するゼロ値を末尾に移動し、非ゼロ値である `4,1,5` の順番を保つ必要があるため
# 前提
# 0 ≦ len(arr) ≦ 10000
# 0 ≦ arr[i] ≦ 10^3

#0を後ろに回すのではなく0以外の値を前に詰める
# def solution(arr):
#     #最後に0ではない数字を書き込んだ次のインデックスを指す
#     non_zero_position = 0
#     for i in range(len(arr)):
#         if arr[i] != 0:
#             arr[non_zero_position] = arr[i]
#             non_zero_position += 1
    
#     #残りの要素を0で埋める
#     for j in range(non_zero_position, len(arr)):
#         arr[j] = 0
#     return arr




# 二要素の足し算
# 説明
# solution 関数には int 型の配列 nums と、 int 型の値 target が引数として与えられています。
# solution 関数の戻り値として、 nums[i] + nums[j] = target となる、index i と j を int 型の配列で返すプログラムを作成してください。
# ただし、 nums[i] + nums[j] = target , i < j となる i と j の組み合わせは常に一つだけ存在します。その i, j を返却してください。

# 例
# 例1:
# 入力: nums = [1,3,7,4], target = 7
# 出力: [1,3]
# 説明: nums[1] + nums[3] = targetとなるため。2つのインデックスの組み合わせを出力とするため、nums[2]は不正解
# 例2:
# 入力: nums = [1,3,4,7,5], target = 10
# 出力: [1,3]
# 説明: nums[1] + nums[3] = targetとなるため。nums[4] + nums[4]だが、同じインデックスを2度使えないため [1,3]が正解。
# 前提
# 2 ≦ len(nums) ≦ 10000
# nums の中には必ず nums[i] + nums[j] = target となる i と j の組み合わせが１つだけ存在する
# nums[i] と target は -inf < nums[i], target < inf を満たす任意の int である
# 発展
# len(nums) が大きくなっても計算量を抑えることのできるアルゴリズムを実装しましょう。

# ヒント


# 2重For文を走ることによって、各要素同士を足し合わせ target になるかを確認します。
# 問題の前提として、 nums[i] + nums[j] で i != j な組み合わせが必ず1つしか存在しないため、組み合わせを見つけ次第 i と j を返すことができます。
# この愚直解では、2重For文の処理が O(N^2) の計算量となります。計算量を減らすために、1つのFor文で完結するアルゴリズムを考えましょう。


# ハッシュマップを使うと、 x = target - nums[i] を満たす x のインデックスが O(1) で探せます。
# nums[i] をkeyとするハッシュマップを作り、各ループで target - nums[i] がハッシュマップに存在しているかを確認します。
# この時問題は nums[i] + nums[j] = target を満たす i と j を返す必要あるので、 i もしくは j を値として格納します。


# nums[i] + x = target になる x のインデックスを O(1) で見つけることができれば、一度のループで解くことができ、計算量は 0(N)となります。
# 式を置き換えると x = target - nums[i] となる x のインデックスを探す必要があります。
# x = target - nums[i] を満たす x を探すために内側のfor文なしで探せるデータ構造はなにでしょう？

# def solution(nums, target):
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             if nums[i] + nums[j] == target:
#                 return(i, j)
# def solution(nums, target):
#     #探索したインデックスを保存
#     value_to_index = {}
#     for current_index, current_value in enumerate(nums):
#         required_value = target - current_value
#         if required_value in value_to_index:
#             return[value_to_index[required_value], current_index]
#         #現在の位置を記録
#         value_to_index[current_value] = current_index
#     return []




# HTMLタグからの特定要素の抽出
# 説明
# HTMLの特定タグの中身を出力するための関数を実装します。
# 以下の仕様に従って、必要な処理を記述してください。

# Solution関数には string型の htmlと出力対象となるタグ名 tag の2つを引数として与えられます。
# このとき、引数 html のタグの中から出力対象となるタグを出力する関数を実装してください。ただし、入力される html は以下の制約条件をすべて満たすものとします。

# 制約条件
# 引数 html に含まれるタグは <html>, <head>, <body>, <h1>, <p> のみです。それ以外のタグは存在しません。
# 開始タグ<tag>に対して、必ずただ一つの対応する終了タグ</tag>が存在します。
# htmlの仕様上は、終了タグを省略できることもありますが、この問題ではそのような入力は与えられません。
# 入力は必ず<html>で始まります。<html>の直下の子要素は、<head>と<body>のみです。ただし、<head>、<body>は存在しないこともあります。
# <head>と<body>はそれぞれ一つずつしか存在しません。
# <p>と<h1>は、<body>の直下にいくつでも存在可能です。ただし、<p>同士、<h1>同士、<p>と<h1>の間では、親子関係を持つことはできません。また、<body>が存在しない場合、<p>と<h1>は必ず存在しません。
# タグで囲まれていないテキストは存在しません。
# 例えば "<body>hoge<p>fuga</p></body>" ではhogeがタグで直接囲まれていないため、入力として不適切です。
# 出力形式
# 対象のタグの要素を各要素にもつ配列を返してください。
# 例
# 例1:
# 入力: html="<html><body>Hello World!</body></html>", tag="<body>"
# 出力: ["Hello World!"]
# 説明: htmlタグの中には、一つのbodyタグが含まれておりそれが"Hello World!"であるため出力対象となる
# 例2:
# 例2:
# 入力: html="<html><body><p>Hello World!</p><p>From HTML</p></body></html>", tag="<p>"
# 出力: ["Hello World!", "From HTML"]
# 説明: htmlタグの中には、2つのbodyタグが含まれておりそれぞれ、"Hello World!"と、"From HTML"であるため出力はカンマ区切りで出力される
# 制約:
# 1 <= len(html) <= 10^4
# html は、上記の制約条件を満たす文字列です。
# tag は、上記の制約条件を満たす文字列です。
# ヒント


# この問題の条件下では、開始タグに対応する終了タグが、ちょうど一つだけ存在します。<tag>が指定されたときに、対応する</tag>を探索することで、対象とする要素を探すことができます。また多くの言語では、文字列を扱うための関数やライブラリが提供されています。


# 対象となる要素が複数存在する場合はどのタグが対応しているでしょうか？入力に “<p></p><p></p>” とあった場合、一つ目の<p>に対応する</p>は2つのうちどちらでしょうか？


# この問題の条件では、同じ要素が入れ子構造にならないことに注意してください。つまり、入力に "<p></p><p></p>" とあった場合、一つ目の<p>に一つ目の</p>が対応することが保証されます。

# def solution(html: str, tag: str) -> list[str]:
#     results: list[str] = []
#     tag_name = tag.strip("<>")
#     open_tag = f"<{tag_name}>"
#     close_tag = f"</{tag_name}>" 
#     search_position = 0

#     while True:
#         # 開始タグ
#         start_index = html.find(open_tag, search_position)
#         if start_index == -1:
#             break
#         # 中身の開始位置
#         content_start = start_index + len(open_tag)
#         # 終了タグ
#         end_index = html.find(close_tag, content_start)

#         # 開始タグと終了タグの間のテキストを抽出
#         inner_text = html[content_start:end_index]
#         results.append(inner_text)

#         # 次の検索は、この終了タグのさらに後ろから開始
#         search_position = end_index + len(close_tag)

#     return results
    