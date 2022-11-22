本文件夹为杨哲思开发文件夹，现捐给零剑游戏程序组。
建议开发者使用Visual Studio Code开发。code.visualstudio.com
文件介绍：

ATE.js
 测试版ATE2。
 如要游玩测试版，请在 [[User:你的用户名/common.js]] 添加
 mw.loader.load("//cloudvillage.miraheze.org/wiki/User:ZeScript/ate.js?action=raw&ctype=text/javascript");
 然后到 [[User:ZeScript/ate]] 游玩。
ATELTS.js
 未压缩正式版ATE2。其与ATE.js的差异仅在末尾。
 这个文件不会出现在CVWiki。
ATE.min.js
 压缩后的正式版ATE2。
ATESolo.js
 独立发行的ATE未压缩版本。
 这个文件不会出现在CVWiki。
ATESolo.min.js
 独立发行的ATE的压缩版本。
 这个文件不会出现在CVWiki。
edit.py
 用于将ATE.js转化为独立版和正式版。（按照井号注释）
Compress.bat
 用于压缩JS文件。
 请先到官网安装Node.js并安装NPM（Node Package Manager, 通常与Node.js捆绑），
 然后在cmd中使用 npm -i uglify-js -g 安装uglifyjs
 之后双击该文件（Compress.bat）即可更新ATE.min.js（请先保存LTS文件）
 （Compress2.bat也要使用，更新ATESolo.min.js，因为uglifyjs只能一个文件用一次就退，不知道为什么）
 如果嫌麻烦就别压缩，群里把整个文件传给我就是了（
 不过目前也没人改动JS就是了（
data.json
 数据文件。为保持注释版优先，请不要直接修改。
data.jsonc
 带有注释的数据。请编辑该文件，并用removeComments.py更新到无注释文件。

其他Python文件请见头部注释。
