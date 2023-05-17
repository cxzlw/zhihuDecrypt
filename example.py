from .utils import *

if __name__ == '__main__':
    raw_passage = get_cdycc(5396)  # 从C的云存储下载一篇文章
    print(detect_encrypt_method_probability(raw_passage))  # 检测文章内容多种加密情况分别的概率，加密情况分别为"none"（即未加密）或dicts中对应的文件名
    method = detect_encrypt_method(raw_passage)  # 判断文章加密情况即解密方法（结果相当于返回上面概率最大的加密情况）
    decrypted_passage = decrypt(raw_passage, method)  # 解密（原内容，解密方法），若method传"none"则返回原文
    print(decrypted_passage)  # 这是解密完的文章，恭喜你，理论上已经没有乱码了（除非选择了错误的方法即detect函数得到了错误的结论）

    # 注: 当前加密情况有"50_1", "50_2", "none". 此加
    # 密情况根据知乎的系统有可能改变，不一定是最新的

    # 注2: detect函数不是必须的, 推荐直接从网页内容获得对
    # 应的加密情况, 而不是使用detect函数. 如果我有空会建一
    # 个博客然后专门出一篇文章解释如何直接得到加密情况。现在
    # 先用detect函数吧, 当然如果你已经知道如何得到加密情况,
    # 那么根据加密情况选择下面的代码
    # decrypted_passage = decrypt(raw_passage, "none")
    # decrypted_passage = decrypt(raw_passage, "50_1")
    # decrypted_passage = decrypt(raw_passage, "50_2")
