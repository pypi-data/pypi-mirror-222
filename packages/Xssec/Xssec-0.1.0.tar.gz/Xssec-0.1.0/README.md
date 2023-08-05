# Xssec
Xssec是一个Python文本加密库，由诗软科技制作


## 安装

```
pip install xssec
```


## 使用方法

```python
from xssec import lock, unlock

# 设置密码
psw = 123

# 对文本进行加密
text = "你好，世界！"
lock_txt = lock(text, psw)
print("加密后的文本:", lock_txt)

# 将加密文本解密
unlock_txt = unlock(lock_txt, psw)
print("解密后的文本:", unlock_txt)
```



_txt, psw)
print("解密后的文本:", umlock_txt)
```







