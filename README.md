SensitivePy
===========

使用python开发的极简的敏感词过滤系统
-----------

API LIST
-----------
1.检测敏感词<br />
URL   http://your_domain/check<br />
参数名         请求类型        可选            长度<br />
words   POST   false  65535
<br />
返回格式：json<br />
{"count":1,"data":[[0,6,"\u6bcd\u5b5d"]]}
<br />
2.过滤敏感词<br />
URL   http://your_domain/replace<br />
参数名         请求类型        可选            长度<br />
words   POST   false  65535<br />
返回格式：text<br />
**这是已经过滤的文本**,还好<br />

words.txt为敏感词文件<br />

### 安装说明<br />
先通过pip或easy_install安装bottle框架<br />
再修改localbottle里的端口设置和域名设置，再使用python 启动即可<br />
*通过云环境的需要修改一下配置，保留wsgi.py，具体参考云环境的说明<br />

### 更新说明<br />
2014/10/7  <br />
1.完成核心检测和过滤API<br />
2.集成bottle框架<br />
3.检测使用DFA过滤算法<br />

2015/4/1 by tanliang<br />
1.环境  python 2.7.x, centos 6.x/windows7<br />
2.pip install gevent (yum install python-devel)<br />
3.增加 /update 接口，即时更新 words.txt，需 watchdog 支持<br />
4.启动 python pymonitor.py localbottle.py<br />
5.附 PHP 的混淆字符过滤<br />
```php
$quanjiao = array('０' => '0', '１' => '1', '２' => '2', '３' => '3', '４' => '4','５' => '5', '６' => '6', '７' => '7', '８' => '8', '９' => '9', 'Ａ' => 'A', 'Ｂ' => 'B', 'Ｃ' => 'C', 'Ｄ' => 'D', 'Ｅ' => 'E','Ｆ' => 'F', 'Ｇ' => 'G', 'Ｈ' => 'H', 'Ｉ' => 'I', 'Ｊ' => 'J', 'Ｋ' => 'K', 'Ｌ' => 'L', 'Ｍ' => 'M', 'Ｎ' => 'N', 'Ｏ' => 'O','Ｐ' => 'P', 'Ｑ' => 'Q', 'Ｒ' => 'R', 'Ｓ' => 'S', 'Ｔ' => 'T','Ｕ' => 'U', 'Ｖ' => 'V', 'Ｗ' => 'W', 'Ｘ' => 'X', 'Ｙ' => 'Y','Ｚ' => 'Z', 'ａ' => 'a', 'ｂ' => 'b', 'ｃ' => 'c', 'ｄ' => 'd','ｅ' => 'e', 'ｆ' => 'f', 'ｇ' => 'g', 'ｈ' => 'h', 'ｉ' => 'i','ｊ' => 'j', 'ｋ' => 'k', 'ｌ' => 'l', 'ｍ' => 'm', 'ｎ' => 'n','ｏ' => 'o', 'ｐ' => 'p', 'ｑ' => 'q', 'ｒ' => 'r', 'ｓ' => 's', 'ｔ' => 't', 'ｕ' => 'u', 'ｖ' => 'v', 'ｗ' => 'w', 'ｘ' => 'x', 'ｙ' => 'y', 'ｚ' => 'z','（' => '(', '）' => ')', '〔' => '[', '〕' => ']', '【' => '[','】' => ']', '〖' => '[', '〗' => ']', '“' => '[', '”' => ']','‘' => '[', '\'' => ']', '｛' => '{', '｝' => '}', '《' => '<','》' => '>','％' => '%', '＋' => '+', '—' => '-', '－' => '-', '～' => '-','：' => ':', '。' => '.', '、' => ',', '，' => '.', '、' => '.', '；' => ',', '？' => '?', '！' => '!', '…' => '-', '‖' => '|', '”' => '"', '\'' => '`', '‘' => '`', '｜' => '|', '〃' => '"','　' => ' ');
$num_char = array('①'=>'1','②'=>'2','③'=>'3','④'=>'4','⑤'=>'5','⑥'=>'6','⑦'=>'7','⑧'=>'8','⑨'=>'9','⑩'=>'10','⑴'=>'1','⑵'=>'2','⑶'=>'3','⑷'=>'4','⑸'=>'5','⑹'=>'6','⑺'=>'7','⑻'=>'8','⑼'=>'9','⑽'=>'10','一'=>'1','二'=>'2','三'=>'3','四'=>'4','五'=>'5','六'=>'6','七'=>'7','八'=>'8','九'=>'9','零'=>'0', '壹'=> '1', '贰'=> '2', '叁' => '3', '肆' => '4', '伍' => '5', '陆' => '6', '柒' => '7', '捌' => '8', '玖' => '9');
$words = strtr($words, $quanjiao);
$words = strtr($words, $num_char);
        
$words = preg_replace('/\s/','',preg_replace("/[[:punct:]]/",'',strip_tags(html_entity_decode($words,ENT_QUOTES,'UTF-8'))));
```

<br />
重庆尚简科技工作室(http://www.sj-kj.com) caroltc(312493732@qq.com)
